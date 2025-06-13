from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

from src.models.timestamp import TimestampMixin

class TrashBase(SQLModel):
    id: Optional[int]               = Field(default=None, primary_key=True)
    label: str                      = Field(index=True)
    yolov5_label: Optional[str]     = Field(default=None, index=True)
    yolov5_score: Optional[float]   = Field(default=None, index=True)
    resnet_label: Optional[str]     = Field(default=None, index=True)
    resnet_score: Optional[float]   = Field(default=None, index=True)

class Trash(TrashBase, TimestampMixin, table=True):
    def __repr__(self):
        return f'<Trash(id={self.id}, label="{self.label}")>'

class TrashCreate(TrashBase):
    pass

class TrashRead(SQLModel):
    id:     int
    label:  str