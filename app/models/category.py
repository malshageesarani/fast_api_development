from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class category(Base):

    __table__ = "category"

category_id:Mapped[int] = mapped_column(Integer,autoincrement=True,primary_key=True,index=True)
category_code:Mapped[int] = mapped_column(Integer,unique=True,nullable=False)
category_name:Mapped[str] = mapped_column(String(100),nullable=False)
description:Mapped[str] = mapped_column(String(200),nullable=True)
active:Mapped[str] = mapped_column(String(20),nullable=False)


