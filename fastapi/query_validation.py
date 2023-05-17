from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# ----------------------------------------

# Additional validation
# Import Query and Annotated¶
# To achieve that, first import:
#     Query from fastapi
#     Annotated from typing

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    results = {"items": "lop lop"}
    if q:
        results.update({"q": q})
    return results


# q: str | None = None -> q: Annotated[str | None] = None

# ----------------------------------------

# Query as the default value or in Annotated
# Have in mind that when using Query inside of Annotated you cannot use the default parameter for Query.

# For example, this is not allowed:
# q: Annotated[str, Query(default="rick")] = "morty"

# So, you would use (preferably):
# q: Annotated[str, Query()] = "rick"


# ----------------------------------------

# Add regular expressions
# You can define a regular expression that the parameter should match:

# q: Annotated[str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")] = None):

# ----------------------------------------

# Default values
# You can, of course, use default values other than None.
# Let's say that you want to declare the q query parameter to have a min_length of 3, and to have a default value of "fixedquery":

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Make it required
# When we don't need to declare more validations or metadata,
# we can make the q query parameter required just by not declaring a default value


# ----------------------------------------

# Required with Ellipsis (...)
# There's an alternative way to explicitly declare that a value is required.
# You can set the default to the literal value ...:

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": "lop.."}
    if q:
        results.update({"q": q})
    return results


# ----------------------------------------

# Required with None
# You can declare that a parameter can accept None, but that it's still required.
# This would force clients to send a value, even if the value is None.
# To do that, you can declare that None is a valid type but still use ... as the default:

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
    results = {"items": "sample"}
    if q:
        results.update({"q": q})
    return results


# ----------------------------------------

# Query parameter list / multiple values
# When you define a query parameter explicitly with Query you can also declare it to receive a list of values,
# or said in other way, to receive multiple values.
# For example, to declare a query parameter q that can appear multiple times in the URL, you can write:

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


# Then, with a URL like:
# http://localhost:8000/items/?q=foo&q=bar


# So, the response to that URL would be:
# {
#   "q": [
#     "foo",
#     "bar"
#   ]
# }


# ----------------------------------------

# Deprecating parameters
# Now let's say you don't like this parameter anymore.
# You have to leave it there a while because there are clients using it, but you want the docs to clearly show it as deprecated.
# Then pass the parameter deprecated=True to Query:

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
            deprecated=True,
        ),
    ] = None
):
    results = {"items": "sample item"}
    if q:
        results.update({"q": q})
    return results


# ----------------------------------------
