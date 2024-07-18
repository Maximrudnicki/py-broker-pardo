import grpc
import logging

from group_pb2_grpc import GroupServiceStub
from group_pb2 import (
    AddStudentRequest,
    AddWordToUserRequest,
    AddWordToUserResponse,
    CreateGroupRequest,
    DeleteGroupRequest,
    FindGroupRequest,
    FindGroupsTeacherRequest,
    FindGroupsStudentRequest,
    GroupResponse,
    FindStudentRequest,
    StudentResponse,
    FindTeacherRequest,
    TeacherResponse,
    GetStatisticsRequest,
    StatisticsResponse,
    RemoveStudentRequest,
)

from schemas.request import group_request as requests


def add_student(client: GroupServiceStub, request: requests.AddStudentRequest) -> None:
    req = AddStudentRequest(token=request.token, group_id=request.group_id)
    try:
        client.AddStudent(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while joining the group: {e}")
        raise Exception("Error happened while joining the group") from e


def add_word_to_user(
    client: GroupServiceStub, request: requests.AddWordToUserRequest
) -> AddWordToUserResponse:
    req = AddWordToUserRequest(
        token=request.token,
        word=request.word,
        definition=request.definition,
        group_id=request.group_id,
        user_id=request.user_id,
    )

    try:
        res = client.AddWordToUser(req)
        return res
    except grpc.RpcError as e:
        logging.error(f"Error happened while adding the word to user: {e}")
        raise Exception("Error happened while adding the word to user") from e


def create_group(
    client: GroupServiceStub, request: requests.CreateGroupRequest
) -> None:
    req = CreateGroupRequest(token=request.token, title=request.title)
    try:
        client.CreateGroup(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while creating group: {e}")
        raise Exception("Error happened while creating group") from e


def delete_group(
    client: GroupServiceStub, request: requests.DeleteGroupRequest
) -> None:
    req = DeleteGroupRequest(token=request.token, group_id=request.group_id)
    try:
        client.DeleteGroup(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while deleting group: {e}")
        raise Exception("Error happened while deleting group") from e


def find_group(
    client: GroupServiceStub, request: requests.FindGroupRequest
) -> GroupResponse:
    req = FindGroupRequest(token=request.token, group_id=request.group_id)

    try:
        res = client.FindGroup(req)
        return res
    except grpc.RpcError as e:
        logging.error(f"Error happened while finding group: {e}")
        raise Exception("Error happened while finding group") from e


def find_student(
    client: GroupServiceStub, request: requests.FindStudentRequest
) -> StudentResponse:
    req = FindStudentRequest(
        token=request.token, student_id=request.student_id, group_id=request.group_id
    )

    try:
        res = client.FindStudent(req)
        return res
    except grpc.RpcError as e:
        logging.error(f"Error happened while finding student: {e}")
        raise Exception("Error happened while finding student") from e


def find_teacher(
    client: GroupServiceStub, request: requests.FindTeacherRequest
) -> TeacherResponse:
    req = FindTeacherRequest(token=request.token, group_id=request.group_id)

    try:
        res = client.FindTeacher(req)
        return res
    except grpc.RpcError as e:
        logging.error(f"Error happened while finding teacher: {e}")
        raise Exception("Error happened while finding teacher") from e


def find_groups_teacher(
    client: GroupServiceStub, request: requests.FindGroupsTeacherRequest
) -> list[GroupResponse]:
    req = FindGroupsTeacherRequest(token=request.token)
    group_list = []
    try:
        stream = client.FindGroupsTeacher(req)
        for res in stream:
            group_list.append(res)
        return group_list
    except grpc.RpcError as e:
        logging.error(f"Error happened while finding groups: {e}")
        raise Exception("Error happened while finding groups") from e


def find_groups_student(
    client: GroupServiceStub, request: requests.FindGroupsStudentRequest
) -> list[GroupResponse]:
    req = FindGroupsStudentRequest(token=request.token)
    group_list = []
    try:
        stream = client.FindGroupsStudent(req)
        for res in stream:
            group_list.append(res)
        return group_list
    except grpc.RpcError as e:
        logging.error(f"Error happened while finding groups: {e}")
        raise Exception("Error happened while finding groups") from e


def get_statistics(
    client: GroupServiceStub, request: requests.GetStatisticsRequest
) -> StatisticsResponse:
    req = GetStatisticsRequest(
        student_id=request.student_id, group_id=request.group_id, token=request.token
    )

    try:
        res = client.GetStatistics(req)
        return res
    except grpc.RpcError as e:
        logging.error(f"Error happened while getting statistics: {e}")
        raise Exception("Error happened while getting statistics") from e


def remove_student(
    client: GroupServiceStub, request: requests.RemoveStudentRequest
) -> None:
    req = RemoveStudentRequest(
        token=request.token, group_id=request.group_id, user_id=request.user_id
    )
    try:
        client.RemoveStudent(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while removing student from the group: {e}")
        raise Exception("Error happened while removing student from the group") from e
