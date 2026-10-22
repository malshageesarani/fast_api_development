from datetime import datetime

from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Customer(Base):

    __table__ = 'Customer'

customer_id:Mapped[int] = mapped_column(Integer,autoincrement=True,primary_key=True,index=True)
full_name:Mapped[str] = mapped_column(String(50),nullable=False)
email:Mapped[str] = mapped_column(String(100),nullable=False)
loyalty_points:Mapped[str] = mapped_column(String(50),nullable=True)
created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), server_default=func.now())