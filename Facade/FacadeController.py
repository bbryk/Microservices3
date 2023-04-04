import random

import uvicorn
from fastapi import FastAPI, APIRouter

from pydantic import BaseModel

from FacadeService import FacadeService

class Item(BaseModel):
    content : str
    id:int
class StartItem(BaseModel):
    content : str



class FacadeController():

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_request, methods=["GET"])
        self.router.add_api_route("/", self.post_request, methods=["POST"])
        self.fs = FacadeService()

    async def get_request(self):
        print(f"Received get in facade...")
        port = random.choice([8005, 8006,8007])
        logging_url = f"http://127.0.0.1:{port}"
        r = await self.fs.get_from_logging(logging_url)
        print(r.text)
        return 0

    async def post_request(self, item: StartItem):
        print(f"Received post: \"{item.content}\" in facade...")
        port = random.choice([8005, 8006,8007])
        logging_url = f"http://127.0.0.1:{port}"
        r = await self.fs.post_to_logging(item, logging_url)
        print(r.status_code)
        if r.status_code != 200:
            print("Something went wrong.")
        return item.content


if __name__ == "__main__":
    facade_port = 8001
    localhost = "127.0.0.1"
    app = FastAPI()
    fc = FacadeController()
    app.include_router(fc.router)
    uvicorn.run(app, host=localhost, port=facade_port)