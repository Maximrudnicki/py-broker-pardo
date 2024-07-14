from fastapi import APIRouter

from service.group_service import GroupService

from utils.token import get_token

router = APIRouter(
    prefix="/group",
    tags=["Group"],
)


@router.post("/add")
def add_student():
    GroupService().add_student()
    pass


@router.post("/add_word")
def add_word_to_user():
    GroupService().add_word_to_user()
    pass


@router.post("")
def create_group():
    GroupService().create_group()
    pass


@router.delete("/{groupId}")
def delete_group():
    GroupService().delete_group()
    pass


@router.post("/find")
def find_group():
    GroupService().find_group()
    pass


@router.post("/find_student")
def find_student():
    GroupService().find_student()
    pass


@router.post("/find_teacher")
def find_teacher():
    GroupService().find_teacher()
    pass


@router.get("/find_teacher_info")
def find_groups_teacher():
    GroupService().find_groups_teacher()
    pass


@router.get("/find_student_info")
def find_groups_student():
    GroupService().find_groups_student()
    pass


@router.get("/get_statistics")
def get_statistics():
    GroupService().get_statistics()
    pass


@router.patch("/remove")
def remove_student():
    GroupService().remove_student()
    pass
