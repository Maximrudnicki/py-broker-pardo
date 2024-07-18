import logging
from fastapi import APIRouter, HTTPException, Request

from schemas.request.group_request import (
    AddStudentRequest,
    AddWordToUserRequest,
    CreateGroupRequest,
    DeleteGroupRequest,
    FindGroupRequest,
    FindGroupsStudentRequest,
    FindGroupsTeacherRequest,
    FindStudentRequest,
    FindTeacherRequest,
    GetStatisticsRequest,
    RemoveStudentRequest,
)
from schemas.request.vocab_request import FindWordRequest
from schemas.response.group_response import StudentInformation
from schemas.response.vocab_response import VocabResponse
from service.group_service import GroupService
from schemas.response.web_response import Response
from service.vocab_service import VocabService
from utils.token import get_token

router = APIRouter(
    prefix="/group",
    tags=["Group"],
)


@router.post("/add")
def add_student(request: Request, add_student_request: AddStudentRequest):
    token = get_token(request=request)
    add_student_request.token = token
    try:
        GroupService().add_student(add_student_request)
        return Response(code=200, status="Ok", message="Successfully added student!")
    except Exception as e:
        logging.error(f"Add student failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot add student")


@router.post("/add_word")
def add_word_to_user(request: Request, add_word_to_user_request: AddWordToUserRequest):
    token = get_token(request=request)
    add_word_to_user_request.token = token

    try:
        res = GroupService().add_word_to_user(add_word_to_user_request)
        return Response(
            code=200, status="Created", message="Successfully created group!", data=res
        )
    except Exception as e:
        logging.error(f"Create group failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot create group")


@router.post("")
def create_group(request: Request, create_group_request: CreateGroupRequest):
    token = get_token(request=request)
    create_group_request.token = token
    try:
        GroupService().create_group(create_group_request)
        return Response(
            code=201, status="Created", message="Successfully created group!"
        )
    except Exception as e:
        logging.error(f"Create group failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot create group")


@router.delete("/{groupId}")
def delete_group(request: Request, delete_group_request: DeleteGroupRequest):
    token = get_token(request=request)
    delete_group_request.token = token
    try:
        GroupService().delete_group(delete_group_request)
        return Response(
            code=200, status="Deleted", message="Successfully deleted group!"
        )
    except Exception as e:
        logging.error(f"Delete group failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot delete group")


@router.post("/find")
def find_group(request: Request, find_group_request: FindGroupRequest):
    token = get_token(request=request)
    find_group_request.token = token
    try:
        group = GroupService().find_group(find_group_request)

        students = []
        for student_id in group.students:
            stat = GroupService().get_statistics(
                GetStatisticsRequest(
                    token=token,
                    student_id=student_id,
                    group_id=find_group_request.group_id,
                )
            )

            words = []
            for word_id in stat.words:
                find_word_request = FindWordRequest(word_id=word_id)
                try:
                    word = VocabService().find_word(find_word_request)
                    words.append(word)
                except:
                    continue

            student = GroupService().find_student(
                FindStudentRequest(
                    token=token,
                    group_id=find_group_request.group_id,
                    student_id=student_id,
                )
            )
            student_info = StudentInformation(
                student_id=student_id,
                email=student.email,
                username=student.username,
                words=words,
            )
            students.append(student_info)

        res = {
            "user_id": group.user_id,
            "group_id": group.group_id,
            "title": group.title,
            "students": students,
        }

        return Response(
            code=200, status="Ok", message="Successfully found group!", data=res
        )
    except Exception as e:
        logging.error(f"Find group failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot find group")


@router.get("/find_student")
def find_groups_student(request: Request):
    token = get_token(request=request)
    find_groups_student_request = FindGroupsStudentRequest(token=token)
    try:
        groups = GroupService().find_groups_student(find_groups_student_request)
        return Response(
            code=200, status="Ok", message="Successfully got groups!", data=groups
        )
    except Exception as e:
        logging.error(f"Find student's groups failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot find student's groups")


@router.get("/find_teacher")
def find_groups_teacher(request: Request):
    token = get_token(request=request)
    find_groups_teacher_request = FindGroupsTeacherRequest(token=token)
    try:
        groups = GroupService().find_groups_teacher(find_groups_teacher_request)
        return Response(
            code=200, status="Ok", message="Successfully got groups!", data=groups
        )
    except Exception as e:
        logging.error(f"Find teacher's groups failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot find teacher's groups")


@router.post("/find_teacher_info")
def find_teacher(request: Request, find_teacher_request: FindTeacherRequest):
    token = get_token(request=request)
    find_teacher_request.token = token
    try:
        teacher = GroupService().find_teacher(find_teacher_request)
        return Response(
            code=200, status="Ok", message="Successfully got groups!", data=teacher
        )
    except Exception as e:
        logging.error(f"Find teacher's groups failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot find teacher's groups")


@router.post("/find_student_info")
def find_student(request: Request, find_student_request: FindStudentRequest):
    token = get_token(request=request)
    find_student_request.token = token
    try:
        student = GroupService().find_student(find_student_request)
        return Response(
            code=200, status="Ok", message="Successfully found student!", data=student
        )
    except Exception as e:
        logging.error(f"Find student failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot find student")


@router.post("/get_statistics")
def get_statistics(request: Request, get_statistics_request: GetStatisticsRequest):
    token = get_token(request=request)
    get_statistics_request.token = token
    try:
        stat = GroupService().get_statistics(get_statistics_request)

        words = []
        for word_id in stat.words:
            find_word_request = FindWordRequest(word_id=word_id)
            try:
                word = VocabService().find_word(find_word_request)
                words.append(word)
            except:
                continue

        student = GroupService().find_student(
            FindStudentRequest(
                token=token, student_id=stat.student_id, group_id=stat.group_id
            )
        )

        res = {
            "statistics_id": stat.statistics_id,
            "group_id": stat.group_id,
            "teacher_id": stat.teacher_id,
            "student": student,
            "words": words,
        }

        return Response(
            code=200, status="Ok", message="Successfully got statistics!", data=res
        )
    except Exception as e:
        logging.error(f"Get statistics failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot get statistics")


@router.patch("/remove")
def remove_student(request: Request, remove_student_request: RemoveStudentRequest):
    token = get_token(request=request)
    remove_student_request.token = token
    try:
        GroupService().remove_student(remove_student_request)
        return Response(
            code=200, status="Removed", message="Successfully removed student!"
        )
    except Exception as e:
        logging.error(f"Remove student failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot remove student")
