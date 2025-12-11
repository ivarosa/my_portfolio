import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# ===== PAGE CONFIGURATION =====
st.set_page_config(
    page_title="Portfolio Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== SIDEBAR NAVIGATION =====
st.sidebar.markdown("# 📍 Navigasi")
page = st.sidebar.radio(
    "Pilih halaman:",
    ["🏠 Beranda", "👤 Tentang Saya", "📁 Proyek", "📊 Dashboard", "📧 Contact"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    ### 🔗 Media Sosial
    - [LinkedIn](https://linkedin.com)
    - [GitHub](https://github.com)
    - [Email](mailto:email@example.com)
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Portfolio Saya")

# ===== PAGE: BERANDA =====
if page == "🏠 Beranda":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("🌟 Selamat Datang!")
        st.markdown(
            """
            Halo, nama saya **Muhammad Rizki**. Saya adalah seorang **Data Analyst** 
            yang passionate tentang mengubah data menjadi insights yang actionable.
            
            Dalam portfolio ini, saya menampilkan beberapa proyek data yang telah saya kerjakan,
            dari exploratory data analysis hingga business intelligence dashboard.
            """
        )
        st.write(" ")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("📥 Download CV"):
                st.success("CV berhasil diunduh!")
        with col_btn2:
            if st.button("💬 Hubungi Saya"):
                st.info("Silakan scroll ke halaman Contact!")
    
    with col2:
        try:
            st.image(
                "assets/profpict.png",     # ← Ubah ke nama file Anda!
                caption="Foto Profil",
                use_container_width=True
            )
        except FileNotFoundError:
            st.warning("⚠️ File 'assets/profpict.jpg' tidak ditemukan!")
            st.info("💡 Buat folder 'assets/' dan masukkan foto Anda di sana.")
    
    st.markdown("---")
    
    # Statistics
    st.subheader("📈 Statistik Singkat")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Proyek Selesai", 12, "+3")
    col2.metric("Total Dataset", 50, "-5")
    col3.metric("Clients", 8, "+2")
    col4.metric("Tahun Pengalaman", 3, "+1")

# ===== PAGE: TENTANG SAYA =====
elif page == "👤 Tentang Saya":
    st.title("👤 Tentang Saya")
    
    st.subheader("Latar Belakang")
    st.write(
        """
        Saya adalah data analyst dengan pengalaman 3+ tahun di industri e-commerce dan fintech.
        Saya berspesialisasi dalam:
        - **Data Exploration & Cleaning**: Menggunakan Pandas & NumPy
        - **Data Visualization**: Tableau, PowerBI, Streamlit
        - **Statistical Analysis**: A/B Testing, Hypothesis Testing
        - **Business Intelligence**: Dashboard development, KPI tracking
        """
    )
    
    st.subheader("🛠️ Technical Skills")
    
    skills_data = pd.DataFrame({
        'Skill': ['Python', 'SQL', 'Tableau', 'PowerBI', 'Excel', 'Statistics'],
        'Proficiency': [95, 90, 85, 80, 95, 85]
    })
    
    fig = px.bar(
        skills_data,
        x='Skill',
        y='Proficiency',
        title='Tingkat Keahlian',
        color='Proficiency',
        color_continuous_scale='Viridis',
        text='Proficiency'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("📚 Sertifikasi")
    cert_col1, cert_col2, cert_col3 = st.columns(3)
    cert_col1.markdown(
        """
        **Google Analytics Certification**
        ✅ Certified, 2022
        """
    )
    cert_col2.markdown(
        """
        **SQL for Data Analysis**
        ✅ Certified, 2021
        """
    )
    cert_col3.markdown(
        """
        **Data Visualization with Tableau**
        ✅ Certified, 2023
        """
    )

# ===== PAGE: PROYEK =====
elif page == "📁 Proyek":
    st.title("📁 Proyek Saya")
    
    # Filter Proyek
    st.subheader("🔍 Filter Proyek")
    col1, col2 = st.columns(2)
    
    with col1:
        selected_category = st.multiselect(
            "Kategori:",
            ['EDA', 'Dashboard', 'Prediction', 'Visualization'],
            default=['EDA', 'Dashboard']
        )
    
    with col2:
        selected_year = st.slider(
            "Tahun:",
            2021, 2024, (2022, 2024)
        )
    
    st.markdown("---")
    
    # Project 1
    with st.expander("📊 Proyek 1: E-commerce Sales Analysis", expanded=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(
                """
                **Deskripsi:**
                Melakukan analisis mendalam terhadap data penjualan e-commerce untuk mengidentifikasi 
                trend dan peluang pertumbuhan.
                
                **Tools:** Python, Pandas, Matplotlib, Streamlit
                
                **Key Insights:**
                - Total sales meningkat 45% YoY
                - Kategori Electronics adalah top performer
                - Waktu terbaik untuk promo adalah Q4
                """
            )
            if st.button("🔗 View Project", key="project1"):
                st.info("Link ke project akan dibuka!")
        
        with col2:
            st.image(
                "assets/project1_ss.png",
                caption="Project Screenshot"
            )
    
    # Project 2
    with st.expander("📈 Proyek 2: Customer Segmentation Dashboard"):
        st.markdown(
            """
            **Deskripsi:**
            Interactive dashboard untuk segmentasi pelanggan berdasarkan RFM analysis.
            
            **Tools:** SQL, Tableau, Python
            
            **Key Metrics:**
            - 5 customer segments identified
            - Average CLV per segment
            - Churn risk prediction
            """
        )
    
    # Project 3
    with st.expander("🤖 Proyek 3: Churn Prediction Model"):
        st.markdown(
            """
            **Deskripsi:**
            Machine learning model untuk memprediksi customer churn dengan akurasi 85%.
            
            **Tools:** Python, Scikit-learn, XGBoost
            
            **Performance:**
            - Accuracy: 85%
            - Precision: 0.82
            - Recall: 0.88
            """
        )

# ===== PAGE: DASHBOARD =====
elif page == "📊 Dashboard":
    st.title("📊 Interactive Dashboard")
    
    # Generate sample data
    dates = pd.date_range('2024-01-01', periods=30)
    dashboard_data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(1000, 5000, 30),
        'Visitors': np.random.randint(500, 3000, 30),
        'Conversion': np.random.uniform(0.01, 0.1, 30)
    })
    
    # KPI Cards
    st.subheader("📌 KPI Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(
        "Total Sales",
        f"Rp {dashboard_data['Sales'].sum():,.0f}",
        f"+{np.random.randint(5, 20)}%"
    )
    col2.metric(
        "Total Visitors",
        f"{dashboard_data['Visitors'].sum():,}",
        f"+{np.random.randint(5, 20)}%"
    )
    col3.metric(
        "Avg Conversion",
        f"{dashboard_data['Conversion'].mean():.2%}",
        f"+{np.random.randint(1, 10)}%"
    )
    col4.metric(
        "Avg Order Value",
        f"Rp {dashboard_data['Sales'].mean():,.0f}",
        f"-{np.random.randint(1, 10)}%"
    )
    
    st.markdown("---")
    
    # Charts
    st.subheader("📈 Sales Trend")
    fig1 = px.line(
        dashboard_data,
        x='Date',
        y='Sales',
        title='Daily Sales',
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig2 = px.bar(
            dashboard_data.groupby('Date').sum().reset_index(),
            x='Date',
            y='Visitors',
            title='Daily Visitors'
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        fig3 = px.scatter(
            dashboard_data,
            x='Visitors',
            y='Sales',
            size='Conversion',
            title='Visitors vs Sales',
            color='Conversion',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig3, use_container_width=True)

# ===== PAGE: CONTACT =====
elif page == "📧 Contact":
    st.title("📧 Get in Touch")
    
    st.write(
        "Jika Anda tertarik untuk berkolaborasi atau memiliki pertanyaan, "
        "silakan hubungi saya melalui form di bawah!"
    )
    
    st.markdown("---")
    
    # Contact Form
    with st.form("contact_form"):
        nama = st.text_input("Nama Lengkap")
        email = st.text_input("Email")
        subject = st.selectbox(
            "Subjek:",
            ['Project Inquiry', 'Collaboration', 'General Question', 'Others']
        )
        message = st.text_area("Pesan:", height=150)
        submitted = st.form_submit_button("📤 Send Message")
        
        if submitted:
            if nama and email and message:
                st.success(
                    f"✅ Terima kasih, {nama}! Pesan Anda telah dikirim. "
                    "Saya akan menghubungi Anda dalam 24 jam."
                )
            else:
                st.error("❌ Mohon isi semua field!")
    
    st.markdown("---")
    
    st.subheader("🔗 Kontak Lainnya")
    col1, col2, col3 = st.columns(3)
    
    col1.write(
        """
        **Email**
        📧 [email@example.com](mailto:email@example.com)
        """
    )
    col2.write(
        """
        **LinkedIn**
        💼 [linkedin.com/in/username](https://linkedin.com)
        """
    )
    col3.write(
        """
        **GitHub**
        🐙 [github.com/username](https://github.com)
        """
    )