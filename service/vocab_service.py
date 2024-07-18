import logging
import grpc

from vocab_pb2_grpc import VocabServiceStub

from schemas.request import vocab_request as requests
from schemas.response import vocab_response as response
from utils.vocab import (
    create_word,
    delete_word,
    get_words,
    find_word,
    update_word,
    update_word_status,
    manage_trainings,
)
from utils.time import timestamp_to_datetime

from config.config import VOCAB_SERVICE


class VocabService:
    def __init__(self):
        self.vocab_service_address = VOCAB_SERVICE

    def connect_to_vocab_service(self):
        try:
            return grpc.insecure_channel(self.vocab_service_address)
        except Exception as e:
            logging.error(f"Failed to connect to vocab service: {e}")
            raise Exception("Failed to connect to vocab service") from e

    def create_word(self, create_word_request: requests.CreateWordRequest):
        with self.connect_to_vocab_service() as channel:
            client = VocabServiceStub(channel)
            try:
                create_word(client, create_word_request)
            except Exception as e:
                logging.error(f"Create word failed: {e}")
                raise Exception("Cannot create word") from e

    def delete_word(self, delete_word_request: requests.DeleteWordRequest):
        with self.connect_to_vocab_service() as channel:
            client = VocabServiceStub(channel)
            try:
                delete_word(client, delete_word_request)
            except Exception as e:
                logging.error(f"Create word failed: {e}")
                raise Exception("Cannot create word") from e

    def get_words(self, vocab_request: requests.VocabRequest):
        with self.connect_to_vocab_service() as channel:
            client = VocabServiceStub(channel)
            try:
                words: list[response.VocabResponse] = []
                resp = get_words(client, vocab_request)

                for word in resp:
                    words.append(
                        response.VocabResponse(
                            id=word.id,
                            word=word.word,
                            definition=word.definition,
                            created_at=timestamp_to_datetime(word.createdAt),
                            is_learned=word.isLearned,
                            cards=word.cards,
                            word_translation=word.wordTranslation,
                            constructor=word.constructor,
                            word_audio=word.wordAudio,
                        )
                    )

                return words
            except Exception as e:
                logging.error(f"Get words failed: {e}")
                raise Exception("Cannot get words") from e

    def find_word(self, find_word_request: requests.FindWordRequest):
        with self.connect_to_vocab_service() as channel:
            client = VocabServiceStub(channel)
            try:
                res = find_word(client, find_word_request)
                return response.VocabResponse(
                    id=res.id,
                    word=res.word,
                    definition=res.definition,
                    created_at=timestamp_to_datetime(res.createdAt),
                    is_learned=res.isLearned,
                    cards=res.cards,
                    word_translation=res.wordTranslation,
                    constructor=res.constructor,
                    word_audio=res.wordAudio,
                )
            except Exception as e:
                logging.error(f"Find word failed: {e}")
                raise Exception("Cannot find word") from e

    def update_word(self, update_word_request: requests.UpdateWordRequest):
        with self.connect_to_vocab_service() as channel:
            client = VocabServiceStub(channel)
            try:
                update_word(client, update_word_request)
            except Exception as e:
                logging.error(f"Update word failed: {e}")
                raise Exception("Cannot update word") from e

    def update_word_status(
        self, update_word_status_request: requests.UpdateWordStatusRequest
    ):
        with self.connect_to_vocab_service() as channel:
            client = VocabServiceStub(channel)
            try:
                update_word_status(client, update_word_status_request)
            except Exception as e:
                logging.error(f"Update word status failed: {e}")
                raise Exception("Cannot update word status") from e

    def manage_trainings(
        self, manage_trainings_request: requests.ManageTrainingsRequest
    ):
        with self.connect_to_vocab_service() as channel:
            client = VocabServiceStub(channel)
            try:
                manage_trainings(client, manage_trainings_request)
            except Exception as e:
                logging.error(f"Manage trainings failed: {e}")
                raise Exception("Cannot manage trainings") from e
