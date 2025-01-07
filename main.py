from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 일원터널
@app.get("/location/irwon-tunnel", response_class=HTMLResponse)
async def get_overlay(request: Request):
    return templates.TemplateResponse(
        "overlay.html", {"request": request, "code": "238"}
    )
