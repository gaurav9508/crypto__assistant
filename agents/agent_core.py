import google.generativeai as genai
from .prompts import PromptManager
from .formatter import ResponseFormatter

class CryptoAgent:
    def __init__(self, api_key, project_id=None):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.prompt_manager = PromptManager()
        self.formatter = ResponseFormatter()

    def analyze_market(self, coin_data):
        prompt = self.prompt_manager.get_market_analysis_prompt(coin_data)
        response = self.model.generate_content(prompt)
        return self.formatter.format_analysis_response(self._extract_text(response))

    def analyze_portfolio(self, portfolio_data):
        prompt = self.prompt_manager.get_portfolio_analysis_prompt(portfolio_data)
        response = self.model.generate_content(prompt)
        return self.formatter.format_portfolio_response(self._extract_text(response))

    def answer_question(self, question):
        prompt = self.prompt_manager.get_general_query_prompt(question)
        response = self.model.generate_content(prompt)
        return self.formatter.format_general_response(self._extract_text(response))

    def _extract_text(self, response):
        if hasattr(response, 'text') and response.text.strip():
            return self._clean_response(response.text.strip())
        if hasattr(response, 'candidates') and response.candidates:
            return self._clean_response(response.candidates[0].content.parts[0].text.strip())
        return "No response"

    def _clean_response(self, text):
        # Remove unnecessary escape characters and extra whitespace
        cleaned = text.replace("\\", "").replace("`", "").strip()
        return cleaned
