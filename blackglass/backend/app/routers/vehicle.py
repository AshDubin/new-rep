from fastapi import APIRouter, HTTPException
from ..tasks import vehicle_lookup_task
from ..celery_app import celery_app

router = APIRouter(prefix="/api/vehicle", tags=["vehicle"])


@router.get("/{plate}")
async def vehicle_lookup(plate: str):
    task = vehicle_lookup_task.delay(plate)
    return {"task_id": task.id}


@router.get("/task/{task_id}")
async def task_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    if result.failed():
        raise HTTPException(status_code=500, detail="Task failed")
    if not result.ready():
        return {"status": result.status}
    return {"status": result.status, "result": result.result}
