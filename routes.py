from models.user import User
from fastapi import Depends, APIRouter, HTTPException
from services.user_service import get_service, UserService


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(user: User, service: UserService = Depends(get_service)):
    existing_user = await service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    user_id = await service.create_user(user)
    return {"message": "User created", "id": user_id}

@router.get("/")
async def list_users(service: UserService = Depends(get_service)):
    return await service.get_all_users()

@router.get("/{user_id}")
async def read_user(user_id: str, service: UserService = Depends(get_service)):
    user_data = await service.get_user_by_id(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data