iimport streamlit as st

# 1. Configuración de la página (esto debe ir PRIMERO)
st.set_page_config(
    page_title="Web Digital Chaco | Portal Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_stdio=True)

# --- CABECERA ---
st.title("🌐 Portal Web Digital Chaco")
st.markdown("### Soluciones Tecnológicas y Entretenimiento Familiar")
st.write("---")

# --- SECCIÓN DE PROYECTOS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.header("📺 Streaming")
    st.info("Accede a las señales de Argentina y la región.")
    # Reemplaza 'TU_URL_AQUI' por el link real de tu IPTV
    st.link_button("Ir a IPTV CHACO", "https://tu-url-de-iptv.streamlit.app")

with col2:
    st.header("🎮 Entretenimiento")
    st.success("Desafíos y juegos para competir en familia.")
    # Reemplaza con el link de tu juego de adivinanzas
    st.link_button("JUGAR: RED FAMILIAR", "https://juego-adivinanzas-familia.streamlit.app")

with col3:
    st.header("📊 Gestión")
    st.warning("Sistema de logística y distribución regional.")
    # Aquí puedes poner el link a tu sistema de Distribuidora si está online
    st.link_button("Acceso Distribuidora", "https://distribuidora-chaco.streamlit.app")

# --- PIE DE PÁGINA ---
st.write("---")
st.caption("© 2026 Web Digital Chaco - Desarrollado con Python & Streamlit")
