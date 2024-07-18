from typing import Optional
from pydantic import BaseModel


class AddStudentRequest(BaseModel):
    token: Optional[str] = None
    group_id: str
    

class AddWordToUserRequest(BaseModel):
    token: Optional[str] = None
    word: str
    definition: str
    group_id: str
    user_id: int
    

class CreateGroupRequest(BaseModel):
    token: Optional[str] = None
    title: str
    

class DeleteGroupRequest(BaseModel):
    token: Optional[str] = None
    group_id: str
    

class FindGroupRequest(BaseModel):
    token: Optional[str] = None
    group_id: str
    

class FindStudentRequest(BaseModel):
    token: Optional[str] = None
    group_id: str
    student_id: int
    

class FindTeacherRequest(BaseModel):
    token: Optional[str] = None
    group_id: str
    

class FindGroupsTeacherRequest(BaseModel):
    token: Optional[str] = None
    

class FindGroupsStudentRequest(BaseModel):
    token: Optional[str] = None
    

class GetStatisticsRequest(BaseModel):
    token: Optional[str] = None
    group_id: str
    student_id: int
    

class RemoveStudentRequest(BaseModel):
    token: Optional[str] = None
    group_id: str
    user_id: int
    
