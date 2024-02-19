from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run
from models import SentimentModel

from mangum import Mangum
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

import os

load_dotenv()
root_path = os.getenv('ENV', default='')

app = FastAPI(root_path=f'/{root_path}')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

sentiment_model = SentimentModel()
sentiment_model.load_model()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/home", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "search.html", {"request": request}
    )

def get_analysis(input_sentence: str):
    classification = sentiment_model.model(input_sentence)
    results = {cl["label"]:cl["score"] for cl in classification}
    return results

@app.post("/analysis", response_class=HTMLResponse)
def analysis(request: Request, input_sentence: str = Form(...)):
    results = get_analysis(input_sentence)
    return templates.TemplateResponse("results.html", 
                                      {"request": request, "input_sentence": input_sentence, "results": results})

@app.get("/about")
def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# The magic that allows the integration with AWS Lambda
handler = Mangum(app)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)