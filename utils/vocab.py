import grpc
import logging

from vocab_pb2_grpc import VocabServiceStub
from vocab_pb2 import (
    VocabRequest,
    VocabResponse,
    CreateRequest,
    WordRequest,
    DeleteRequest,
    UpdateRequest,
    UpdateStatusRequest,
    ManageTrainingsRequest,
)

from schemas.request import vocab_request as requests


def create_word(client: VocabServiceStub, request: requests.CreateWordRequest) -> None:
    req = CreateRequest(
        word=request.word, definition=request.definition, token=request.token
    )
    try:
        client.CreateWord(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while creating word: {e}")
        raise Exception("Error happened while creating word") from e


def get_words(
    client: VocabServiceStub, request: requests.VocabRequest
) -> list[VocabResponse]:
    vocab_list = []

    req = VocabRequest(tokenType="Bearer", token=request.token)

    try:
        stream = client.GetWords(req)
        for res in stream:
            vocab_list.append(res)
    except grpc.RpcError as e:
        logging.error(f"Error happened while getting words: {e}")
        raise Exception("Error happened while getting words") from e
    return vocab_list


def delete_word(client: VocabServiceStub, request: requests.DeleteWordRequest) -> None:
    req = DeleteRequest(word_id=request.word_id, token=request.token)
    try:
        client.DeleteWord(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while deleting word: {e}")
        raise Exception("Error happened while deleting word") from e


def find_word(
    client: VocabServiceStub, request: requests.FindWordRequest
) -> VocabResponse:
    req = WordRequest(word_id=request.word_id)

    try:
        res = client.FindWord(req)
        return res
    except grpc.RpcError as e:
        logging.error(f"Error happened while finding word: {e}")
        raise Exception("Error happened while finding word") from e


def update_word(client: VocabServiceStub, request: requests.UpdateWordRequest) -> None:
    req = UpdateRequest(
        id=request.word_id, token=request.token, definition=request.definition
    )
    try:
        client.UpdateWord(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while updating word: {e}")
        raise Exception("Error happened while updating word") from e


def update_word_status(
    client: VocabServiceStub, request: requests.UpdateWordStatusRequest
) -> None:
    req = UpdateStatusRequest(
        id=request.word_id, token=request.token, is_learned=request.is_learned
    )
    try:
        client.UpdateWordStatus(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while updating status of the word: {e}")
        raise Exception("Error happened while updating status of the word") from e


def manage_trainings(
    client: VocabServiceStub, request: requests.ManageTrainingsRequest
) -> None:
    req = ManageTrainingsRequest(
        id=request.word_id,
        res=request.result,
        training=request.training,
        token=request.token,
    )
    try:
        client.ManageTrainings(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while managing trainings: {e}")
        raise Exception("Error happened while managing trainings") from e
