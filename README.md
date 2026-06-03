# Smart Recipe Preparation Agent

## Problem Statement
Recipe Preparation Agent using IBM Watsonx.ai and Granite Foundation Model.

## Overview
This AI-powered cooking assistant helps users prepare recipes using ingredients available at home.

The system provides:
- Recipe Suggestions
- Cooking Instructions
- Ingredient Substitutions
- Cooking Tips
- Dietary Recommendations

## Technologies Used
- IBM Cloud Lite
- IBM Watsonx.ai
- IBM Granite 4h Small
- LangFlow
- Streamlit
- Python

## Architecture

User Ingredients
↓
Recipe Knowledge Base (recipes.csv)
↓
LangFlow Workflow
↓
IBM Granite 4h Small
↓
Recipe Response

## Features
- Ingredient-based recipe suggestions
- AI-generated cooking instructions
- Ingredient substitutions
- Dietary guidance
- IBM Granite integration
- LangFlow workflow automation

## Sample Input
egg, onion, tomato

## Future Enhancements
- RAG-based retrieval with vector database
- Personalized meal planning
- Nutrition analysis
- Multi-language support
