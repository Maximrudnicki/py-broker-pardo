from pydantic import BaseModel, EmailStr
from typing import List
from vocab_response import VocabResponse


class GroupResponse(BaseModel):
    user_id: int
    group_id: str
    title: str
    students: List[int]


class StudentResponse(BaseModel):
    email: EmailStr
    username: str


class TeacherResponse(BaseModel):
    teacher_id: int
    email: EmailStr
    username: str


class StatisticsResponse(BaseModel):
    statistics_id: str
    group_id: str
    teacher_id: int
    student_id: int
    words: List[int]


class AddWordToUserResponse(BaseModel):
    word_id: int


class StudentInfo(BaseModel):
    student_id: int
    email: EmailStr
    username: str


class StudentInformation(BaseModel):
    student_id: int
    email: EmailStr
    username: str
    words: List[VocabResponse]
