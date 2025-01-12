import { useRequests } from "./api-client"
import { Recipe } from "~/lib/api/types/recipe"

export function useRecipeApi() {
    const apiClient = useRequests()

    return {
        async createVariation(recipeId: string): Promise<Recipe> {
            const { data } = await apiClient.post<Recipe>(`/recipes/${recipeId}/variations`, {})
            return data!
        },

        async deleteVariation(variationId: string): Promise<void> {
            await apiClient.delete(`/recipes/${variationId}`)
        },

        async getVariations(recipeId: string): Promise<Recipe[]> {
            const { data } = await apiClient.get<Recipe[]>(`/recipes/${recipeId}/variations`)
            return data!
        }
    }
}
