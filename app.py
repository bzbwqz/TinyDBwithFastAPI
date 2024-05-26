from pydantic import BaseModel, Field
from tinydb import TinyDB, Query
from fastapi import FastAPI, HTTPException
import uvicorn
from enum import Enum

# 定义枚举类
class GradeEnum(str, Enum):
    grade_one = "Grade One"
    grade_two = "Grade Two"
    grade_three = "Grade Three"

# 定义学生模型
class Student(BaseModel):
    id: int = Field(default=None, alias='_id')
    name: str
    age: int
    grade: GradeEnum

# 初始化数据库和表
db = TinyDB('db.json')
StudentTable = db.table('Student')

# 插入学生记录
def insert_student(student_data: Student):
    if student_data.id is None:
        student_data.id = (max((s.get('id', 0) for s in StudentTable.all()), default=0)) + 1
    student_data_dict = student_data.dict(by_alias=True)
    student_data_dict['_id'] = student_data.id
    StudentTable.insert(student_data_dict)
    return student_data.id

# 获取单个学生记录
def get_student(student_id: int):
    StudentQuery = Query()
    result = StudentTable.search(StudentQuery._id == student_id)
    return result[0] if result else None

# 获取所有学生记录
def get_all_students():
    return StudentTable.all()

# 更新学生记录
def update_student(student_id: int, student_data: Student):
    StudentQuery = Query()
    StudentTable.update(student_data.dict(by_alias=True), StudentQuery._id == student_id)

# 删除学生记录
def delete_student(student_id: int):
    StudentQuery = Query()
    StudentTable.remove(StudentQuery._id == student_id)

# 创建 FastAPI 应用
app = FastAPI()

# 创建学生记录
@app.post("/students/", response_model=Student)
def create_student(student: Student):
    student_id = insert_student(student)
    return get_student(student_id)

# 获取单个学生记录
@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    student = get_student(student_id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

# 获取所有学生记录
@app.get("/students/", response_model=list[Student])
def read_all_students():
    return get_all_students()

# 更新学生记录
@app.put("/students/{student_id}", response_model=Student)
def update_student_endpoint(student_id: int, student: Student):
    update_student(student_id, student)
    return get_student(student_id)

# 删除学生记录
@app.delete("/students/{student_id}")
def delete_student_endpoint(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted successfully"}

# 运行应用
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
