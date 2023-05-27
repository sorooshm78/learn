# Continuing with the previous example, it will be common to have more than one related model.

# This is especially the case for user models, because:

#     The input model needs to be able to have a password.
#     The output model should not have a password.
#     The database model would probably need to have a hashed password.

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


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# About **user_in.dict()
# Pydantic's .dict()
# user_in is a Pydantic model of class UserIn.
# Pydantic models have a .dict() method that returns a dict with the model's data.
# So, if we create a Pydantic object user_in like:
# user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
# and then we call:
# user_dict = user_in.dict()
# we now have a dict with the data in the variable user_dict (it's a dict instead of a Pydantic model object).
# And if we call:
# print(user_dict)
# we would get a Python dict with:
# {
#     'username': 'john',
#     'password': 'secret',
#     'email': 'john.doe@example.com',
#     'full_name': None,
# }
# Unwrapping a dict
# If we take a dict like user_dict and pass it to a function (or class) with **user_dict, Python will "unwrap" it. It will pass the keys and values of the user_dict directly as key-value arguments.
# So, continuing with the user_dict from above, writing:
# UserInDB(**user_dict)
# Would result in something equivalent to:
# UserInDB(
#     username="john",
#     password="secret",
#     email="john.doe@example.com",
#     full_name=None,
# )
# Or more exactly, using user_dict directly, with whatever contents it might have in the future:
# UserInDB(
#     username = user_dict["username"],
#     password = user_dict["password"],
#     email = user_dict["email"],
#     full_name = user_dict["full_name"],
# )

# --------------------------------------

# Reduce duplication
# Reducing code duplication is one of the core ideas in FastAPI.
# As code duplication increments the chances of bugs, security issues, code desynchronization issues (when you update in one place but not in the others), etc.
# And these models are all sharing a lot of the data and duplicating attribute names and types.
# We could do better.
# We can declare a UserBase model that serves as a base for our other models. And then we can make subclasses of that model that inherit its attributes (type declarations, validation, etc).
# All the data conversion, validation, documentation, etc. will still work as normally.
# That way, we can declare just the differences between the models (with plaintext password, with hashed_password and without password):

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# ---------------------------------

# Union or anyOf
# You can declare a response to be the Union of two types, that means, that the response would be any of the two.
# It will be defined in OpenAPI with anyOf.
# To do that, use the standard Python type hint typing.Union

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]

# ---------------------------------

