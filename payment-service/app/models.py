from pydantic import BaseModel

class Payment(BaseModel):
    user_email: str
    amount: float