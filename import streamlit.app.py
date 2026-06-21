import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Pelanggan",
    layout="wide"
)

st.title("📊 Dashboard Pelanggan")

FILE_ID = "1z-n2vW1cfp8wYkNkR-aIlDbXJUgQ5C--"
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

try:
    df = pd.read_csv(URL)

    st.success("Data berhasil dimuat")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Jumlah Baris", len(df))

    with col2:
        st.metric("Jumlah Kolom", len(df.columns))

    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Error: {e}")
