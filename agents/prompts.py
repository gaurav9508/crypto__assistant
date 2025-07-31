class PromptManager:
    def get_market_analysis_prompt(self, coin_data):
        return f"""
            You are a professional crypto analyst. Analyze the following market data for top-performing coins in the last 24 hours:

            {coin_data}`

            Provide concise investment insights in 5-6 bullet points.
            Include short-term and long-term potential, risks, and key observations.
            """

    def get_portfolio_analysis_prompt(self, portfolio_data):
        return f"""
            You are a crypto portfolio advisor. Here is the user's current portfolio:

            {portfolio_data}

            Analyze it and suggest:
            - Improvements or rebalancing opportunities
            - Risk management tips
            - Diversification ideas (if needed)
            Be concise and specific.
            """

    def get_general_query_prompt(self, question):
        return f"""
            You are an expert in cryptocurrency and blockchain.

            User question:
            "{question}"

            Respond clearly and concisely. If relevant, reference market trends or investor best practices.
            """
