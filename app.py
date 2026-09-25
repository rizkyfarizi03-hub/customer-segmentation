import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LOAD MODEL
# =========================================================
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
.stApp {
    background: #0b1120;
}

.block-container {
    max-width: 1120px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* NAV */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 32px;
}

.nav-logo {
    color: #f8fafc;
    font-size: 18px;
    font-weight: 700;
}

.nav-logo-accent {
    color: #3b82f6;
}

.nav-author {
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.3px;
}

/* HERO */
.hero {
    padding: 45px;
    border-radius: 24px;
    border: 1px solid #1e293b;
    background: linear-gradient(
        135deg,
        #111827 0%,
        #0f172a 100%
    );
    margin-bottom: 28px;
}

.hero-badge {
    display: inline-block;
    padding: 6px 11px;
    border-radius: 999px;
    background: rgba(37, 99, 235, 0.12);
    border: 1px solid rgba(59, 130, 246, 0.22);
    color: #93c5fd;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.hero-title {
    color: #f8fafc;
    font-size: 45px;
    font-weight: 750;
    line-height: 1.1;
    letter-spacing: -1.8px;
    max-width: 760px;
    margin-bottom: 16px;
}

.hero-accent {
    color: #3b82f6;
}

.hero-description {
    color: #94a3b8;
    font-size: 15px;
    line-height: 1.8;
    max-width: 720px;
}

/* INFO CARD */
.info-card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 16px;
    padding: 20px;
    min-height: 112px;
}

.info-label {
    font-size: 10px;
    color: #64748b;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.info-value {
    color: #f8fafc;
    font-size: 22px;
    font-weight: 700;
}

.info-desc {
    color: #64748b;
    font-size: 12px;
    margin-top: 5px;
}

/* SECTION */
.section-title {
    color: #f8fafc;
    font-size: 25px;
    font-weight: 700;
    letter-spacing: -0.6px;
    margin-top: 45px;
}

.section-description {
    color: #64748b;
    font-size: 13px;
    margin-top: 5px;
    margin-bottom: 20px;
}

/* FORM */
div[data-testid="stForm"] {
    background: #0f172a;
    border: 1px solid #1e293b;
    padding: 25px;
    border-radius: 18px;
}

div[data-testid="stNumberInput"] input {
    background-color: #111827 !important;
    border-radius: 10px !important;
}

div[data-testid="stFormSubmitButton"] button {
    width: 100%;
    height: 48px;
    border-radius: 10px;
    border: none;
    background: #2563eb;
    color: white;
    font-weight: 650;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #1d4ed8;
    color: white;
}

/* RESULT */
.result-card {
    border-radius: 18px;
    padding: 28px;
    margin-top: 10px;
}

.result-high {
    border: 1px solid rgba(16, 185, 129, 0.30);
    background: rgba(16, 185, 129, 0.07);
}

.result-regular {
    border: 1px solid rgba(59, 130, 246, 0.30);
    background: rgba(59, 130, 246, 0.07);
}

.result-inactive {
    border: 1px solid rgba(239, 68, 68, 0.28);
    background: rgba(239, 68, 68, 0.06);
}

.result-label {
    font-size: 11px;
    font-weight: 750;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.high-label {
    color: #34d399;
}

.regular-label {
    color: #60a5fa;
}

.inactive-label {
    color: #f87171;
}

.result-title {
    color: #f8fafc;
    font-size: 27px;
    font-weight: 700;
    margin-bottom: 10px;
}

.result-description {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.75;
}

.strategy {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 17px;
    margin-top: 12px;
}

.strategy-title {
    color: #cbd5e1;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.8px;
    margin-bottom: 5px;
}

.strategy-text {
    color: #94a3b8;
    font-size: 13px;
}

/* FOOTER */
.custom-footer {
    border-top: 1px solid #1e293b;
    margin-top: 55px;
    padding-top: 22px;
    display: flex;
    justify-content: space-between;
    color: #475569;
    font-size: 11px;
}

.author {
    color: #64748b;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVBAR
# =========================================================
st.markdown(
    '<div class="navbar"><div class="nav-logo">Customer<span class="nav-logo-accent">Segmentation</span></div><div class="nav-author">RIZKYSTARBOY</div></div>',
    unsafe_allow_html=True
)

# =========================================================
# HERO
# =========================================================
st.markdown(
    '<div class="hero">'
    '<div class="hero-badge">CUSTOMER ANALYTICS · MACHINE LEARNING</div>'
    '<div class="hero-title">Understand customer behavior through <span class="hero-accent">data-driven segmentation.</span></div>'
    '<div class="hero-description">Sistem segmentasi pelanggan menggunakan K-Means Clustering untuk mengelompokkan pelanggan berdasarkan Recency, Frequency, dan Monetary sehingga pola perilaku pelanggan dapat dianalisis secara lebih terstruktur.</div>'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# MODEL SUMMARY
# =========================================================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        '<div class="info-card">'
        '<div class="info-label">ALGORITHM</div>'
        '<div class="info-value">K-Means</div>'
        '<div class="info-desc">Unsupervised Learning</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="info-card">'
        '<div class="info-label">CLUSTERS</div>'
        '<div class="info-value">3</div>'
        '<div class="info-desc">Customer Segments</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        '<div class="info-card">'
        '<div class="info-label">FEATURES</div>'
        '<div class="info-value">RFM</div>'
        '<div class="info-desc">Recency · Frequency · Monetary</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        '<div class="info-card">'
        '<div class="info-label">METHODOLOGY</div>'
        '<div class="info-value">CRISP-DM</div>'
        '<div class="info-desc">Data Mining Framework</div>'
        '</div>',
        unsafe_allow_html=True
    )

# =========================================================
# CUSTOMER ANALYSIS
# =========================================================
st.markdown(
    '<div class="section-title">Customer Analysis</div>'
    '<div class="section-description">Masukkan data RFM pelanggan untuk menentukan hasil segmentasi.</div>',
    unsafe_allow_html=True
)

with st.form("customer_analysis"):

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input(
            "Recency",
            min_value=0,
            value=30,
            step=1,
            help="Jumlah hari sejak transaksi terakhir."
        )

    with col2:
        frequency = st.number_input(
            "Frequency",
            min_value=1,
            value=3,
            step=1,
            help="Jumlah transaksi pelanggan."
        )

    with col3:
        monetary = st.number_input(
            "Monetary",
            min_value=0.0,
            value=500.0,
            step=50.0,
            help="Total nilai pembelian pelanggan."
        )

    st.write("")

    submit = st.form_submit_button(
        "Analyze Customer"
    )

# =========================================================
# PREDICTION
# =========================================================
if submit:

    input_data = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [monetary]
    })

    scaled_data = scaler.transform(input_data)

    cluster = int(
        kmeans.predict(scaled_data)[0]
    )

    st.markdown(
        '<div class="section-title">Analysis Result</div>'
        '<div class="section-description">Hasil cluster berdasarkan karakteristik pelanggan yang dimasukkan.</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3 = st.columns(3)

    m1.metric(
        "Recency",
        f"{recency} days"
    )

    m2.metric(
        "Frequency",
        f"{frequency} transactions"
    )

    m3.metric(
        "Monetary",
        f"{monetary:,.2f}"
    )

    st.write("")

    # CLUSTER 0
    if cluster == 0:

        st.markdown(
            '<div class="result-card result-high">'
            '<div class="result-label high-label">CLUSTER 0 · HIGH VALUE</div>'
            '<div class="result-title">High Value Customer</div>'
            '<div class="result-description">Pelanggan berada pada kelompok bernilai tinggi. Cluster ini secara umum memiliki Recency yang rendah, Frequency yang tinggi, dan Monetary yang tinggi. Pelanggan relatif aktif dan memberikan kontribusi transaksi yang besar.</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="strategy">'
            '<div class="strategy-title">RECOMMENDED STRATEGY</div>'
            '<div class="strategy-text">Pertahankan pelanggan melalui loyalty reward, personalized offer, benefit eksklusif, atau program pelanggan prioritas.</div>'
            '</div>',
            unsafe_allow_html=True
        )

    # CLUSTER 1
    elif cluster == 1:

        st.markdown(
            '<div class="result-card result-regular">'
            '<div class="result-label regular-label">CLUSTER 1 · REGULAR</div>'
            '<div class="result-title">Regular Customer</div>'
            '<div class="result-description">Pelanggan berada pada kelompok dengan aktivitas transaksi menengah. Frequency dan Monetary masih berada di bawah kelompok High Value sehingga masih terdapat potensi peningkatan aktivitas pelanggan.</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="strategy">'
            '<div class="strategy-title">RECOMMENDED STRATEGY</div>'
            '<div class="strategy-text">Tingkatkan engagement melalui voucher, rekomendasi produk, promo berkala, atau program loyalitas.</div>'
            '</div>',
            unsafe_allow_html=True
        )

    # CLUSTER 2
    elif cluster == 2:

        st.markdown(
            '<div class="result-card result-inactive">'
            '<div class="result-label inactive-label">CLUSTER 2 · INACTIVE</div>'
            '<div class="result-title">Inactive Customer</div>'
            '<div class="result-description">Pelanggan berada pada kelompok dengan aktivitas rendah. Cluster ini secara umum memiliki Recency tinggi, Frequency rendah, dan Monetary rendah yang menunjukkan pelanggan sudah cukup lama tidak melakukan transaksi.</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="strategy">'
            '<div class="strategy-title">RECOMMENDED STRATEGY</div>'
            '<div class="strategy-text">Gunakan strategi re-engagement seperti voucher khusus, reminder, diskon, atau campaign win-back.</div>'
            '</div>',
            unsafe_allow_html=True
        )

# =========================================================
# TECHNICAL DETAILS
# =========================================================
st.markdown(
    '<div class="section-title">Model Information</div>'
    '<div class="section-description">Detail teknis mengenai model clustering yang digunakan.</div>',
    unsafe_allow_html=True
)

with st.expander("View Technical Details"):

    st.markdown("""
**Model:** K-Means Clustering  
**Jumlah Cluster:** 3  
**Fitur:** Recency, Frequency, Monetary  
**Scaling:** StandardScaler  
**Metodologi:** CRISP-DM  
**Evaluasi:** Silhouette Score dan Davies-Bouldin Index  

Data telah melalui proses cleaning, transformasi RFM, penanganan outlier, dan standardisasi sebelum digunakan pada model clustering.
""")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    '<div class="custom-footer">'
    '<div>Customer Segmentation · K-Means · RFM</div>'
    '<div>Developed by <span class="author">RIZKYSTARBOY</span> · 2026</div>'
    '</div>',
    unsafe_allow_html=True
)