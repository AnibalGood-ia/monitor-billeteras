python
import streamlit as st
import pandas as pd

# Configuración de la página móvil
st.set_page_config(page_title="Monitor Rendimientos AR", page_icon="💰", layout="centered")

# Título y descripción
st.title("🇦🇷 Monitor de Billeteras Virtuales")
st.caption("Compará las Tasas Nominales Anuales (TNA) en tiempo real para hacer rendir tu sueldo diario.")

# --- ESPACIO PARA PUBLICIDAD (BANNER SUPERIOR) ---
st.markdown(
    """
    <div style="background-color: #f0f2f6; padding: 10px; text-align: center; border-radius: 5px; margin-bottom: 20px;">
        <span style="color: #555; font-size: 12px;">ANUNCIO</span>
        <p style="margin: 0; font-weight: bold; color: #1e3d59;">¡Abrí tu cuenta hoy y empezá a ganar!</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Datos simulación del mercado (estos datos se actualizarán dinámicamente más adelante)
datos_billeteras = [
    {"Billetera": "Naranja X", "TNA": 42.0, "Monto Máximo con Tasa": "Hasta $600.000"},
    {"Billetera": "Personal Pay (Nivel 3)", "TNA": 39.5, "Monto Máximo con Tasa": "Sin límite"},
    {"Billetera": "Mercado Pago", "TNA": 37.2, "Monto Máximo con Tasa": "Sin límite"},
    {"Billetera": "Ualá (Uilo)", "TNA": 36.0, "Monto Máximo con Tasa": "Sin límite"},
]

df = pd.DataFrame(datos_billeteras)

# Formatear la columna TNA para mostrar el símbolo %
df_mostrar = df.copy()
df_mostrar["TNA"] = df_mostrar["TNA"].apply(lambda x: f"{x}%")

# Mostrar la tabla comparativa
st.subheader("📊 Ranking de Tasas de Hoy")
st.dataframe(df_mostrar, use_container_width=True, hide_index=True)

# Calculadora de ganancias
st.subheader("🧮 Calculadora de Rendimiento Diario")
monto = st.number_input("Ingresá cuántos pesos querés depositar ($):", min_value=0, value=100000, step=10000)

if monto > 0:
    resultados = []
    for b in datos_billeteras:
        # Cálculo de rendimiento diario aproximado (Monto * TNA / 100 / 365 días)
        ganancia_diaria = (monto * (b["TNA"] / 100)) / 365
        ganancia_mensual = ganancia_diaria * 30
        resultados.append({
            "Billetera": b["Billetera"],
            "Ganancia Diaria": f"$ {ganancia_diaria:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "Ganancia Mensual (30 días)": f"$ {ganancia_mensual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        })
    
    df_res = pd.DataFrame(resultados)
    st.table(df_res)

# --- ESPACIO PARA PUBLICIDAD (BANNER INFERIOR) ---
st.markdown(
    """
    <div style="background-color: #fff3cd; padding: 10px; text-align: center; border-radius: 5px; margin-top: 30px; border: 1px solid #ffeeba;">
        <span style="color: #856404; font-size: 12px;">ANUNCIO RECOMENDADO</span>
        <p style="margin: 0; font-weight: bold; color: #856404;">¿Buscás una tarjeta de crédito gratis? Hacé clic acá.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.info("💡 Consejo: Las tasas pueden variar diariamente según las regulaciones del Banco Central.")
