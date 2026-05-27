from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.student import Student
from app.schemas.student import (
    StudentCreate,
    StudentOut
)

from app.core.security import (
    get_current_user
)

router = APIRouter()


@router.post(
    "/students",
    response_model=StudentOut
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_student = Student(**student.dict())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.get(
    "/students",
    response_model=list[StudentOut]
)
def get_students(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Student).all()