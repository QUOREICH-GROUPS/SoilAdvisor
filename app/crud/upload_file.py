from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.upload_file import  Upload                                         
from app.schemas.upload_file import UploadCreate

async def create_upload(db: AsyncSession, upload_data: UploadCreate):
    upload = Upload(**upload_data.model_dump())
    db.add(upload)
    await db.commit()
    await db.refresh(upload)
    print("Upload created with ID:", upload.id)
    return upload

async def get_all_uploads(db: AsyncSession):
    result = await db.execute(select(Upload))
    return result.scalars().all()
