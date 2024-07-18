from typing import Optional
from pydantic import BaseModel


class CreateWordRequest(BaseModel):
    token: Optional[str] = None
    word: str
    definition: str

    class Config:
        from_attributes = True


class DeleteWordRequest(BaseModel):
    token: Optional[str] = None
    word_id: int

    class Config:
        from_attributes = True


class FindWordRequest(BaseModel):
    word_id: int

    class Config:
        from_attributes = True


class VocabRequest(BaseModel):
    token_type: str  # Bearer
    token: Optional[str] = None

    class Config:
        from_attributes = True


class UpdateWordRequest(BaseModel):
    token: Optional[str] = None
    word_id: int
    definition: str

    class Config:
        from_attributes = True


class UpdateWordStatusRequest(BaseModel):
    token: Optional[str] = None
    word_id: int
    is_learned: bool

    class Config:
        from_attributes = True


class ManageTrainingsRequest(BaseModel):
    token: Optional[str] = None
    result: bool
    training: str
    word_id: Optional[int] = None
