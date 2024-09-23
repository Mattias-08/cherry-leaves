import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"**Cherry Leaves:**\n"
        f"* Powdery mildew infection causes white, powdery spots or patches on leaves and stems.\n"
        f"* The powdery growth spreads, covering the entire leaf and making it appear dusted with white powder.\n"
        f"* We believe these features are sufficient to differentiate healthy from infected leaves.\n"
        f"* The ML model is expected to achieve at least 97% accuracy in classifying healthy and infected leaves."
    )

    st.success(
        f"**Validation:**\n\n"
        f"1. Visual Inspection:\n"
        f"   - Image Montage reveals clear visual differences between healthy and infected leaves, such as white patches and color changes.\n"
        f"* The ML pipeline performance was evaluated and it differentiates a healthy leaf and an infected leaf with at least 97% accuracy.\n\n"
    )