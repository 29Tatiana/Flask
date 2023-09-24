from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from hw_6.dbmodels import database
from hw_6.routers import users, products, orders

app = FastAPI()
templates = Jinja2Templates(directory="./hw_6/templates")
app.include_router(users.router, tags=["users"])
app.include_router(products.router, tags=["products"])
app.include_router(orders.router, tags=["orders"])


@app.on_event("startup")
async def startup():
    await database.connect()
