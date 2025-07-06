from fastapi import APIRouter, HTTPException
from ..tasks import (
    hibp_email_search,
    social_lookup_task,
)
from ..celery_app import celery_app

router = APIRouter(prefix="/api/identity", tags=["identity"])


@router.get("/search")
async def search_identity(q: str):
    """Start an identity search."""
    results = {}
    if "@" in q:
        task = hibp_email_search.delay(q)
        results["breaches_task"] = task.id
    task = social_lookup_task.delay(q)
    results["social_task"] = task.id
    return {"query": q, **results}


@router.get("/task/{task_id}")
async def task_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    if result.failed():
        raise HTTPException(status_code=500, detail="Task failed")
    if not result.ready():
        return {"status": result.status}
    return {"status": result.status, "result": result.result}
