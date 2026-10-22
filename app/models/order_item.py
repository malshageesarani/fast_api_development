from sqlalchemy import Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class OrderItem(Base):

    __table__ = 'OrderItem'

orderItem_id:Mapped[int] = mapped_column(Integer,autoincrement=True,primary_key=True,index=True)
quantity:Mapped[int] = mapped_column(Integer,nullable=False)
unit_price:Mapped[float] = mapped_column(Numeric(12,2),nullable=False)
subtotal:Mapped[float] = mapped_column(Numeric(12,2),nullable=False)


