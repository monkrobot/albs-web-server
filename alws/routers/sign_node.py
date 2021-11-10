from sqlalchemy.util.langhelpers import dependencies
from fastapi import APIRouter, Depends

from alws import crud, database
from alws.dependencies import get_db, JWTBearer
from alws.schemas import sign_node_schema


router = APIRouter(
    prefix='/sign_node',
    dependencies=[Depends(JWTBearer())]
)


@router.get('/create_sign_task')
async def create_sign_task(
            request: sign_node_schema.RequestSignTask,
            db: database.Session = Depends(get_db)
        ):
    msg = await crud.create_sign_task(db, request)
    response = {
        'msg': msg
    }

@router.get('/get_task')
async def get_build(
            db: database.Session = Depends(get_db)
        ):
    task = await crud.get_available_build(db)
    if not task:
        return
    response = {
        'task_id': task.id
    }
    return response
