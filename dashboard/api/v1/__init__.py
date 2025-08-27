from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["v1"])

@router.get("/status")
def get_status():
    return {"status": "ok"}

@router.get("/ping")
def ping():
    return {"ping": "pong"}