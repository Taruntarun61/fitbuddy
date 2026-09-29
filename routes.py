from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Home page
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Generate workout
@router.post("/generate-workout", response_class=HTMLResponse)
async def generate_workout(request: Request,
                           username: str = Form(...),
                           goal: str = Form(...),
                           intensity: str = Form(...)):

    # dummy output (later Gemini add pannalam)
    plan = f"Workout plan for {username} with goal {goal} and intensity {intensity}"

    return templates.TemplateResponse("result.html", {
        "request": request,
        "plan": plan
    })
