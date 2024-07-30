import logging
from fastapi import APIRouter, Request, status
from fastapi.exceptions import HTTPException

from schemas.request.vocab_request import (
    CreateWordRequest,
    DeleteWordRequest,
    FindWordRequest,
    VocabRequest,
    UpdateWordRequest,
    UpdateWordStatusRequest,
    ManageTrainingsRequest,
)
from service.vocab_service import VocabService
from schemas.response.web_response import Response

from utils.time import datetime_to_timestamp
from utils.token import get_token

router = APIRouter(
    prefix="/vocab",
    tags=["Vocab"],
)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_word(request: Request, create_word_request: CreateWordRequest):
    token = get_token(request=request)
    create_word_request.token = token
    try:
        VocabService().create_word(create_word_request)
        return Response(
            code=201, status="Created", message="Successfully created word!"
        )
    except Exception as e:
        logging.error(f"Create word failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot create word")


@router.delete("/{word_id}", status_code=status.HTTP_200_OK)
def delete_word(request: Request, word_id: int):
    token = get_token(request=request)
    try:
        VocabService().delete_word(DeleteWordRequest(token=token, word_id=word_id))
        return Response(code=200, status="Ok", message="Successfully deleted word!")
    except Exception as e:
        logging.error(f"Delete word failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot delete word")


@router.get("", status_code=status.HTTP_200_OK)
def get_words(request: Request):
    token = get_token(request=request)

    vocab_request = VocabRequest(token_type="Bearer", token=token)
    try:
        words = VocabService().get_words(vocab_request)
        res: list[dict] = []
        for word in words:
            result = word.model_dump()
            result['created_at'] = datetime_to_timestamp(word.created_at)
            res.append(result)
        return Response(
            code=200, status="Ok", message="Successfully got words!", data=res
        )
    except Exception as e:
        logging.error(f"Get words failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot get words")


@router.patch("/{word_id}", status_code=status.HTTP_200_OK)
def update_word(request: Request, word_id: int, update_word_request: UpdateWordRequest):
    token = get_token(request=request)
    update_word_request.token = token
    update_word_request.word_id = word_id
    try:
        VocabService().update_word(update_word_request)
        return Response(code=200, status="Ok", message="Successfully updated word!")
    except Exception as e:
        logging.error(f"Update word failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot update word")


@router.patch("/{word_id}/status", status_code=status.HTTP_200_OK)
def update_word_status(
    request: Request, word_id: int, update_word_status_request: UpdateWordStatusRequest
):
    token = get_token(request=request)
    update_word_status_request.token = token

    update_word_status_request.word_id = word_id
    try:
        VocabService().update_word_status(update_word_status_request)
        return Response(
            code=200, status="Ok", message="Successfully updated word status!"
        )
    except Exception as e:
        logging.error(f"Update word status failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot update word status")


@router.patch("/{word_id}/trainings", status_code=status.HTTP_200_OK)
def manage_trainings(
    request: Request, word_id: int, manage_trainings_request: ManageTrainingsRequest
):
    token = get_token(request=request)
    manage_trainings_request.token = token
    manage_trainings_request.word_id = word_id
    try:
        VocabService().manage_trainings(manage_trainings_request)
        return Response(
            code=200, status="Ok", message="Successfully managed trainings!"
        )
    except Exception as e:
        logging.error(f"Manage trainings failed: {e}")
        raise HTTPException(status_code=500, detail="Cannot manage trainings")


@router.get("/{word_id}", status_code=status.HTTP_200_OK)
def find_word(request: Request, word_id: int):
    find_word_request = FindWordRequest(word_id=word_id)
    try:
        word = VocabService().find_word(find_word_request)
        res = word.model_dump()
        res['created_at'] = datetime_to_timestamp(word.created_at)

        if not word:
            raise HTTPException(
                status_code=404,
                detail=f"Word with id {find_word_request.word_id} not found",
            )
        return Response(
            code=200, status="Ok", message="Successfully found word!", data=res
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve word: {e}")
