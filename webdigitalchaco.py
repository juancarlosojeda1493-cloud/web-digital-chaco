import streamlit as st

# Configuración estética
st.set_page_config(page_title="Digital Chaco", layout="centered")

# Contenido de la web
st.title("🌐 Web Digital Chaco")
st.subheader("Bienvenidos a nuestra plataforma interactiva")

st.write("---")
st.write("Esta página está siendo construida con Python para brindar soluciones digitales en la región.")

# Un botón interactivo para probar
if st.button("Hacer clic aquí"):
    st.balloons()
    st.success("¡Funciona perfectamente!")