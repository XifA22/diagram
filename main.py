import streamlit as st

# Fungsi untuk halaman utama
def halaman_utama():
    # Membuat container untuk kolom kedua dengan gambar di pojok kanan
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            pass 
        with col2:
            st.image("foto/logo.png", width=200)

    # Membuat container untuk kolom pertama
    with st.container():
        st.title("Visualisasi Data \n Silahkan pilih diagram yang ingin digunakan (double klik/tap :)")
        if st.button("Diagram Lingkaran"):
            st.session_state['halaman'] = 'Diagram Lingkaran'
        if st.button("Diagram Batang"):
            st.session_state['halaman'] = 'Diagram Batang'
        if st.button("Diagram Garis"):
            st.session_state['halaman'] = 'Diagram Garis'
    
# Menentukan halaman yang akan ditampilkan berdasarkan status aplikasi
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'utama'
if st.session_state['halaman'] == 'utama':
    halaman_utama()
elif st.session_state['halaman'] == 'Diagram Lingkaran':
    import lingkaran
    lingkaran.tampilkan_halaman()
elif st.session_state['halaman'] == 'Diagram Batang':
    import batang
    batang.tampilkan_halaman()
elif st.session_state['halaman'] == 'Diagram Garis':
    import garis
    garis.tampilkan_halaman()
