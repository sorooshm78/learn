# You can declare the type used for the response by annotating the path operation function return type.
# You can use type annotations the same way you would for input data in function parameters,
# you can use Pydantic models, lists, dictionaries, scalar values like integers, booleans, etc.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


# FastAPI will use this return type to:

#     * Validate the returned data.
#         If the data is invalid (e.g. you are missing a field), it means that your app code is broken, not returning what it should, and it will return a server error instead of returning incorrect data. This way you and your clients can be certain that they will receive the data and the data shape expected.
#     * Add a JSON Schema for the response, in the OpenAPI path operation.
#         This will be used by the automatic docs.
#         It will also be used by automatic client code generation tools.

# But most importantly:

#     * It will limit and filter the output data to what is defined in the return type.
#         This is particularly important for security, we'll see more of that below.


# -----------------------------

# response_model Parameter
# There are some cases where you need or want to return some data that is not exactly what the type declares.
# For example, you could want to return a dictionary or a database object, but declare it as a Pydantic model. This way the Pydantic model would do all the data documentation, validation, etc. for the object that you returned (e.g. a dictionary or database object).
# If you added the return type annotation, tools and editors would complain with a (correct) error telling you that your function is returning a type (e.g. a dict) that is different from what you declared (e.g. a Pydantic model).
# In those cases, you can use the path operation decorator parameter response_model instead of the return type.
# You can use the response_model parameter in any of the path operations:

#     @app.get()
#     @app.post()
#     @app.put()
#     @app.delete()

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

# -----------------------------

# Add an output model
# We can instead create an input model with the plaintext password and an output model without it:

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

# Here, even though our path operation function is returning the same input user that contains the password:

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

# -----------------------------

# Return Type and Data Filtering
# Let's continue from the previous example. We wanted to annotate the function with one type but return something that includes more data.
# We want FastAPI to keep filtering the data using the response model.
# In the previous example, because the classes were different, we had to use the response_model parameter. But that also means that we don't get the support from the editor and tools checking the function return type.
# But in most of the cases where we need to do something like this, we want the model just to filter/remove some of the data as in this example.
# And in those cases, we can use classes and inheritance to take advantage of function type annotations to get better support in the editor and tools, and still get the FastAPI data filtering.

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

# -----------------------------

# Return a Response Directly


from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

# This simple case is handled automatically by FastAPI because the return type annotation is the class (or a subclass) of Response.
# And tools will also be happy because both RedirectResponse and JSONResponse are subclasses of Response,
# so the type annotation is correct.
# Annotate a Response Subclass
# You can also use a subclass of Response in the type annotation:

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# This will also work because RedirectResponse is a subclass of Response, and FastAPI will automatically handle this simple case.

# Invalid Return Type Annotations

# But when you return some other arbitrary object that is not a valid Pydantic type (e.g. a database object) and you annotate it like that in the function,
# FastAPI will try to create a Pydantic response model from that type annotation, and will fail.
# The same would happen if you had something like a union between different types where one or more of them are not valid Pydantic types, for example this would fail 💥:

from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

# ...this fails because the type annotation is not a Pydantic type and is not just a single Response class or subclass, it's a union (any of the two) between a Response and a dict

# -----------------------------

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# and those default values won't be included in the response, only the values actually set.
# So, if you send a request to that path operation for the item with ID foo, the response (not including default values) will be:

# {
#     "name": "Foo",
#     "price": 50.2
# }


# -----------------------------

# response_model_include and response_model_exclude
# You can also use the path operation decorator parameters response_model_include and response_model_exclude.
# They take a set of str with the name of the attributes to include (omitting the rest) or to exclude (including the rest).
# This can be used as a quick shortcut if you have only one Pydantic model and want to remove some data from the output.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]


# -----------------------------
