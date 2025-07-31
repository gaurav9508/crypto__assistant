import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from utils import escape_markdown

logger = logging.getLogger(__name__)

class CryptoTelegramBot:
    def __init__(self, token, binance_client, crypto_agent):
        self.token = token
        self.binance_client = binance_client
        self.crypto_agent = crypto_agent
        self.app = ApplicationBuilder().token(self.token).build()
        self._register_handlers()

    def _register_handlers(self):
        self.app.add_handler(CommandHandler("start", self.handle_start))
        self.app.add_handler(CommandHandler("analyze", self.handle_analyze))
        self.app.add_handler(CommandHandler("ask", self.handle_ask))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text))

    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_message = (
            "👋 Welcome to the *Crypto Investment Assistant*\n\n"
            "Commands:\n"
            "• /analyze - Market analysis\n"
            "• /ask [question] - Ask investment questions\n"
            "• Or type a question directly!"
        )
        await update.message.reply_text(welcome_message, parse_mode='Markdown')

    async def handle_analyze(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("📊 Analyzing the market...")

        try:
            top_symbols = self.binance_client.get_top_symbols(limit=5)
            coin_data = []

            for symbol in top_symbols:
                price = self.binance_client.get_price(symbol)
                if price:
                    coin_data.append(f"{symbol}: ${price:.2f}")

            coin_data_str = "\n".join(coin_data)
            result = self.crypto_agent.analyze_market(coin_data_str)

            if result:
                await update.message.reply_text(f"📈 Market Analysis:\n{result}")
            else:
                await update.message.reply_text("❌ Market analysis failed. Please try again later.")

        except Exception as e:
            await update.message.reply_text(f"⚠️ Error: {str(e)}")


    async def handle_ask(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("❓ Please ask something after /ask\nExample: /ask Should I buy ETH now?")
            return

        question = ' '.join(context.args)
        await self._process_question(update, question)

    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        question = update.message.text
        await self._process_question(update, question)

    async def _process_question(self, update: Update, question: str):
        try:
            loading_msg = await update.message.reply_text("🤔 Thinking about that...")

            # Get market data for context
            top_symbols = self.binance_client.get_top_symbols(limit=3)
            market_data = {symbol: self.binance_client.get_price(symbol) for symbol in top_symbols}

            # Ask AI
            answer = self.crypto_agent.answer_question(f"{question}\n\nMarket Data: {market_data}")
            formatted = escape_markdown(answer)
            await loading_msg.edit_text(formatted, parse_mode='MarkdownV2')

        except Exception as e:
            logger.error(f"Question error: {e}")
            await update.message.reply_text("❌ Could not process your question.")

    def run(self):
        self.app.run_polling()