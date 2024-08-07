import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def tampilkan_halaman():

    # Tombol di sidebar untuk kembali ke halaman utama
    with st.sidebar:
        if st.button("Kembali"):
            st.session_state.halaman = 'utama'

    # Menambahkan tombol untuk menuju halaman satudata.tulungagung.go.id
        if st.button("Kunjungi Satu Data Tulungagung"):
            st.markdown("[Klik di sini untuk mengunjungi Satu Data Tulungagung](https://satudata.tulungagung.go.id/)")

    # Membuat layout dua kolom
    col1, col2 = st.columns([1, 0.5])
    
    with col1:
        # Menampilkan tulisan "Diagram Lingkaran"
        st.write("### Diagram Lingkaran")

    with col2:
        # Menampilkan gambar dari folder foto
        st.image("foto/logo.png", width=200)

    # Menampilkan komponen file uploader
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    if st.button("Pengertian"):
        if st.button("Tutup"):
            st.session_state.show_terms = False
        st.text("Diagram lingkaran atau diagram pie adalah representasi grafis yang berbentuk \n lingkaran yang terbagi menjadi beberapa sektor. Setiap sektor merepresentasikan \n proporsi atau persentase dari suatu kategori terhadap keseluruhan data. Besar \n sudut setiap sektor sebanding dengan besaran data yang diwakilinya.")

    # Menambahkan tombol Syarat dan Ketentuan
    if st.button("Panduan Penggunaan"):
        if st.button("Tutup"):
            st.session_state.show_terms = False
        st.info("Berikut cara penggunaan aplikasi:")
        st.text("1. File harus berformat CSV \n2. Untuk contoh isi file CSV seperti gambar ini :")
        st.image("foto/image.png")

    # Jika file diunggah
    if uploaded_file is not None:
        # Membaca data dari file CSV yang diunggah
        data = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah dan dibaca")

        # Ekstraksi nama kolom pertama
        kolom_pertama = data.columns[0]
        st.write(f"Kolom pertama: {kolom_pertama}")

        # Ekstraksi data dari kolom pertama
        label_pertama = data[kolom_pertama]
        
        # Menampilkan daftar opsi yang tersedia
        opsi = data.columns[1:]  # Mengambil semua kolom kecuali kolom pertama
        selected_opsi = st.selectbox("Pilih Opsi:", opsi)

        # Ekstraksi jumlah data untuk opsi yang dipilih
        jumlah = data[selected_opsi]

        # Fungsi untuk format angka pada sumbu y
        def format_angka(x, pos):
            return '{:,.0f}'.format(x)

        # Membuat diagram lingkaran
        fig, ax = plt.subplots(figsize=(10, 11))
        ax.pie(jumlah, labels=label_pertama, autopct='%1.1f%%', startangle=140)

        # Menambahkan jumlah total di pojok kanan atas
        total = sum(jumlah)
        ax.text(1.5, 1.5, f'Total: {total}', horizontalalignment='right', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

        ax.set_title(f'Diagram Lingkaran {selected_opsi}')
        ax.axis('equal')

        # Menampilkan diagram menggunakan Streamlit
        st.pyplot(fig)
    else:
        st.info("Silakan unggah file CSV.")
