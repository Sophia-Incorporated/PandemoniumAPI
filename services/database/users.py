from sqlalchemy.orm import Session
from sqlalchemy import select

from models.user import User
from schemas.user_schema import UserCreationSchema

async def create_user(session: Session, user:UserCreationSchema):
    new_user = User(**user.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
