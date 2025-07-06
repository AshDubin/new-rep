from fastapi import APIRouter, HTTPException
from ..tasks import location_lookup_task
from ..celery_app import celery_app

router = APIRouter(prefix="/api/location", tags=["location"])


@router.get("/trail")
async def trail(handle: str):
    task = location_lookup_task.delay(handle)
    return {"task_id": task.id}


@router.get("/task/{task_id}")
async def task_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    if result.failed():
        raise HTTPException(status_code=500, detail="Task failed")
    if not result.ready():
        return {"status": result.status}
    return {"status": result.status, "result": result.result}
