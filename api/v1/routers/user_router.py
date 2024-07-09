from schemas.user_schema import UserSchema, UserCreationSchema
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from database import get_db_session
from models import User
from services.database import users as user_db_services


router = APIRouter(
    prefix="/api/v1/user",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/register", response_model=UserCreationSchema)
def register_user(payload: UserCreationSchema = Body(), session: Session=Depends(get_db_session)):
    """Processes request to register user account."""
    payload.password = User.hash_password(payload.password)
    return user_db_services.create_user(session, user=payload)

@router.post("/login")
def login():
    """Processes user's credentials and returns a token on succesful authentication.

    request body:

    - Email: Unique identifier for the user

    - Password: """
    return "ThisTokenIsFake"