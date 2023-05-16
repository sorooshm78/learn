# Query Parameters
# When you declare other function parameters that are not part of the path parameters,
# they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# --------------------------------------

from fastapi import FastAPI

app = FastAPI()


# name and age -> required
@app.get("/person/")
async def person(name: str, age: int):
    return f"name is {name} and age is {age}"


# name and age -> optional
@app.get("/info/")
async def info(name: str = "ali", age: int = 10):
    return f"name is {name} and age is {age}"


# --------------------------------------

# Optional parameters
# The same way, you can declare optional query parameters, by setting their default to None

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# --------------------------------------

# Query parameter type conversion
# You can also declare bool types, and they will be converted:

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# In this case, if you go to:
# http://127.0.0.1:8000/items/foo?short=1
# or
# http://127.0.0.1:8000/items/foo?short=True
# or
# http://127.0.0.1:8000/items/foo?short=true
# or
# http://127.0.0.1:8000/items/foo?short=on
# or
# http://127.0.0.1:8000/items/foo?short=yes
# or any other case variation (uppercase, first letter in uppercase, etc),
# your function will see the parameter short with a bool value of True. Otherwise as False.
