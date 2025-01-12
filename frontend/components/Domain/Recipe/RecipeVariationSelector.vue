<template>
  <v-card class="mt-4">
    <v-card-title>{{ $t("recipe.variations") }}</v-card-title>
    <v-card-text>
      <template v-if="isLoading">
        <v-progress-linear indeterminate />
      </template>
      <template v-else>
        <v-select
          v-if="variations.length > 0"
          :items="variations"
          item-text="name"
          item-value="id"
          :label="$t('recipe.select-variation')"
          @change="$emit('select', $event)"
        />
        <v-alert
          v-else
          type="info"
        >
          {{ $t("recipe.no-variations") }}
        </v-alert>
      </template>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent, PropType, ref, watch } from "@nuxtjs/composition-api"
import { Recipe } from "~/lib/api/types/recipe"
import { useRecipeApi } from "~/composables/api/recipe"

export default defineComponent({
  props: {
    recipeId: {
      type: String,
      required: true
    }
  },

  setup(props, { emit }) {
    const variations = ref<Recipe[]>([])
    const isLoading = ref(false)
    const api = useRecipeApi()

    const loadVariations = async () => {
      isLoading.value = true
      try {
        variations.value = await api.getVariations(props.recipeId)
      } catch (error) {
        variations.value = []
      } finally {
        isLoading.value = false
      }
    }

    watch(() => props.recipeId, loadVariations, { immediate: true })

    return {
      variations,
      isLoading
    }
  }
})
</script>
