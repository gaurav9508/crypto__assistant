import re

class ResponseFormatter:
    def clean(self, text):
        # Remove unwanted markdown characters
        return re.sub(r'[*_`\\]', '', text).strip()

    def format_analysis_response(self, response_text):
        cleaned = self.clean(response_text)
        return f"📈 Market Analysis Result:\n{cleaned}"

    def format_portfolio_response(self, response_text):
        cleaned = self.clean(response_text)
        return f"💼 Portfolio Insight:\n{cleaned}"

    def format_general_response(self, response_text):
        cleaned = self.clean(response_text)
        return f"❓ Answer:\n{cleaned}"
