# With FastAPI, you can define, validate, document, and use arbitrarily deeply nested models

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# # ----------------------------------

# List fields with type parameter
# But Python has a specific way to declare lists with internal types, or "type parameters":
# Import typing's List
# In Python 3.9 and above you can use the standard list to declare these type annotations as we'll see below.
# But in Python versions before 3.9 (3.6 and above), you first need to import List from standard Python's typing module:

from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[int] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# # ----------------------------------

# Set types
# But then we think about it, and realize that tags shouldn't repeat, they would probably be unique strings.
# And Python has a special data type for sets of unique items, the set.
# Then we can declare tags as a set of strings:

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# With this, even if you receive a request with duplicate data, it will be converted to a set of unique items.
# And whenever you output that data, even if the source had duplicates, it will be output as a set of unique items.

# # ----------------------------------

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    image: Image | None = None


@app.put("/items/")
async def update_item(item: Item):
    results = {"item": item}
    return results


# # ----------------------------------

# Special types and validation
# Apart from normal singular types like str, int, float, etc. You can use more complex singular types that inherit from str.
# To see all the options you have, checkout the docs for Pydantic's exotic types. You will see some examples in the next chapter.
# For example, as in the Image model we have a url field, we can declare it to be instead of a str, a Pydantic's HttpUrl:

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    image: Image | None = None


@app.put("/items/")
async def update_item(item: Item):
    results = {"item": item}
    return results


# # ----------------------------------

# Attributes with lists of submodels

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# # ----------------------------------

# Bodies of arbitrary dicts
# You can also declare a body as a dict with keys of some type and values of other type.
# Without having to know beforehand what are the valid field/attribute names (as would be the case with Pydantic models).
# This would be useful if you want to receive keys that you don't already know.
# Other useful case is when you want to have keys of other type, e.g. int.
# That's what we are going to see here.
# In this case, you would accept any dict as long as it has int keys with float values:

from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[str, int]):
    return weights


# # ----------------------------------
