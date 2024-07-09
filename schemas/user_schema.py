from pydantic import BaseModel, Field, EmailStr

class UserBaseSchema(BaseModel):
    email: str
    first_name: str
    last_name: str

class UserSchema(UserBaseSchema):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True

class UserFullSchema(UserSchema):
    password: str

class UserCreationSchema(UserBaseSchema):
    password: str

class UserLoginSchema(BaseModel):
    email: str
    password: str