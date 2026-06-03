import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()

st.set_page_config(
    page_title="Recipe Preparation Agent",
    page_icon="🍳"
)

st.title("🍳 Smart Recipe Preparation Agent")
st.write("RAG-based Recipe Agent using recipes.csv + IBM Granite")

df = pd.read_csv("recipes.csv")

api_key = os.getenv("IBM_API_KEY")
project_id = os.getenv("IBM_PROJECT_ID")
url = os.getenv("IBM_URL")


def retrieve_recipes(user_ingredients):
    user_items = [item.strip().lower() for item in user_ingredients.split(",")]
    retrieved = []

    for _, row in df.iterrows():
        recipe_ingredients = str(row["Ingredients"]).lower()
        score = 0

        for item in user_items:
            if item and item in recipe_ingredients:
                score += 1

        if score > 0:
            retrieved.append((score, row))

    retrieved.sort(key=lambda x: x[0], reverse=True)
    return [row for score, row in retrieved[:3]]


def generate_recipe_with_granite(user_ingredients, retrieved_recipes, diet_preference):
    recipe_context = ""

    for recipe in retrieved_recipes:
        recipe_context += f"""
Recipe Name: {recipe['Recipe Name']}
Ingredients: {recipe['Ingredients']}
Instructions: {recipe['Instructions']}
Category: {recipe['Category']}
"""

    prompt = f"""
You are a Smart Recipe Preparation Agent.

The user has these ingredients:
{user_ingredients}

Dietary preference:
{diet_preference}

Relevant recipes retrieved from the recipe knowledge base:
{recipe_context}

Using the retrieved recipes, generate a helpful final answer with:
1. Best Recipe Name
2. Ingredients Required
3. Step-by-Step Cooking Instructions
4. Ingredient Substitutions
5. Cooking Tips
6. Dietary Recommendations

Keep the answer clear, practical, and beginner-friendly.
"""

    credentials = {
        "url": url,
        "apikey": api_key
    }

    params = {
        GenParams.MAX_NEW_TOKENS: 700,
        GenParams.TEMPERATURE: 0.7
    }

    model = ModelInference(
        model_id="ibm/granite-4-h-small",
        credentials=credentials,
        project_id=project_id,
        params=params
    )

    return model.generate_text(prompt=prompt)


ingredients = st.text_input(
    "Enter available ingredients",
    placeholder="egg,onion,tomato"
)

diet = st.selectbox(
    "Select dietary preference",
    [
        "No Preference",
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan",
        "High Protein",
        "Low Carb"
    ]
)

if st.button("Generate Recipe"):
    if not ingredients.strip():
        st.warning("Please enter ingredients.")
    else:
        retrieved_recipes = retrieve_recipes(ingredients)

        if not retrieved_recipes:
            st.error("No matching recipe found in the knowledge base.")
        else:
            st.subheader("🔎 Retrieved Recipes from Knowledge Base")
            for recipe in retrieved_recipes:
                st.write(f"✅ {recipe['Recipe Name']}")

            st.subheader("🤖 IBM Granite Generated Recipe")
            with st.spinner("Generating recipe using IBM Granite..."):
                try:
                    result = generate_recipe_with_granite(
                        ingredients,
                        retrieved_recipes,
                        diet
                    )
                    st.write(result)
                except Exception as e:
                    st.error("Granite generation failed.")
                    st.write(e)
