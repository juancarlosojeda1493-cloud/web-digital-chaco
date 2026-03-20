import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA (Debe ser la primera instrucción)
st.set_page_config(
    page_title="Web Digital Chaco | Portal Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ESTILO CSS PERSONALIZADO (Para que se vea como una App profesional)
st.markdown("""
    <style>
    /* Fondo de la aplicación */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Estilo general para todos los botones de enlace */
    div.stButton > button, div.stLinkButton > a {
        width: 100% !important;
        border-radius: 12px !important;
        height: 4em !important;
        line-height: 2.5em !important;
        font-weight: bold !important;
        text-decoration: none !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        border: none !important;
        transition: 0.3s;
    }

    /* Colores específicos para cada botón para que resalten */
    /* Botón IPTV (Azul) */
    div.col1-style a {
        background-color: #007bff !important;
        color: white !important;
    }
    
    /* Botón Juegos (Verde) */
    div.col2-style a {
        background-color: #28a745 !important;
        color: white !important;
    }
    
    /* Botón Gestión (Naranja) */
    div.col3-style a {
        background-color: #fd7e14 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("🌐 Portal Web Digital Chaco")
st.markdown("#### Central de Proyectos y Soluciones Tecnológicas")
st.write("---")

# --- SECCIÓN DE PROYECTOS (Organizado en columnas) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="col1-style">', unsafe_allow_html=True)
    st.header("📺 Streaming")
    st.info("Accede a las señales de Argentina y la región Nordeste.")
    # REEMPLAZA CON TU URL REAL DE IPTV
    st.link_button("ACCEDER A IPTV CHACO", "https://tu-url-iptv.streamlit.app")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="col2-style">', unsafe_allow_html=True)
    st.header("🎮 Juegos")
    st.success("Desafíos familiares: RED FAMILIAR Championship.")
    # REEMPLAZA CON TU URL REAL DE JUEGOS
    st.link_button("¡A JUGAR AHORA!", "https://juego-adivinanzas-familia.streamlit.app")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="col3-style">', unsafe_allow_html=True)
    st.header("📊 Gestión")
    st.warning("Sistema de logística para Distribuidora Chaco.")
    # REEMPLAZA CON TU URL REAL DE DISTRIBUIDORA
    st.link_button("SISTEMA DE LOGÍSTICA", "https://distribuidora-chaco.streamlit.app")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN INFERIOR / INFORMACIÓN ---
st.write("---")
with st.expander("ℹ️ Información del Desarrollador"):
    st.write("""
    Este portal centraliza las herramientas digitales desarrolladas en Python. 
    Optimizado para acceso rápido desde dispositivos móviles y gestión en tiempo real.
    """)

# --- PIE DE PÁGINA ---
st.caption("© 2026 Web Digital Chaco | Resistencia, Chaco, Argentina")
