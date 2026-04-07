from fastapi import APIRouter

router = APIRouter()

@router.post("/notify")
def send_notification(user_email: str, message: str):
    return {
        "message": f"Notification sent to {user_email}: {message}"
    }