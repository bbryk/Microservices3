

import uvicorn
from fastapi import FastAPI, APIRouter

from pydantic import BaseModel



class Item(BaseModel):
    id:int
    content : str


class MessagesController():

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_request, methods=["GET"])
    async def get_request(self):
        print(f"Received get in messages...")
        return "Not implemented"




if __name__ == "__main__":
    facade_port = 8100
    localhost = "127.0.0.1"
    app = FastAPI()
    fcd_cntrllr = MessagesController()
    app.include_router(fcd_cntrllr.router)
    uvicorn.run(app, host=localhost, port=facade_port)