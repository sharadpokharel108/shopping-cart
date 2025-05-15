from pydantic import BaseModel, Field
from typing import List

class CartItem(BaseModel):
    item: str = Field(..., title="Item name", min_length=1)
    price: float = Field(..., gt=0, title="Item price")
    quantity: int = Field(..., ge=1, title="Item quantity")

class CartSummary(BaseModel):
    total_price: float
    total_quantity: int
