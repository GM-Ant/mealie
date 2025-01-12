# Recipe Variations API

## Overview
The Recipe Variations API allows managing recipe variations, which are alternative versions of a base recipe. Variations inherit properties from their parent recipe but can have different ingredients, instructions, or other attributes.

## Endpoints

### Create Variation
`POST /api/recipes/{recipe_id}/variations`

Create a new variation from an existing recipe.

**Request Body:**
```json
{
  "name": "string",
  "description": "string",
  "ingredients": [
    {
      "title": "string",
      "note": "string",
      "unit": "string",
      "quantity": 0,
      "food": "string"
    }
  ],
  "instructions": [
    {
      "text": "string"
    }
  ]
}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "parent_id": "uuid",
  "is_variation": true
}
```

### Get Variations
`GET /api/recipes/{recipe_id}/variations`

Get all variations for a recipe.

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "parent_id": "uuid",
    "is_variation": true
  }
]
```

### Delete Variation
`DELETE /api/recipes/{recipe_id}/variations/{variation_id}`

Delete a recipe variation.

### Convert to Variation
`POST /api/recipes/{recipe_id}/variations/{variation_id}/convert-to-variation`

Convert an existing recipe to a variation of another recipe.

### Convert to Standalone
`POST /api/recipes/{recipe_id}/variations/{variation_id}/convert-to-standalone`

Convert a variation back to a standalone recipe.
