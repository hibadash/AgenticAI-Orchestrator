import asyncio
import logging

class SupervisorAgent:
    def __init__(self, classifier, risk, recommender):
        self.classifier = classifier
        self.risk = risk
        self.recommender = recommender

    async def orchestrate(self, incident_text):
        logging.info("SupervisorAgent starting orchestration")

        # Step 1: Classification
        classification = await self.classifier.run(incident_text)
        logging.info(f"Classifier output: {classification}")

        # Step 2: Risk assessment
        risk_level = await self.risk.run(incident_text, classification)
        logging.info(f"Risk output: {risk_level}")

        # Step 3: Recommendation
        recommendation = await self.recommender.run(classification, risk_level)
        logging.info(f"Recommendation output: {recommendation}")

        # Step 4: Agentic behavior: re-assess if output is uncertain
        if risk_level == "Unknown":
            logging.warning("Risk unknown, asking RiskAgent to re-assess")
            risk_level = await self.risk.run(incident_text, classification)

        return {
            "classification": classification,
            "risk": risk_level,
            "recommendation": recommendation
        }
