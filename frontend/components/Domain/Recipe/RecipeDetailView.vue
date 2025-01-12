<template>
  <v-card class="mt-4">
    <v-card-title>{{ $t("recipe.details") }}</v-card-title>
    <v-card-text>
      <template v-if="recipe">
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              :value="recipe.name"
              :label="$t('recipe.name')"
              readonly
            />
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              :value="recipe.description"
              :label="$t('recipe.description')"
              readonly
            />
          </v-col>
        </v-row>

        <v-row v-if="isVariation">
          <v-col cols="12">
            <v-alert type="info">
              {{ $t("recipe.variation-of", { name: parentRecipe?.name || "" }) }}
            </v-alert>
          </v-col>
        </v-row>
      </template>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent, PropType, computed } from "@nuxtjs/composition-api"
import { Recipe } from "~/lib/api/types/recipe"

export default defineComponent({
  props: {
    recipe: {
      type: Object as PropType<Recipe | null>,
      default: null
    },
    parentRecipe: {
      type: Object as PropType<Recipe | null>,
      default: null
    }
  },

  setup(props) {
    const isVariation = computed(() => !!props.parentRecipe)

    return {
      isVariation
    }
  }
})
</script>
