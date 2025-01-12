from uuid import UUID

from mealie.repos.all_repositories import get_repositories
from mealie.schema.recipe import Recipe


class RecipeVariationService:
    def __init__(self):
        self.repos = get_repositories()

    async def create_variation(self, parent_id: UUID, variation_data: Recipe) -> Recipe:
        """Create a new recipe variation from an existing recipe"""
        parent = await self.repos.recipes.get_one(parent_id)

        # Create new recipe with variation data
        variation = await self.repos.recipes.create(variation_data)

        # Set variation relationship
        variation.parent_id = parent.id
        variation.is_variation = True
        await self.repos.recipes.update(variation.id, variation)

        return variation

    async def get_variations(self, parent_id: UUID) -> list[Recipe]:
        """Get all variations for a parent recipe"""
        return await self.repos.recipes.get_many(parent_id=parent_id)

    async def delete_variation(self, variation_id: UUID) -> None:
        """Delete a recipe variation"""
        variation = await self.repos.recipes.get_one(variation_id)

        if not variation.is_variation:
            raise ValueError("Cannot delete non-variation recipe")

        await self.repos.recipes.delete(variation_id)

    async def convert_to_variation(self, recipe_id: UUID, parent_id: UUID) -> Recipe:
        """Convert an existing recipe to a variation"""
        recipe = await self.repos.recipes.get_one(recipe_id)

        if recipe.is_variation:
            raise ValueError("Recipe is already a variation")

        recipe.parent_id = parent_id
        recipe.is_variation = True
        return await self.repos.recipes.update(recipe_id, recipe)

    async def convert_to_standalone(self, variation_id: UUID) -> Recipe:
        """Convert a variation back to a standalone recipe"""
        variation = await self.repos.recipes.get_one(variation_id)

        if not variation.is_variation:
            raise ValueError("Recipe is not a variation")

        variation.parent_id = None
        variation.is_variation = False
        return await self.repos.recipes.update(variation_id, variation)
