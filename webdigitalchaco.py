import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="LU1GAS-10 | Monitor de Radio",
    page_icon="📡",
    layout="wide"
)

# --- ESTILO TIPO CONSOLA DE RADIO ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .callsign-header {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        text-align: center;
    }
    .metric-card {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #464855;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA OFICIAL ---
st.markdown('<div class="callsign-header">', unsafe_allow_html=True)
st.title("📟 Estación LU1GAS - Juan Carlos")
st.write("📍 Resistencia, Chaco, Argentina | Altura: 54m | Nodo: LU1GAS-10")
st.markdown('</div>', unsafe_allow_html=True)
st.write("---")

# --- MONITOR DE PROPAGACIÓN Y ESTACIONES ---
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("☀️ Propagación HF/VHF")
    # Widget de propagación externa
    st.image("https://www.hamqsl.com/solar101vhf.php", caption="Estado de las Bandas en Tiempo Real")
    
    st.write("---")
    st.subheader("🕵️ Ver Estaciones en el Aire")
    st.info("Consulta quiénes están activos en la zona:")
    
    # Botón para buscar estaciones cercanas a tu ubicación
    st.link_button("📻 Estaciones cerca de Resistencia", 
                  "https://aprs.fi/#!addr=Resistencia%2C%20Chaco%2C%20Argentina")
    
    st.link_button("📋 Listado de Tráfico Reciente", 
                  "https://aprs.fi/info/a/LU1GAS-10")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("📍 Radar APRS Regional")
    # Mapa interactivo centrado en tu área de influencia
    # A 54 metros, verás estaciones de Corrientes, Formosa y norte de Santa Fe
    components.iframe("https://aprs.fi/#!addr=Resistencia%2C%20Chaco%2C%20Argentina", height=600)

# --- SECCIÓN DE EQUIPOS ---
st.write("---")
expander = st.expander("🛠️ Configuración Técnica de la Estación")
expander.write(f"""
- **Transmisores:** Yaesu FT-1900 (VHF) / Yaesu FT-5DR (Digital C4FM)
- **Antena:** Ringo VHF en balcón (54 metros de altura)
- **iGate:** Puente ESP32 conectado a Notebook via USB-Serial
- **Red:** Conectado a Servidores APRS-IS Tier 2
""")

# --- PIE DE PÁGINA ---
st.caption("© 2026 Web Digital Chaco | 73's Cordiales de LU1GAS Juan Carlos")
