import os
import shutil
import uuid
from fastapi import UploadFile, HTTPException
from app.schemas.upload_file import UploadCreate


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_uploaded_file(file: UploadFile) -> str:
    filename = file.filename.lower()
    extension = filename.split(".")[-1]

    if extension not in ["csv", "tif", "tiff"]:
        raise HTTPException(status_code=400, detail=f"Type non supporté : {filename}")

    new_filename = f"{uuid.uuid4()}_{filename}"
    file_path = os.path.join(UPLOAD_DIR, new_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return  UploadCreate(
        nom_fichier=filename,
        chemin_fichier=file_path,
        type_fichier=extension
    )

