from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# --------------------------------------------------------

# Singular values in body
# The same way there is a Query and Path to define extra data for query and path parameters, FastAPI provides an equivalent Body.
# For example, extending the previous model, you could decide that you want to have another key importance in the same body, besides the item and user.
# If you declare it as is, because it is a singular value, FastAPI will assume that it is a query parameter.
# But you can instruct FastAPI to treat it as another body key using Body:

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


# --------------------------------------------------------

# Embed a single body parameter¶
# Let's say you only have a single item body parameter from a Pydantic model Item.
# By default, FastAPI will then expect its body directly.
# But if you want it to expect a JSON with a key item and inside of it the model contents,
# as it does when you declare extra body parameters, you can use the special Body parameter embed:
# item: Item = Body(embed=True)

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


# In this case FastAPI will expect a body like:

# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }

# instead of:

# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }


# --------------------------------------------------------
