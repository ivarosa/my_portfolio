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

# ===== CACHED DATA GENERATION =====
@st.cache_data
def generate_dashboard_data():
    """Generate dashboard data once and cache it"""
    dates = pd.date_range('2024-01-01', periods=30)
    return pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(1000, 5000, 30),
        'Visitors': np.random.randint(500, 3000, 30),
        'Conversion': np.random.uniform(0.01, 0.1, 30)
    })

@st.cache_data
def get_skills_data():
    """Return skills data"""
    return pd.DataFrame({
        'Skill': ['Python', 'SQL', 'Tableau', 'PowerBI', 'Excel', 'Statistics'],
        'Proficiency': [95, 90, 85, 80, 95, 85]
    })

@st.cache_data
def get_projects_data():
    """Return projects data with filtering capability"""
    projects = [
        {
            'title': '📊 Proyek 1: E-commerce Sales Analysis',
            'category': 'EDA',
            'year': 2023,
            'description': '''**Deskripsi:**
Melakukan analisis mendalam terhadap data penjualan e-commerce untuk mengidentifikasi 
trend dan peluang pertumbuhan.

**Tools:** Python, Pandas, Matplotlib, Streamlit

**Key Insights:**
- Total sales meningkat 45% YoY
- Kategori Electronics adalah top performer
- Waktu terbaik untuk promo adalah Q4''',
            'has_image': False
        },
        {
            'title': '📈 Proyek 2: Customer Segmentation Dashboard',
            'category': 'Dashboard',
            'year': 2023,
            'description': '''**Deskripsi:**
Interactive dashboard untuk segmentasi pelanggan berdasarkan RFM analysis.

**Tools:** SQL, Tableau, Python

**Key Metrics:**
- 5 customer segments identified
- Average CLV per segment
- Churn risk prediction''',
            'has_image': False
        },
        {
            'title': '🤖 Proyek 3: Churn Prediction Model',
            'category': 'Prediction',
            'year': 2024,
            'description': '''**Deskripsi:**
Machine learning model untuk memprediksi customer churn dengan akurasi 85%.

**Tools:** Python, Scikit-learn, XGBoost

**Performance:**
- Accuracy: 85%
- Precision: 0.82
- Recall: 0.88''',
            'has_image': False
        }
    ]
    return pd.DataFrame(projects)

# ===== UTILITY FUNCTIONS =====
def render_divider():
    """Render a divider line"""
    st.markdown("---")

def render_sidebar_nav():
    """Render sidebar navigation"""
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
    
    return page

def render_profile_image():
    """Render profile image with fallback"""
    try:
        st.image(
            "assets/profpict.png",
            caption="Foto Profil",
            use_container_width=True
        )
    except FileNotFoundError:
        st.warning("⚠️ File 'assets/profpict.png' tidak ditemukan!")
        st.info("💡 Buat folder 'assets/' dan masukkan foto Anda di sana.")

# ===== PAGE: BERANDA =====
def page_beranda():
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
        render_profile_image()
    
    render_divider()
    
    # Statistics
    st.subheader("📈 Statistik Singkat")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Proyek Selesai", 12, "+3")
    col2.metric("Total Dataset", 50, "-5")
    col3.metric("Clients", 8, "+2")
    col4.metric("Tahun Pengalaman", 3, "+1")

# ===== PAGE: TENTANG SAYA =====
def page_tentang_saya():
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
    
    skills_data = get_skills_data()
    
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
def page_proyek():
    st.title("📁 Proyek Saya")
    
    # Filter Proyek
    st.subheader("🔍 Filter Proyek")
    col1, col2 = st.columns(2)
    
    with col1:
        selected_category = st.multiselect(
            "Kategori:",
            ['EDA', 'Dashboard', 'Prediction', 'Visualization'],
            default=['EDA', 'Dashboard', 'Prediction']
        )
    
    with col2:
        selected_year = st.slider(
            "Tahun:",
            2021, 2024, (2021, 2024)
        )
    
    render_divider()
    
    # Load and filter projects
    projects_df = get_projects_data()
    
    # Apply filters
    filtered_projects = projects_df[
        (projects_df['category'].isin(selected_category)) &
        (projects_df['year'] >= selected_year[0]) &
        (projects_df['year'] <= selected_year[1])
    ]
    
    if len(filtered_projects) == 0:
        st.info("📭 Tidak ada proyek yang sesuai dengan filter Anda")
        return
    
    # Display filtered projects
    for idx, project in filtered_projects.iterrows():
        with st.expander(f"{project['title']} ({project['year']})", expanded=(idx==0)):
            col1, col2 = st.columns([2, 1]) if project['has_image'] else (st.container(), None)
            
            with col1:
                st.markdown(project['description'])
                if st.button("🔗 View Project", key=f"project_{idx}"):
                    st.info(f"Link ke project {project['title']} akan dibuka!")
            
            if col2 and project['has_image']:
                with col2:
                    try:
                        st.image(f"assets/project1_ss.png", caption="Project Screenshot")
                    except FileNotFoundError:
                        st.info("📷 Screenshot tidak tersedia")

# ===== PAGE: DASHBOARD =====
def page_dashboard():
    st.title("📊 Interactive Dashboard")
    
    # Use cached data
    dashboard_data = generate_dashboard_data()
    
    # KPI Cards
    st.subheader("📌 KPI Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    total_sales = dashboard_data['Sales'].sum()
    total_visitors = dashboard_data['Visitors'].sum()
    avg_conversion = dashboard_data['Conversion'].mean()
    avg_order_value = dashboard_data['Sales'].mean()
    
    col1.metric("Total Sales", f"Rp {total_sales:,.0f}", "+15%")
    col2.metric("Total Visitors", f"{total_visitors:,}", "+12%")
    col3.metric("Avg Conversion", f"{avg_conversion:.2%}", "+8%")
    col4.metric("Avg Order Value", f"Rp {avg_order_value:,.0f}", "-3%")
    
    render_divider()
    
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
            dashboard_data.groupby('Date').sum(numeric_only=True).reset_index(),
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
def page_contact():
    st.title("📧 Get in Touch")
    
    st.write(
        "Jika Anda tertarik untuk berkolaborasi atau memiliki pertanyaan, "
        "silakan hubungi saya melalui form di bawah!"
    )
    
    render_divider()
    
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
    
    render_divider()
    
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

# ===== MAIN APP =====
def main():
    page = render_sidebar_nav()
    
    if page == "🏠 Beranda":
        page_beranda()
    elif page == "👤 Tentang Saya":
        page_tentang_saya()
    elif page == "📁 Proyek":
        page_proyek()
    elif page == "📊 Dashboard":
        page_dashboard()
    elif page == "📧 Contact":
        page_contact()

if __name__ == "__main__":
    main()