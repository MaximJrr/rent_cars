from pydantic import BaseModel, EmailStr


class SUser(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr
    passport_id: str
    phone_number: str

    class Config:
        orm_mode = True


class SUsersAuth(BaseModel):
    email: EmailStr
    password: str


class SUserUpdate(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    passport_id: str
    phone_number: str


class SUserUpdatePartial(SUserUpdate):
    name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    passport_id: str | None = None
    phone_number: str | None = None

    class Config:
        orm_mode = True
