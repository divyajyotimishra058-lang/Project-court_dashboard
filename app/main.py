from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/query", response_class=HTMLResponse)
async def run_query(request: Request, case_type: str = Form(...), case_number: str = Form(...), filing_year: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "result": "Coming soon!"})
