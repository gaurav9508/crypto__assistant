from utils import logger, load_env_vars
from binance_client import BinanceClient
from agents.agent_core import CryptoAgent
from telegram_bot import CryptoTelegramBot


def main():
    """Main application entry point"""
    try:
        logger.info("Starting Crypto Investment Assistant...")

        # Load env vars
        env_vars = load_env_vars()
        logger.info("Environment variables loaded successfully")

        # Init services
        binance_client = BinanceClient()
        logger.info("✅ Binance client initialized")

        crypto_agent = CryptoAgent(
            api_key=env_vars['GEMINI_API_KEY'],
            project_id=env_vars.get('GOOGLE_CLOUD_PROJECT_ID')
        )
        logger.info("✅ Crypto agent initialized")

        telegram_bot = CryptoTelegramBot(
            token=env_vars['TELEGRAM_BOT_TOKEN'],
            binance_client=binance_client,
            crypto_agent=crypto_agent
        )
        logger.info("✅ Telegram bot initialized")
        logger.info("🚀 Starting Telegram bot...")

        telegram_bot.run()

    except KeyboardInterrupt:
        logger.info("👋 Exiting gracefully...")
    except Exception as e:
        logger.error(f"Application error: {e}")
        logger.exception("Full error traceback:")
        raise
    finally:
        logger.info("Application shutdown complete")


if __name__ == "__main__":
    main()
