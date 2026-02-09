import asyncio
import logging

from agents.classifier_agent import ClassifierAgent
from agents.risk_agent import RiskAgent
from agents.recommendation_agent import RecommendationAgent
from orchestrator.supervisor import SupervisorAgent

logging.basicConfig(level=logging.INFO)

async def main():
    # Create agents
    classifier = ClassifierAgent()
    risk = RiskAgent()
    recommender = RecommendationAgent()
    supervisor = SupervisorAgent(classifier, risk, recommender)

    # Sample incident
    incident_text = "Vehicle reported sudden braking and dashboard warning at high speed."

    # Run orchestration
    result = await supervisor.orchestrate(incident_text)
    print("\n--- Agentic Orchestration Result ---")
    print(result)

# Run main async function
asyncio.run(main())
