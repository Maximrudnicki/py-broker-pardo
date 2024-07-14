from pydantic import BaseModel


class CreateWordRequest(BaseModel):
    token: str
    word: str
    definition: str

    class Config:
        from_attributes = True


class DeleteWordRequest(BaseModel):
    token: str
    word_id: int

    class Config:
        from_attributes = True


class FindWordRequest(BaseModel):
    word_id: int

    class Config:
        from_attributes = True


class VocabRequest(BaseModel):
    token_type: str  # Bearer
    token: str

    class Config:
        from_attributes = True


class UpdateWordRequest(BaseModel):
    token: str
    word_id: int
    definition: str

    class Config:
        from_attributes = True


class UpdateWordStatusRequest(BaseModel):
    token: str
    word_id: int
    is_learned: bool

    class Config:
        from_attributes = True


class ManageTrainingsRequest(BaseModel):
    token: str
    training_result: bool
    training: str
    word_id: int
