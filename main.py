from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/location/{header_url_code}/{location_code}", response_class=HTMLResponse)
async def get_overlay(request: Request, header_url_code: str, location_code: str):
    return templates.TemplateResponse(
        "overlay.html",
        {
            "request": request,
            "header_url_code": header_url_code,
            "location_code": location_code,
        },
    )
