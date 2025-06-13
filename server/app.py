from fastapi import FastAPI, Depends, UploadFile

from src.models.base import connect_db
from src.models.trash import TrashRead
from src.services.trash import TrashService
from src.classifiers.classify import classify

app = FastAPI()

def get_trash_service(db=Depends(connect_db)):
    return TrashService(db)

@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}

@app.post('/trash', tags=['Trash'], response_model=TrashRead)
def create_trash(image: UploadFile, service=Depends(get_trash_service)):
    return service.create(classify(image))