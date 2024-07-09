from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import bcrypt
import jwt
import time

from config import Settings
from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
    #updated_date = Column(DateTime(timezone=True), server_default=datetime.now(), onupdate=datetime.now())
    #created_date = Column(DateTime(timezone=True), server_default=datetime.now())
    is_admin: Mapped[bool]

    @staticmethod
    def hash_password(password) -> str:
        """Transforms password from it's raw text form to 
        cryptographic hashes
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def validate_password(self, password) -> bool:
        """Confirms password is valid"""
        return bcrypt.checkpw(password, self.password)


    def generate_token(self) -> dict:
        """Generate access token for user"""
        return {
            "access_token": jwt.encode(
                {
                    "id": self.id,
                    "email": self.email,
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "is_admin": self.is_admin,
                    "expires": time.time() + 600,
                },
                Settings.jwt_secret,
                Settings.jwt_algorithm
        )
    }