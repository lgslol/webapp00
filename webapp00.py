# myFirstStreamlitApp.py
  
#import the library
import streamlit as st

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Leozn3Kpa")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("O mestre do AZ")
         
# Use st.write("") para adicionar um texto ao seu Web app
st.write("0 recuperações")

st.write("Melhor que o cecconello no enem de Mat")

st.write("Progamador profissional desde 28/04/2023")

# pede ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(numero, "é par")
else:
    print(numero, "é ímpar")

