from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from data import get_movie_details

from models.movie import MoviePublic

router = APIRouter()

@router.get("/{id}", status_code=status.HTTP_201_CREATED)
async def get_movie_details(
    movie: Optional[MoviePublic] = Depends(get_movie_details)
) -> MoviePublic:
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return movie