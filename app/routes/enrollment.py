from app.core.security import get_current_user
from fastapi import Depends, APIRouter
router = APIRouter()
@router.post("/enroll")
def enroll(
    student_id: int,
    course_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    enrollment = Enrollment(
        student_id=student_id,
        course_id=course_id
    )

    db.add(enrollment)
    db.commit()

    return {"message": "Student enrolled"}