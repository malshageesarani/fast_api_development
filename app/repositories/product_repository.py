from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductCreate

class ProductRepository:

    async def create(self,session:AsyncSession,product:ProductCreate,):
        product_obj = Product(
            name = product.name,
            description = product.description,
            price = product.price,
            status= product.status
        )

        session.add(product_obj)
        await session.flush()
        return product_obj