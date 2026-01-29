from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .api import router

app = FastAPI(title="Maya Calendar Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API eerst
app.include_router(router)

# --- robuust pad naar frontend ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

print("Frontend dir:", FRONTEND_DIR)

app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
