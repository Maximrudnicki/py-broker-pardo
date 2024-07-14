from pydantic import BaseModel


class AddStudentRequest(BaseModel):
    token: str
    group_id: str
    

class AddWordToUserRequest(BaseModel):
    token: str
    word: str
    definition: str
    group_id: str
    user_id: int
    

class CreateGroupRequest(BaseModel):
    token: str
    title: str
    

class DeleteGroupRequest(BaseModel):
    token: str
    group_id: str
    

class FindGroupRequest(BaseModel):
    token: str
    group_id: str
    

class FindStudentRequest(BaseModel):
    token: str
    group_id: str
    student_id: int
    

class FindTeacherRequest(BaseModel):
    token: str
    group_id: str
    

class FindGroupsTeacherRequest(BaseModel):
    token: str
    

class FindGroupsStudentRequest(BaseModel):
    token: str
    

class GetStatisticsRequest(BaseModel):
    token: str
    group_id: str
    student_id: int
    

class RemoveStudentRequest(BaseModel):
    token: str
    group_id: str
    user_id: int
    
