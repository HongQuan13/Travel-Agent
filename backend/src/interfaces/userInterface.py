from pydantic import BaseModel


class UserRequest(BaseModel):
    username: str
    email: str


class CreateUserResponse(BaseModel):
    id: int
    username: str
    email: str
