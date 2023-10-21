from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from data_structure.stack import Stack

router = APIRouter()

stack = Stack()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "stack": stack})

@router.post("/push")
async def push_item(request: Request):
    form_data = await request.form()
    item = int(form_data["item"])
    stack.push(item)
    return RedirectResponse("/stack", status_code=303)  # Redirect to the root page


@router.get("/pop")
async def pop_item():
    try:
        if stack:
            item = stack.pop()
            return RedirectResponse("/stack", status_code=303)
    except IndexError:
        message = "Stack is empty"
        return RedirectResponse("/stack", status_code=303)