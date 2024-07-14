from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class VocabResponse(BaseModel):
    id: int
    word: str
    definition: str
    created_at: Optional[datetime]
    is_learned: bool
    cards: bool
    word_translation: bool
    constructor: bool
    word_audio: bool

    class Config:
        from_attributes = True
