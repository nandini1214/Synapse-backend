from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    tags=["Test"]
)

@router.get("/")
async def test_api():
    return {
        "status": "success",
        "message": "Synapse backend is working"
    }