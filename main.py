from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import datetime

app = FastAPI()

class Req(BaseModel):
    text: str = "Hola Martín. Soy CONSIA."

def now():
    return datetime.datetime.utcnow().isoformat() + "Z"

@app.get("/health")
def health():
    return {
        "ok": True,
        "engine": "CONSIA",
        "status": "ACTIVE",
        "mode": "AVATAR_ENGINE",
        "at": now()
    }

@app.post("/v1/avatar/render")
def render(req: Req):
    return JSONResponse({
        "ok": True,
        "reply": req.text,
        "video_url": "placeholder.mp4",
        "resumen": "Motor listo (fase inicial)"
    })
