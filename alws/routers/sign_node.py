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
    response = await crud.create_sign_task(db, request)
    return response
    

@router.get('/get_sign_task')
async def get_sign_task(
            db: database.Session = Depends(get_db)
        ):
    task = await crud.get_available_sign_task(db)
    if not task:
        return
    response = {
        'task_id': task.id
    }
    return response


@router.get('/sign_done')
async def sign_done(
            request: sign_node_schema.SignDone,
            db: database.Session = Depends(get_db)
        ):
    return await crud.sign_done(db)
