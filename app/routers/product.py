from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.session import get_session
from app.schemas.product import ProductResponse, ProductCreate
from app.services.products_services import ProductService

router = APIRouter(prefix="/products", tags=["Products"])
product_service = ProductService()


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(get_session)
):
    return await product_service.create_product(session, product_in)