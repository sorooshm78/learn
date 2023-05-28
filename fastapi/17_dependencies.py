# What is "Dependency Injection"¶
# "Dependency Injection" means, in programming, that there is a way for your code (in this case, your path operation functions) to declare things that it requires to work and use: "dependencies".
# And then, that system (in this case FastAPI) will take care of doing whatever is needed to provide your code with those needed dependencies ("inject" the dependencies).
# This is very useful when you need to:
#     Have shared logic (the same code logic again and again).
#     Share database connections.
#     Enforce security, authentication, role requirements, etc.
#     And many other things...
# All these, while minimizing code repetition.
# First Steps¶
# Let's see a very simple example. It will be so simple that it is not very useful, for now.
# But this way we can focus on how the Dependency Injection system works.
# Create a dependency, or "dependable"¶
# Let's first focus on the dependency.
# It is just a function that can take all the same parameters that a path operation function can take

from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


# Although you use Depends in the parameters of your function the same way you use Body, Query, etc, Depends works a bit differently.
# You only give Depends a single parameter.
# This parameter must be something like a function.
# You don't call it directly (don't add the parenthesis at the end), you just pass it as a parameter to Depends().
# And that function takes parameters in the same way that path operation functions do.

# Whenever a new request arrives, FastAPI will take care of:
#     Calling your dependency ("dependable") function with the correct parameters.
#     Get the result from your function.
#     Assign that result to the parameter in your path operation function.

# ----------------------------------------

# Share Annotated dependencies¶
# In the examples above, you see that there's a tiny bit of code duplication.
# When you need to use the common_parameters() dependency, you have to write the whole parameter with the type annotation and Depends():
# commons: Annotated[dict, Depends(common_parameters)]
# But because we are using Annotated, we can store that Annotated value in a variable and use it

from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: CommonsDep):
    return commons


@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons


# ----------------------------------------

from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

# ----------------------------------------

from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


# ----------------------------------------

# Global Dependencies¶
# For some types of applications you might want to add dependencies to the whole application.
# Similar to the way you can add dependencies to the path operation decorators, you can add them to the FastAPI application.
# In that case, they will be applied to all the path operations in the application

from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


# ----------------------------------------
