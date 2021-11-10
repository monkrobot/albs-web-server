import typing

from pydantic import BaseModel


class RequestSignTask(BaseModel):

    build_id: int
    pgp_keyid: str
    result: dict


class SignDone(BaseModel):

    task_id: int
    status: typing.Literal['done', 'failed', 'excluded']


# class SignTaskResult(BaseModel):
#     api_version: str
#     result: dict
