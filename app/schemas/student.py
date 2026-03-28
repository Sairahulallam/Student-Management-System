from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str

class StudentOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True