import streamlit as st
import pandas as pd
import os

# === Streamlit UI ===
st.set_page_config(page_title="CSV Dashboard", layout="wide")
st.title("📂 CSV Viewer Dashboard (Deployed)")

# === Read CSV from bundled file ===
DATA_PATH = os.path.join("data", "secure_data.csv")

try:
    df = pd.read_csv(DATA_PATH)
    st.subheader("📊 Data Preview")
    st.dataframe(df, use_container_width=True)

    if st.checkbox("Show Summary Statistics"):
        st.subheader("Summary")
        st.write(df.describe(include='all'))

    if st.checkbox("Filter by Column"):
        col = st.selectbox("Choose a column to filter", df.columns)
        unique_vals = df[col].dropna().unique()
        filter_val = st.selectbox(f"Select value in {col}", unique_vals)
        st.write(df[df[col] == filter_val])

except FileNotFoundError:
    st.error("❌ CSV file not found. Make sure 'data/secure_data.csv' is bundled with the app.")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
