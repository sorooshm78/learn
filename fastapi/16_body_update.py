# Body - Updates¶
# Update replacing with PUT¶
# To update an item you can use the HTTP PUT operation.
# You can use the jsonable_encoder to convert the input data to data that can be stored as JSON (e.g. with a NoSQL database). For example, converting datetime to str.


from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


# PUT is used to receive data that should replace the existing data.

# Warning about replacing¶
# That means that if you want to update the item bar using PUT with a body containing:

# {
#     "name": "Barz",
#     "price": 3,
#     "description": None,
# }

# because it doesn't include the already stored attribute "tax": 20.2, the input model would take the default value of "tax": 10.5.
# And the data would be saved with that "new" tax of 10.5.

# -----------------------------------------

# Partial updates with PATCH¶
# You can also use the HTTP PATCH operation to partially update data.
# This means that you can send only the data that you want to update, leaving the rest intact.

# Using Pydantic's exclude_unset parameter¶
# If you want to receive partial updates, it's very useful to use the parameter exclude_unset in Pydantic's model's .dict().
# Like item.dict(exclude_unset=True).
# That would generate a dict with only the data that was set when creating the item model, excluding default values.
# Then you can use this to generate a dict with only the data that was set (sent in the request), omitting default values:

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


# Using Pydantic's update parameter¶
# Now, you can create a copy of the existing model using .copy(), and pass the update parameter with a dict containing the data to update.
# Like stored_item_model.copy(update=update_data):


# -----------------------------------------
