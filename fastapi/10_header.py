# Header Parameters
# You can define Header parameters the same way you define Query, Path and Cookie parameters
# Then declare the header parameters using the same structure as with Path, Query and Cookie.
# The first value is the default value, you can pass all the extra validation or annotation parameters:

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


# ---------------------------------

# Automatic conversion
# Header has a little extra functionality on top of what Path, Query and Cookie provide.
# Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-).
# But a variable like user-agent is invalid in Python.
# So, by default, Header will convert the parameter names characters from underscore (_) to hyphen (-) to extract and document the headers.
# Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake_case").
# So, you can use user_agent as you normally would in Python code, instead of needing to capitalize the first letters as User_Agent or something similar.
# If for some reason you need to disable automatic conversion of underscores to hyphens, set the parameter convert_underscores of Header to False:

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None
):
    return {"strange_header": strange_header}


# ---------------------------------

# Duplicate headers
# It is possible to receive duplicate headers. That means, the same header with multiple values.
# You can define those cases using a list in the type declaration.
# You will receive all the values from the duplicate header as a Python list.
# For example, to declare a header of X-Token that can appear more than once, you can write:

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}


# If you communicate with that path operation sending two HTTP headers like:

# X-Token: foo
# X-Token: bar

# The response would be like:

# {
#     "X-Token values": [
#         "bar",
#         "foo"
#     ]
# }


# ---------------------------------
