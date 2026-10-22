from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    product_name:str = Field(...,min_length=2,max_length=150,description="product name")