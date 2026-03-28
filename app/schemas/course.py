from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str

class CourseOut(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True