import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Web Saya",
    page_icon="🚀",
    layout="centered"
)

# Header
st.title("🎉 Selamat Datang di Aplikasi Web Saya")
st.markdown("---")

# Sidebar
st.sidebar.header("Menu Navigasi")
menu = st.sidebar.selectbox(
    "Pilih Halaman:",
    ["Beranda", "Tentang", "Kontak"]
)

# Konten berdasarkan menu
if menu == "Beranda":
    st.header("Beranda")
    st.write("Ini adalah halaman utama aplikasi web Anda.")
    
    # LINK GOOGLE DRIVE (SUDAH DITAMBAHKAN)
    st.link_button(
        "📥 Download File dari Google Drive",
        "https://drive.google.com/file/d/1z-n2vW1cfp8wYkNkR-aIlDbXJUgQ5C--/view?usp=drive_link"
    )
    
    st.markdown("---")
    
    # Contoh input
    nama = st.text_input("Masukkan nama Anda:")
    if nama:
        st.success(f"Halo, {nama}! Selamat datang! 👋")
    
    # Contoh tombol
    if st.button("Klik Saya"):
        st.balloons()
        st.info("Anda baru saja mengklik tombol!")

elif menu == "Tentang":
    st.header("Tentang Aplikasi")
    st.write("""
    Aplikasi ini dibuat menggunakan **Streamlit**, 
    framework Python untuk membuat aplikasi web dengan cepat dan mudah.
    """)
    
    # Contoh kolom
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Pengguna", "1,234", "+12%")
    with col2:
        st.metric("Rating", "4.8", "+0.2")

elif menu == "Kontak":
    st.header("Hubungi Kami")
    
    with st.form("form_kontak"):
        email = st.text_input("Email")
        pesan = st.text_area("Pesan")
        kirim = st.form_submit_button("Kirim")
        
        if kirim:
            if email and pesan:
                st.success("Pesan berhasil dikirim!")
            else:
                st.error("Mohon isi semua field.")

# Footer
st.markdown("---")
st.caption("© 2024 Aplikasi Web Saya | Dibuat dengan ❤️ dan Streamlit")
