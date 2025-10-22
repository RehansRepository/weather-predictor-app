#!/usr/bin/env python
# coding: utf-8

# In[9]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# App title
st.title("🌍 Future Climate Prediction (2025–2075)")
st.markdown("Using LSTM to forecast weather and CO₂ levels for the next 50 years.")

# Available cities
PREDICTIONS_DIR = "predictions"
cities = sorted([f.split('_')[0] for f in os.listdir(PREDICTIONS_DIR) if f.endswith('_predictions.csv')])

# City selection
selected_city = st.selectbox("Select a City", cities)

# Load predictions
file_path = os.path.join(PREDICTIONS_DIR, f"{selected_city}_predictions.csv")
df = pd.read_csv(file_path)
df["Date"] = pd.to_datetime(df["Date"])

# Feature selection
feature = st.selectbox("Select Feature to View", ["Temperature", "Humidity", "WindSpeed", "CO2"])

# Plot
st.subheader(f"📈 {feature} Forecast for {selected_city}")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["Date"], df[feature], label=feature)
ax.set_xlabel("Year")
ax.set_ylabel(feature)
ax.set_title(f"{feature} Forecast for {selected_city} (2025–2075)")
st.pyplot(fig)

# Show data table
if st.checkbox("Show Raw Data"):
    st.dataframe(df[["Date", feature]])

# Download option
csv = df.to_csv(index=False)
st.download_button("Download Full Prediction CSV", csv, file_name=f"{selected_city}_predictions.csv", mime="text/csv")

