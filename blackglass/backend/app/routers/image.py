from fastapi import APIRouter, HTTPException
from ..tasks import image_analysis_task
from ..celery_app import celery_app

router = APIRouter(prefix="/api/image", tags=["image"])


@router.get("/analysis")
async def analyze(url: str):
    task = image_analysis_task.delay(url)
    return {"task_id": task.id}


@router.get("/task/{task_id}")
async def task_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    if result.failed():
        raise HTTPException(status_code=500, detail="Task failed")
    if not result.ready():
        return {"status": result.status}
    return {"status": result.status, "result": result.result}
