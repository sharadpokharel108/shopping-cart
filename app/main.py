from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CartItem(BaseModel):
    name: str
    price: float
    quantity: int

cart = []

@app.post("/add/")
async def add_item(item: CartItem):
    cart.append(item)
    return {"message": f"Added {item.quantity} of {item.name} to the cart."}

@app.post("/remove/")
async def remove_item(item: CartItem):
    global cart
    cart = [i for i in cart if not (i.name == item.name and i.quantity == item.quantity)]
    return {"message": f"Removed {item.quantity} of {item.name} from the cart."}

@app.get("/cart/")
async def get_cart():
    return {"cart": cart}

@app.get("/total/")
async def get_total():
    total = sum(item.price * item.quantity for item in cart)
    return {"total": total}

@app.get("/quantities/")
async def get_quantities():
    quantities = {}
    for item in cart:
        if item.name in quantities:
            quantities[item.name] += item.quantity
        else:
            quantities[item.name] = item.quantity
    return {"quantities": quantities}
