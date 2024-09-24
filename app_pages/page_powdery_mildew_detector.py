import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_powdery_mildew_detector_body():
  """
  This function shows mildew detector page
  """
  st.header("Powdery Mildew Detection for Cherry Leaves")
  st.success(
      "**Identify Powdery Mildew:** Upload cherry leaf images to predict if they have the disease."
  )

  st.info(
      "**Download reference images:** Find sample cherry leaves with and without powdery mildew on [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)."
  )

  st.write(
      "**Upload images:** Drag and drop or select cherry leaf images to analyze."
  )
  images_buffer = st.file_uploader("", accept_multiple_files=True)

  st.write("**Click Make Prediction to start the analysis.**")
  predict_button = st.button("Make Prediction")

  if predict_button and images_buffer:
      df_report = pd.DataFrame([])
      for image in images_buffer:

          if image.type not in ('image/jpeg', 'image/png', 'image/bmp', 'image/tiff'):
              st.error(f"Error: Unsupported file format for {image.name}. Please upload JPG, PNG, BMP, or TIFF images.")
              continue

          img_pil = Image.open(image)
          st.info(f"Processing image: {image.name}")
          st.image(img_pil, caption=f"Image Size: {img_pil.size}")

          version = 'v1'
          resized_img = resize_input_image(img=img_pil, version=version)
          pred_proba, pred_class = load_model_and_predict(
              resized_img, version=version)
          plot_predictions_probabilities(pred_proba, pred_class)

          df_report = df_report.append({"Name": image.name, 'Result': pred_class},
                                         ignore_index=True)

      if not df_report.empty:
          st.success("Analysis Report")
          st.table(df_report)
          st.markdown(download_dataframe_as_csv(df_report))