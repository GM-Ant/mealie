from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from mealie.routes._base.deps import get_current_user
from mealie.schema.recipe import Recipe
from mealie.services.recipe_variation_service import RecipeVariationService

router = APIRouter(prefix="/recipes/{recipe_id}/variations", tags=["Recipe Variations"])


@router.post("", response_model=Recipe)
async def create_variation(
    recipe_id: UUID, variation_data: Recipe, service: RecipeVariationService = Depends(), _=Depends(get_current_user)
):
    """Create a new variation from an existing recipe"""
    try:
        return await service.create_variation(recipe_id, variation_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("", response_model=list[Recipe])
async def get_variations(recipe_id: UUID, service: RecipeVariationService = Depends(), _=Depends(get_current_user)):
    """Get all variations for a recipe"""
    return await service.get_variations(recipe_id)


@router.delete("/{variation_id}")
async def delete_variation(
    recipe_id: UUID, variation_id: UUID, service: RecipeVariationService = Depends(), _=Depends(get_current_user)
):
    """Delete a recipe variation"""
    try:
        await service.delete_variation(variation_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.post("/{variation_id}/convert-to-variation", response_model=Recipe)
async def convert_to_variation(
    recipe_id: UUID, variation_id: UUID, service: RecipeVariationService = Depends(), _=Depends(get_current_user)
):
    """Convert an existing recipe to a variation"""
    try:
        return await service.convert_to_variation(variation_id, recipe_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.post("/{variation_id}/convert-to-standalone", response_model=Recipe)
async def convert_to_standalone(
    recipe_id: UUID, variation_id: UUID, service: RecipeVariationService = Depends(), _=Depends(get_current_user)
):
    """Convert a variation back to a standalone recipe"""
    try:
        return await service.convert_to_standalone(variation_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
