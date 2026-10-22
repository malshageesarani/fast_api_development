from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductResponse, ProductCreate


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    async def create_product(self, session: AsyncSession, product_in: ProductCreate) -> ProductResponse:
        try:
            existing = await self.repository.get_by_id(session, product_in.id)
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Product with slug '{product_in.id}' already exists."
                )

            db_product = await self.repository.create(session, product_in)
            await session.commit()
            await session.refresh(db_product)

        return ProductResponse.model_validate(db_product)

    async def search_by_id(self, session: AsyncSession, product_id: int) -> Optional[Product]:
        query = select(Product).where(Product.id == product_id)
        result = await  session.execute(query)
        return result.scalar_one_or_none()
