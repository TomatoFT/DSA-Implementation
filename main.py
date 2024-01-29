# main.py
from controllers.stack_controller import router as stack_router
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(stack_router, prefix="/stack")
