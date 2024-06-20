import streamlit as st

with st.sidebar:
    st.title("calculadora IMC")

    st.header("IMC - Indice de Massa Corporal")

st.title("Calculadora")

peso = st.number_input(label="digite o seu peso em Kg", min_value=0.0)

altura = st.number_input(label="digite a sua altura em metros", min_value=0.0)

if st.button("Calcular"):

    imc = peso / (altura ** 2)
    imc = round(imc, 2)

    st.write(f"Seu IMC é {imc}")
