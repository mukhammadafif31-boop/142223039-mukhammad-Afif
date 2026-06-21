import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Dashboard Pelanggan",
    page_icon="📊",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}

[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #e6e6e6;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA GOOGLE DRIVE
# =========================
FILE_ID = "1z-n2vW1cfp8wYkNkR-aIlDbXJUgQ5C--"
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

@st.cache_data
def load_data():
    return pd.read_csv(URL)

try:
    df = load_data()

    # =========================
    # HEADER
    # =========================
    st.title("📊 Dashboard Data Pelanggan")
    st.markdown("Dashboard interaktif yang terhubung langsung ke Google Drive")

    # =========================
    # KPI
    # =========================
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Jumlah Data", len(df))
    col2.metric("Jumlah Kolom", len(df.columns))
    col3.metric("Missing Value", int(df.isnull().sum().sum()))
    col4.metric("Duplikat", int(df.duplicated().sum()))

    st.divider()

    # =========================
    # FILTER
    # =========================
    st.sidebar.header("🔍 Filter Data")

    filter_col = st.sidebar.selectbox(
        "Pilih Kolom",
        df.columns
    )

    pilihan = st.sidebar.multiselect(
        "Pilih Nilai",
        options=df[filter_col].dropna().unique()
    )

    if pilihan:
        filtered_df = df[df[filter_col].isin(pilihan)]
    else:
        filtered_df = df.copy()

    # =========================
    # DATAFRAME
    # =========================
    st.subheader("📋 Data Pelanggan")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500
    )

    # =========================
    # GRAFIK OTOMATIS
    # =========================
    st.subheader("📈 Visualisasi Data")

    kolom_kategori = filtered_df.columns[0]

    fig, ax = plt.subplots(figsize=(10, 5))

    filtered_df[kolom_kategori].value_counts().head(10).plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(f"Top 10 {kolom_kategori}")
    ax.set_xlabel(kolom_kategori)
    ax.set_ylabel("Jumlah")

    st.pyplot(fig)

    # =========================
    # DOWNLOAD
    # =========================
    st.download_button(
        label="⬇ Download Data",
        data=filtered_df.to_csv(index=False),
        file_name="data_pelanggan.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(f"Gagal memuat data: {e}")