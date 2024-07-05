from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        'name': 'John Doe',
        'age': 20,
        'grade': 'A'
    }
}

class Teacher(BaseModel):
    name: str
    age: int
    grade: str


@app.get("/get_teacher")
def get_teacher(teacher_id: int = Path(..., gt=0, description="Teacher ID")):
    teacher = Teacher(**students[teacher_id])
    return teacher

@app.post("/teacher")
def create_teacher(teacher: Teacher):
    students[teacher.id] = teacher.dict()
    return {"message": "Teacher created successfully"}


@app.get("/")
def index():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/get_student")
def get_student(student_id: int = Path(..., gt=0, description="Student ID")):
    return  students.get(student_id, {"error": "Student not found"})


@app.post("/add_student")
def add_student(student_id: int, name: str, age: int, grade: str):
    if student_id in students:
        return {"error": "Student ID already exists"}
    students[student_id] = {'name': name, 'age': age, 'grade': grade}
    return {"message": "Student added successfully"}


@app.put("/update_student/{student_id}")
def update_student(student_id: int, name: str = None, age: int = None, grade: str = None):
    if student_id not in students:
        return {"error": "Student not found"}
    if name:
        students[student_id]['name'] = name
    if age:
        students[student_id]['age'] = age
    if grade:
        students[student_id]['grade'] = grade
    return {"message": "Student updated successfully"}


@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted successfully"}

@app.get("/get_all_students")
def get_all_students():
    return students

@app.get("/get_student_by_name/{name}")
def get_student_by_name(name: Optional[str] = None): 
    for student_id, student in students.items():
        if student['name'] == name:
            return student
    return {"error": "Student not found"}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)