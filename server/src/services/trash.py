from sqlmodel import Session

from ..models.trash import Trash, TrashCreate

class TrashService:
    def __init__(self, session: Session, model=Trash):
        self.session    = session
        self.model      = model

    def create(self, req: TrashCreate):
        trash = self.model.model_validate(req)
        self.session.add(trash)
        self.session.commit()
        self.session.refresh(trash)
        return trash