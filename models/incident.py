from pydantic import BaseModel

class Incident(BaseModel):
    description: str
    classification: str = None
    risk: str = None
    recommendation: str = None
