# Request Body
# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
# A request body is data sent by the client to your API. A response body is the data your API sends to the client.
# Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.

from fastapi import FastAPI
from pydantic import BaseModel


# The same as when declaring query parameters,
# when a model attribute has a default value, it is not required. Otherwise,
# it is required. Use None to make it just optional.
# description and tax are optional (with a default value of None),
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    print(item)
    print(item.name.capitalize())
    return item


# -------------------------------------------

# Request body + path parameters
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# -------------------------------------------

