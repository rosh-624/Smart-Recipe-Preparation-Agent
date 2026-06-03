import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Recipe Preparation Agent",
    page_icon="🍳"
)

st.title("🍳 Smart Recipe Preparation Agent")

df = pd.read_csv("recipes.csv")

ingredients = st.text_input(
    "Enter ingredients",
    placeholder="egg,onion,tomato"
)

if st.button("Find Recipe"):

    found_recipes = []

    for _, row in df.iterrows():

        recipe_ingredients = row["Ingredients"].lower()

        user_ingredients = ingredients.lower()

        matches = 0

        for item in user_ingredients.split(","):
            if item.strip() in recipe_ingredients:
                matches += 1

        if matches > 0:
            found_recipes.append(row)

    if found_recipes:

        recipe = found_recipes[0]

        st.success("Recipe Found!")

        st.subheader(recipe["Recipe Name"])

        st.write("Ingredients:")
        st.write(recipe["Ingredients"])

        st.write("Instructions:")
        st.write(recipe["Instructions"])

    else:
        st.error("No matching recipe found.")