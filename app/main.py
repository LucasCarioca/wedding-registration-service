from fastapi import FastAPI, Request
from .routers.registrations import router as registration_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(registration_router, prefix="/api/v1/registrations")

origins = [
    "http://localhost:3000",
    "https://lucasandkaren.com",
    "https://karenandlucas.com",
    "https://wedding.ldkube.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
