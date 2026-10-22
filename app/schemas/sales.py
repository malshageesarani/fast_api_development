

from pydantic import BaseModel, Field


class SaleBase(BaseModel):
    quantity:int = Field(...,ge=0)
    unit_price: float = Field(None, ge=0, decimal_places=2)
    subtotal:float

