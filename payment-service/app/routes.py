from fastapi import APIRouter
from app.models import Payment

router = APIRouter()

@router.post("/pay")
def make_payment(payment: Payment):
    # Mock payment logic
    if payment.amount > 0:
        return {"message": "Payment successful"}
    return {"message": "Payment failed"}