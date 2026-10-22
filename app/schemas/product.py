from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    product_name:str = Field(...,min_length=2,max_length=150,description="product name")
    price: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    available_quantity:int = Field(None,ge=0, description="How much quanity is available")
    active:str = Field(min_length=2,max_length=50)

class ProductCreate(ProductBase):
    product_code:int

class ProductSearch(BaseModel):
    name: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    categoryId: Optional[int] = None

class ProductResponse(ProductCreate):
    product_id : int
    product_code : int
    created_at : datetime
    updated_at :Optional[datetime] = None
