import asyncio
import logging

class RecommendationAgent:
    async def run(self, classification, risk_level):
        await asyncio.sleep(0.5)
        logging.info("RecommendationAgent generating recommendation...")
        
        if risk_level in ["High", "Critical"]:
            return "Immediate inspection required. Vehicle should not be driven."
        return "Schedule maintenance at earliest convenience."
