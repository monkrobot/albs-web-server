import typing

from pydantic import BaseModel


class RequestSignTask(BaseModel):

    build_id: int
    pgp_keyids: typing.List[str]


#class RequestBuild(BaseModel):
#
#    status: str
