from datetime import datetime


from sqlalchemy import Integer, func, DateTime, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Order(Base):

    __table__ = 'Order'

order_id:Mapped[int] = mapped_column(Integer,autoincrement=True,primary_key=True,index=True)
order_date_time:Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), server_default=func.now())
order_status:Mapped[str] = mapped_column(String(50),nullable=False)
total_amount:Mapped[float] = mapped_column(Numeric(12,2),nullable=False)
loyalty_points_earned:Mapped[str] = mapped_column(String)
