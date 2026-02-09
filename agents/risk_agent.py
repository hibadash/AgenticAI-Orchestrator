import asyncio
import logging

class RiskAgent:
    async def run(self, incident_text, classification):
        await asyncio.sleep(0.5)
        logging.info("RiskAgent evaluating severity...")
        
        # Simulated AI logic
        if "high speed" in incident_text.lower() or classification == "Brake system anomaly":
            return "High"
        elif classification == "Collision-related incident":
            return "Critical"
        return "Medium"
