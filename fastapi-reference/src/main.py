import logging
from typing import Annotated

from pydantic import BaseModel

from fastapi import FastAPI, Header

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    age: int | None = None


@app.get("/get")
async def get(
    user_agent: Annotated[str, Header()],  # mandatory header
    any_header: Annotated[str | None, Header()] = None,  # optional header
):
    logging.info(user_agent)
    logging.info(any_header)
    return {"user_agent": user_agent, "any_header": any_header}


@app.get("/getQueryParams")
async def get_query_params(a, b):
    logging.info(a)
    logging.info(b)
    return {"a": a, "b": b}


@app.get("/getPathParams/{a}")
async def get_path_params(a):
    logging.info(a)
    return {"a": a}


@app.post("/post")
async def post(item: Item):
    logging.info(item)
    return item
