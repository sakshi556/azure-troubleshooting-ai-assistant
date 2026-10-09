from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import logging

from fastapi import FastAPI, Request, HTTPException

from ai import ask_ai

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


class Question(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze")
def analyze(data: Question):

    try:
        logger.info("Received troubleshooting request")

        if not data.question.strip():
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty."
            )

        answer = ask_ai(data.question)

        logger.info("Troubleshooting request completed")

        return {
            "answer": answer
        }

    except HTTPException:
        raise

    except Exception:
        logger.exception("Failed to process troubleshooting request")

        raise HTTPException(
            status_code=500,
            detail="Unable to process the request."
        )