import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Dashboard LDA [Opini Publik MBG]",
    page_icon="📊",
    layout="wide",
)



st.markdown("""
    <style>
        .stApp {
            background-color: #FFFFFF;
        }

        
        .stApp * {
            color: #1A1A2E !important;  /* ganti warna font di sini */
        }

        /* Khusus judul h1, h2, h3 */
        h1, h2, h3 {
            color: #0D47A1 !important;
        }

        /* Khusus teks paragraf biasa */
        p {
            color: #333333 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Analisis Opini Publik: Program Makan Bergizi Gratis (MBG)")
st.markdown(
    """
    | Info | Detail |
    |------|--------|
    | **Mata Kuliah** | Analisis Data Tak Terstruktur |
    | **Metode** | Text Mining + Topic Modeling (LDA) |
    | **Dataset** | 500 tweet terkait Program MBG |
    """
)
st.divider()

tab1, tab2 = st.tabs(["Visualisasi LDA Interaktif", "Detail Dashboard"])

with tab1:
    st.subheader("Visualisasi Interaktif Hasil LDA")
    st.markdown(
        """
        > **Petunjuk Membaca Visualisasi:**
        > - **Lingkaran besar** di kiri = topik; ukurannya menunjukkan proporsi topik dalam corpus.
        > - **Jarak antar lingkaran** = kemiripan antar topik (semakin jauh, semakin berbeda).
        > - **Bar chart** di kanan = kata-kata paling relevan untuk topik yang dipilih.
        > - Geser slider **λ (lambda)** untuk mengatur relevansi kata (λ=1 → frekuensi; λ=0 → keunikan topik).
        """
    )

    html_path = os.path.join(os.path.dirname(__file__), "lda_visualization_interactive.html")

    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=800, scrolling=True)
    else:
        st.error(
            "⚠️ File `lda_visualization_interactive.html` tidak ditemukan. "
            "Pastikan file ada di folder yang sama dengan `streamlit_app.py`."
        )

with tab2:
    st.subheader("Detail Dashboard")
    st.markdown(
        """
        Dashboard ini menampilkan hasil **Topic Modeling** menggunakan metode
        **Latent Dirichlet Allocation (LDA)** terhadap 500 tweet berbahasa Indonesia
        yang membahas Program Makan Bergizi Gratis (MBG).

        ### Preprocessing yang dilakukan:
        1. **Text Cleaning** 
        2. **Tokenization** 
        3. **Stopwords Removal** 
        4. **Stemming** 

        ### Model LDA:
        - Library: `gensim`
        - Jumlah topik optimal dipilih berdasarkan **Coherence Score**

        ### Topik yang teridentifikasi (6 topik):
        | Topik | Label | Proporsi |
        |-------|-------|----------|
        | 1 | Dampak Ekonomi & Lokal | ~16% |
        | 2 | Pengawasan & Implementasi | ~14% |
        | 3 | Distribusi Polri/Institusi | ~9% |
        | 4 | Anak, Pendidikan & Gizi | ~27% |
        | 5 | Korupsi & Anggaran | ~15% |
        | 6 | Distribusi & Kualitas | ~18% |
        """
    )
