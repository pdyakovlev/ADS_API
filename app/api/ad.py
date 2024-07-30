from fastapi import APIRouter, Depends

from app.crud.ad import ad_crud

from app.schemas.ad import AdCreate, AdRead
from app.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/ad',
                   tags=['Ads'])


@router.get(
    '/',
    response_model=list[AdRead],
    response_model_exclude_none=True,
)
async def get_all_ads(
        session: AsyncSession = Depends(get_async_session)
):
    ad = await ad_crud.get_multi(session)
    return ad[0:10]


@router.get(
    '/{ad_id}/',
    response_model=AdRead,
    response_model_exclude_none=True,
)
async def get_ad(
        ad_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    ad = await ad_crud.get(ad_id, session)
    if ad is None:
        return {'name': "No ad"}  # сделать валидатор
    return ad


@router.post(
    '/',
    response_model=AdCreate,
    response_model_exclude_none=True
)
async def create_ad(
        ad: AdCreate,
        session: AsyncSession = Depends(get_async_session)
):
    new_ad = await ad_crud.create(ad, session)
    return new_ad


@router.patch('/{ad_id}/',
              response_model=AdRead,
              response_model_exclude_none=True,)
async def partialy_update_ad(
        ad_id: int,
        cat_in: AdRead,
        session: AsyncSession = Depends(get_async_session)):
    ad = await ad_crud.get(ad_id, session)
    ad_updated = await ad_crud.update(ad, cat_in, session)
    return ad_updated


@router.delete('/{ad_id}/',
               response_model=AdRead,
               response_model_exclude_none=True,)
async def remove_ad(ad_id: int,
                    session: AsyncSession = Depends(get_async_session)):
    ad = await ad_crud.get_by_attribute('id', ad_id, session)
    deleted_ad = await ad_crud.remove(ad, session)
    return deleted_ad
