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
