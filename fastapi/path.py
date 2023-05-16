from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# --------------------------------------

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


# --------------------------------------

# Predefined values¶
# If you have a path operation that receives a path parameter,
# but you want the possible valid path parameter values to be predefined,
# you can use a standard Python Enum

from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# --------------------------------------

from enum import Enum

from fastapi import FastAPI


class CityName(Enum):
    tehran = "tehran"
    shiraz = "shiraz"
    mashhad = "mashhad"


app = FastAPI()


@app.get("/city/{city_name}")
async def get_city(city_name: CityName):
    if city_name is CityName.tehran:
        return {"city": "capital of Iran"}
    return {"city": "city of Iran"}


