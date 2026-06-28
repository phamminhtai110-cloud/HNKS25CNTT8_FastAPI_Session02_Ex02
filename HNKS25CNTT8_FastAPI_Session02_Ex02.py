from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Bình"},
    {"id": 3, "name": "Chi"}
]

@app.get("/students")
def get_students():
    return students