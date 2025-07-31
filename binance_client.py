import requests
import logging

class BinanceClient:
    """
    Binance client for fetching market data using public endpoints.
    No authentication required for public market data.
    """

    BASE_URL = "https://api.binance.com/api/v3"

    def __init__(self):
        self.session = requests.Session()

    def get_price(self, symbol="BTCUSDT"):
        """
        Fetches current price of the given symbol (default: BTC/USDT).
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/ticker/price", params={"symbol": symbol})
            response.raise_for_status()
            data = response.json()
            return float(data["price"])
        except Exception as e:
            logging.error(f"Failed to fetch price for {symbol}: {e}")
            return None

    def get_top_symbols(self, limit=5):
        """
        Returns top traded symbols by volume.
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/ticker/24hr")
            response.raise_for_status()
            tickers = response.json()
            sorted_tickers = sorted(tickers, key=lambda x: float(x["quoteVolume"]), reverse=True)
            return [t["symbol"] for t in sorted_tickers[:limit]]
        except Exception as e:
            logging.error(f"Failed to fetch top symbols: {e}")
            return []
        
    def get_top_gainers_24h(self, limit=5):
        try:
            response = requests.get(f"{self.BASE_URL}/ticker/24hr")
            response.raise_for_status()
            data = response.json()

            # Filter to only USDT pairs
            usdt_pairs = [coin for coin in data if coin['symbol'].endswith("USDT")]

            # Sort by percentage gain (descending)
            sorted_data = sorted(usdt_pairs, key=lambda x: float(x['priceChangePercent']), reverse=True)

            return sorted_data[:limit]

        except Exception as e:
            print(f"[BinanceClient] Error fetching 24hr gainers: {e}")
            return []