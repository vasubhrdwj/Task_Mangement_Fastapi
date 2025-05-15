from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Bro"}

@app.get("/sqlalchemy_test")
def test_pos(db : Session = Depends(get_db)):
    return {"status_db" : "Connected"}

