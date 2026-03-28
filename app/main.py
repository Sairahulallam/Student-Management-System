from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import student, course, enrollment, user
from app.routes import student as student_routes
from app.routes import course as course_routes
from app.routes import enrollment as enrollment_routes
from app.routes import auth as auth_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_routes.router)
app.include_router(course_routes.router)
app.include_router(enrollment_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Student API running"}