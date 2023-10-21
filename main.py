# main.py
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from controllers.stack_controller import router as stack_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(stack_router, prefix="/stack")
