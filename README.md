# Smart Recipe Preparation Agent

## Problem Statement

Recipe Preparation Agent using IBM Watsonx.ai and IBM Granite Foundation Model.

## Overview

This AI-powered cooking assistant helps users prepare recipes using ingredients available at home. The system generates recipe suggestions, cooking instructions, ingredient substitutions, and dietary recommendations.

## Technologies Used

* IBM Cloud Lite
* IBM Watsonx.ai
* IBM Granite 4h Small
* LangFlow
* Streamlit
* Python

## System Architecture

```text
User Ingredients
        ↓
Recipe Knowledge Base (recipes.csv)
        ↓
Ingredient Matching & Retrieval
        ↓
LangFlow Workflow
        ↓
IBM Granite 4h Small
        ↓
Recipe Generation
        ↓
Final Recipe Response
```

## Features

* Ingredient-based recipe suggestions
* AI-powered recipe generation
* Step-by-step cooking instructions
* Ingredient substitutions
* Dietary recommendations
* IBM Granite integration
* LangFlow workflow automation

## Sample Input

egg, onion, tomato

## Sample Output

* Recipe Name
* Ingredients Required
* Cooking Instructions
* Ingredient Substitutions
* Cooking Tips
* Dietary Recommendations

## Future Enhancements

* RAG-based retrieval with vector database
* Personalized meal planning
* Nutrition analysis
* Multi-language support
  
  ## RAG Implementation
  
The project uses `recipes.csv` as a recipe knowledge base. Based on user-entered ingredients, the app retrieves the most relevant recipes and sends them as context to IBM Granite 4h Small for final recipe generation.
