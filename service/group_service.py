import logging
import grpc

from group_pb2_grpc import GroupServiceStub

from schemas.request import group_request as requests
from schemas.response import group_response as response
from utils.group import (
    add_student,
    add_word_to_user,
    create_group,
    delete_group,
    find_group,
    find_student,
    find_teacher,
    find_groups_teacher,
    find_groups_student,
    get_statistics,
    remove_student,
)

from config.config import GROUP_SERVICE


class GroupService:
    def __init__(self):
        self.group_service_address = GROUP_SERVICE

    def connect_to_group_service(self):
        try:
            return grpc.insecure_channel(self.group_service_address)
        except Exception as e:
            logging.error(f"Failed to connect to group service: {e}")
            raise Exception("Failed to connect to group service") from e

    def add_student(self, add_student_request: requests.AddStudentRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                add_student(client, add_student_request)
            except Exception as e:
                logging.error(f"Add student failed: {e}")
                raise Exception("Cannot add student") from e

    def add_word_to_user(self, add_word_to_user_request: requests.AddWordToUserRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                res = add_word_to_user(client, add_word_to_user_request)
                return response.AddWordToUserResponse(word_id=res.word_id)
            except Exception as e:
                logging.error(f"Add word to user failed: {e}")
                raise Exception("Cannot add word to user") from e

    def create_group(self, create_group_request: requests.CreateGroupRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                create_group(client, create_group_request)
            except Exception as e:
                logging.error(f"Create group failed: {e}")
                raise Exception("Cannot create group") from e

    def delete_group(self, delete_group_request: requests.DeleteGroupRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                delete_group(client, delete_group_request)
            except Exception as e:
                logging.error(f"Delete group failed: {e}")
                raise Exception("Cannot delete group") from e

    def find_group(self, find_group_request: requests.FindGroupRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                group = find_group(client, find_group_request)
                return response.GroupResponse(
                    user_id=group.user_id,
                    group_id=group.group_id,
                    title=group.title,
                    students=group.students
                )
            except Exception as e:
                logging.error(f"Find group failed: {e}")
                raise Exception("Cannot find group") from e

    def find_student(self, find_student_request: requests.FindStudentRequest) -> response.StudentResponse:
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                student = find_student(client, find_student_request)
                return response.StudentResponse(
                    username=student.username,
                    email=student.email
                )
            except Exception as e:
                logging.error(f"Find student failed: {e}")
                raise Exception("Cannot find student") from e

    def find_teacher(self, find_teacher_request: requests.FindTeacherRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                teacher = find_teacher(client, find_teacher_request)
                return response.TeacherResponse(
                    teacher_id=teacher.teacher_id,
                    email=teacher.email,
                    username=teacher.username
                )
            except Exception as e:
                logging.error(f"Find teacher failed: {e}")
                raise Exception("Cannot find teacher") from e

    def find_groups_teacher(
        self, find_groups_teacher_request: requests.FindGroupsTeacherRequest
    ):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                groups: list[response.GroupResponse] = []
                resp = find_groups_teacher(client, find_groups_teacher_request)
                for group in resp:
                    groups.append(
                        response.GroupResponse(
                            user_id=group.user_id,
                            group_id=group.group_id,
                            title=group.title,
                            students=group.students
                        )
                    )
                return groups
            except Exception as e:
                logging.error(f"Find groups teacher failed: {e}")
                raise Exception("Cannot find groups teacher") from e

    def find_groups_student(
        self, find_groups_student_request: requests.FindGroupsStudentRequest
    ):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                groups: list[response.GroupResponse] = []
                resp = find_groups_student(client, find_groups_student_request)
                for group in resp:
                    groups.append(
                        response.GroupResponse(
                            user_id=group.user_id,
                            group_id=group.group_id,
                            title=group.title,
                            students=group.students
                        )
                    )
                return groups
            except Exception as e:
                logging.error(f"Find groups student failed: {e}")
                raise Exception("Cannot find groups student") from e

    def get_statistics(self, get_statistics_request: requests.GetStatisticsRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                stat = get_statistics(client, get_statistics_request)
                return response.StatisticsResponse(
                    statistics_id=stat.stat_id,
                    group_id=stat.group_id,
                    teacher_id=stat.teacher_id,
                    student_id=stat.student_id,
                    words=stat.words
                )
            except Exception as e:
                logging.error(f"Get statistics failed: {e}")
                raise Exception("Cannot get statistics") from e

    def remove_student(self, remove_student_request: requests.RemoveStudentRequest):
        with self.connect_to_group_service() as channel:
            client = GroupServiceStub(channel)
            try:
                remove_student(client, remove_student_request)
            except Exception as e:
                logging.error(f"Remove student failed: {e}")
                raise Exception("Cannot remove student") from e
