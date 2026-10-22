
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator, Field


class OrderBase(BaseModel):
    order_date_time: datetime
    order_status:Optional[str] = Field(min_length=2,max_length=50,description="COMPLETED")
    price:float = Field(None,ge=0,decimal_places=2)




    @field_validator("date")
    @classmethod
    def validate_date(cls) -> int:
        current_date = datetime.now().date()
        return current_date


