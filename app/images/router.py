import shutil

from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix="/images",
    tags=["Load images"]
)


@router.post("/images")
async def add_cars(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
