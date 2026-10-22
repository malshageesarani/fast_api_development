

from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Product(Base):

    __table__ = 'product'

product_id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
product_code:Mapped[int] = mapped_column(Integer,unique=True,nullable=False)
product_name:Mapped[str] = mapped_column(String(50),nullable=False)
unit_price:Mapped[float] = mapped_column(Numeric(12,2),nullable=False)
available_quantity:Mapped[int]= mapped_column(Integer,nullable=False)
active:Mapped[str]= mapped_column(String(50))