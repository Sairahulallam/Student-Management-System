from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.enrollment import Enrollment

router = APIRouter()

@router.post("/enroll")
def enroll(student_id: int, course_id: int, db: Session = Depends(get_db)):
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()
    return {"message": "Student enrolled"}