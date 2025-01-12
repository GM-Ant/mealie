<template>
  <v-card class="mt-4">
    <v-card-title>{{ $t("recipe.variation-management") }}</v-card-title>
    <v-card-text>
      <v-btn
        color="primary"
        :loading="isCreating"
        @click="createVariation"
      >
        {{ $t("recipe.create-variation") }}
      </v-btn>

      <v-btn
        v-if="selectedVariation"
        color="error"
        class="ml-2"
        :loading="isDeleting"
        @click="deleteVariation"
      >
        {{ $t("recipe.delete-variation") }}
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent, ref } from "@nuxtjs/composition-api"
import { Recipe } from "~/lib/api/types/recipe"
import { useRecipeApi } from "~/composables/api/recipe"
import { alert } from "~/composables/use-toast"

export default defineComponent({
  props: {
    recipe: {
      type: Object as () => Recipe,
      required: true
    },
    selectedVariation: {
      type: Object as () => Recipe | null,
      default: null
    }
  },

  setup(props, { emit }) {
    const isCreating = ref(false)
    const isDeleting = ref(false)

    const createVariation = async () => {
      isCreating.value = true
      try {
        const newVariation = await useRecipeApi().createVariation(props.recipe.id)
        emit("create", newVariation)
      } catch (error) {
        alert.error("Failed to create variation", null)
      } finally {
        isCreating.value = false
      }
    }

    const deleteVariation = async () => {
      if (!props.selectedVariation) return

      isDeleting.value = true
      try {
        await useRecipeApi().deleteVariation(props.selectedVariation.id)
        emit("delete", props.selectedVariation.id)
      } catch (error) {
        useToast().error("Failed to delete variation")
      } finally {
        isDeleting.value = false
      }
    }

    return {
      isCreating,
      isDeleting,
      createVariation,
      deleteVariation
    }
  }
})
</script>
