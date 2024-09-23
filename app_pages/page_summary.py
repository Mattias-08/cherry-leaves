import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    """ Function to display project summary page """

    st.title("A Brief Summary of Project")

    st.header("General Information")

    st.info(
        f"**Powdery mildew** is a common fungal disease affecting cherry trees. It's caused by the pathogen Podosphaera clandestina.\n"
        f"Infected plants exhibit white, powdery spots on their leaves and stems, often starting on the lower leaves.\n\n"
        f"Powdery mildew is easily identifiable and can spread rapidly, causing significant damage to cherry trees.\n"
        f"It thrives in high humidity and moderate temperatures, reducing plant yield and overall health."
    )

    st.warning(
        f"**Project Dataset**\n\n"
        f"The dataset used in this project was sourced from Kaggle ([link](https://www.kaggle.com/codeinstitute/cherry-leaves)).\n"
        f"It consists of 2104 images of healthy cherry leaves and 2104 images of leaves infected with powdery mildew,\n"
        f"providing a balanced dataset for training and evaluation."
    )

    st.success(
        f"The project aims to address two key objectives:\n\n"
        f"1. **Visual Differentiation:** Develop a method to visually distinguish healthy cherry leaves from those infected with powdery mildew.\n\n"
        f"2. **Disease Classification:** Create a model capable of accurately classifying a given cherry leaf image as healthy or infected."
    )

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Mattias-08/cherry-leaves/blob/main/README.md).")