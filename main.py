from fastapi import FastAPI, HTTPException
from starlette.requests import Request

from geo import locate_ip

app = FastAPI()


@app.get("/")
def roo(request: Request):
    location_data = locate_ip(request.client.host)
    return {
        'data': location_data
    }
