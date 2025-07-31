# 🪙 Crypto Investment Assistant

This project is a **Crypto Investment Advisor Bot** that fetches real-time market data from Binance and uses a Gemini-powered AI agent to analyze market trends, provide investment insights, and respond to user queries via Telegram.

---

## 🚀 Features

* 📈 Fetches top cryptocurrency prices using Binance API.
* 🧠 Uses Gemini LLM to provide investment analysis.
* 🤖 Telegram bot interface for user interaction.
* 🔡️ Environment variables for secure API key management.
* 📈 Insights on market trends, opportunities, and risks.

---

## 📦 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/crypto-investment-assistant.git
   cd crypto-investment-assistant
   ```

2. **Create Virtual Environment & Install Dependencies**

   ```bash
   conda create --name cryptoenv python=3.11
   conda activate cryptoenv
   pip install -r requirements.txt
   ```

3. **Add Your API Keys**

   * Create a `.env` file at the root with the following variables:

     ```env
     BINANCE_API_KEY=your_binance_key
     BINANCE_SECRET_KEY=your_binance_secret
     GEMINI_API_KEY=your_gemini_key
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     ```

---

## 🧪 Run the App

Start the Telegram bot:

```bash
python telegram_bot.py
```

---

## 📁 Project Structure

```
.
├── agents/                  # AI prompt and analysis logic
├── binance_client.py        # Handles Binance API calls
├── telegram_bot.py          # Telegram bot logic
├── utils.py                 # Helper functions
├── .env                     # API keys and secrets (not committed)
├── .gitignore               # Ignored files
├── main.py                  # Optional CLI/entrypoint
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

---

## 📬 Telegram Commands

* `/start` — Welcome message
* `/insight` — Get latest market insights
* `/ask` — Ask AI about the market

---

## 📌 Notes

* Gemini is used to generate intelligent financial insights based on real-time crypto data.
* Binance public API is used to fetch prices (top coins or all coins).
* The bot can be deployed on any server that supports long polling or webhooks.

---

## 💡 Contributions

Feel free to fork and contribute by improving prompts, adding new exchanges, or UI layers!
