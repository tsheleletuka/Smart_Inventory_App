# forecasting.py

import pandas as pd
from prophet import Prophet

def generate_forecast(df, product_name):
    # Filter and prepare data
    product_df = df[df['Product_Name'] == product_name][['Date', 'Units_Sold']].copy()
    product_df.rename(columns={'Date': 'ds', 'Units_Sold': 'y'}, inplace=True)

    # Fit the model
    model = Prophet()
    model.fit(product_df)

    # Make forecast
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    return forecast
