
import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Sistema Respiratorio", page_icon="🫁", layout="wide")

# Sidebar con navegación
seccion = st.sidebar.selectbox("Navegación", ["🏠 Inicio", "📖 Aprende", "❓ Preguntas", "🏁 Resultado"])

# --- Sección: INICIO ---
if seccion == "🏠 Inicio":
    st.markdown("<h1 style='text-align: center; color: #0077B6;'>🫁 Anatomía del Sistema Respiratorio</h1>", unsafe_allow_html=True)
    st.image("pulmones.png", width=300)
    st.markdown("""
    Bienvenido a esta aplicación educativa sobre el sistema respiratorio humano. 
    Aquí podrás aprender sobre la estructura de los pulmones, su función y cómo cuidarlos.
    Además, podrás responder un quiz para evaluar lo que has aprendido.
    """)
    st.markdown("---")
    st.info("Usa el menú lateral para navegar por las secciones.")

# --- Sección: APRENDER ---
elif seccion == "📖 Aprende":
    st.markdown("## 📚 Información Educativa")
    st.markdown("### ¿Qué son los pulmones?")
    st.markdown("""
    Los pulmones son órganos respiratorios que se encuentran a ambos lados del mediastino, rodeados por las cavidades pleurales.
    Son responsables del intercambio de gases entre el aire y la sangre. Están protegidos por la caja torácica y diferenciados en 
    pulmón derecho (3 lóbulos) y pulmón izquierdo (2 lóbulos).
    """)
    st.markdown("### Funciones principales")
    st.markdown("- Intercambio de oxígeno y dióxido de carbono")
    st.markdown("- Regulación del equilibrio ácido-base")
    st.markdown("- Filtrado de pequeños trombos")
    st.markdown("- Conversión de angiotensina I en II")
    st.markdown("### Cómo cuidarlos")
    st.markdown("- No fumar")
    st.markdown("- Hacer ejercicio regularmente")
    st.markdown("- Evitar contaminantes")
    st.markdown("- Alimentación saludable")
    st.markdown("- Higiene adecuada y controles médicos")

# --- Sección: PREGUNTAS ---
elif seccion == "❓ Preguntas":
    st.markdown("## ❓ Quiz del Sistema Respiratorio")
    st.markdown("Responde las siguientes preguntas para poner a prueba lo que aprendiste:")

    # Preguntas (simples para ejemplo, luego podemos mejorar)
    preguntas = [
        {"pregunta": "¿Cuál es la función principal de los pulmones?", "opciones": ["Digestión", "Respiración", "Filtración"], "respuesta": "Respiración"},
        {"pregunta": "¿Cuántos lóbulos tiene el pulmón derecho?", "opciones": ["2", "3", "4"], "respuesta": "3"},
        {"pregunta": "¿Qué membrana recubre los pulmones?", "opciones": ["Pleura", "Peritoneo", "Pericardio"], "respuesta": "Pleura"},
        {"pregunta": "¿Qué bronquios llevan aire a cada pulmón?", "opciones": ["Primarios", "Terminales", "Alveolos"], "respuesta": "Primarios"},
        {"pregunta": "¿Qué órgano se encuentra entre ambos pulmones?", "opciones": ["Estómago", "Corazón", "Hígado"], "respuesta": "Corazón"},
    ]

    # Repetir preguntas para llegar a 15
    preguntas = preguntas * 3  # 5 x 3 = 15

    score = 0
    for i, p in enumerate(preguntas, 1):
        st.markdown(f"**{i}. {p['pregunta']}**")
        respuesta = st.radio(f"Opciones {i}", p['opciones'], key=f"pregunta_{i}")
        if respuesta == p['respuesta']:
            score += 1

    st.session_state["score"] = score

# --- Sección: RESULTADO ---
elif seccion == "🏁 Resultado":
    if "score" in st.session_state:
        st.markdown("## 🏁 Resultado final")
        st.success(f"Obtuviste {st.session_state['score']} de 15 respuestas correctas. ¡Bien hecho! 🥳")
        if st.session_state['score'] >= 12:
            st.balloons()
            st.markdown("¡Excelente conocimiento del sistema respiratorio!")
        elif st.session_state['score'] >= 8:
            st.markdown("¡Vas muy bien! Sigue aprendiendo 💪")
        else:
            st.markdown("¡No te preocupes! Puedes volver a intentarlo cuando quieras. 😊")
    else:
        st.warning("Primero completa las preguntas para ver tu resultado.")
