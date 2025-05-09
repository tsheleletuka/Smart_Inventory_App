# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from forecasting import generate_forecast

st.set_page_config(page_title="Smart Inventory Forecasting", layout="wide")

st.title("🧠 Smart Inventory Demand Forecasting App")

# Load the sample sales data
@st.cache_data
def load_data():
    return pd.read_csv("sample_sales.csv", parse_dates=["Date"])

df = load_data()

# Product selection
product_list = df['Product_Name'].unique()
selected_product = st.selectbox("Select a Product", product_list)

# Filter data for the selected product
filtered_df = df[df['Product_Name'] == selected_product]

# Display raw data
with st.expander("📊 View Product Sales Data"):
    st.dataframe(filtered_df)

# Forecast generation
if st.button("Generate Forecast"):
    forecast = generate_forecast(df, selected_product)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(forecast['ds'], forecast['yhat'], label='Forecast', color='blue')
    ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], alpha=0.3)
    ax.set_title(f"{selected_product} - Sales Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Units Sold")
    ax.legend()
    st.pyplot(fig)

    # Display forecast table
    st.subheader("📅 Forecasted Data (Next 7 Days)")
    st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7).reset_index(drop=True))
