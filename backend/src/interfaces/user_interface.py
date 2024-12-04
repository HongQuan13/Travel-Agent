from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    email: str


class CreateUserResponse(BaseModel):
    id: int
    username: str
    email: str
