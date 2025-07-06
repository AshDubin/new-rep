from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import identity, vehicle, image, location, breach

app = FastAPI(title="BlackGlass OSINT API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(identity.router)
app.include_router(vehicle.router)
app.include_router(image.router)
app.include_router(location.router)
app.include_router(breach.router)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}
