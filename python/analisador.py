
import streamlit as st
import re
from collections import Counter

# Configuração inicial
st.title("Analisador de Texto")
st.write("Forneça um texto ou carregue um arquivo para análise.")

# Entrada do usuário
input_option = st.radio("Como você deseja fornecer o texto?", ("Digite diretamente", "Carregar arquivo"))

if input_option == "Digite diretamente":
    texto = st.text_area("Digite o texto aqui:", height=200, placeholder="Insira seu texto...")
else:
    uploaded_file = st.file_uploader("Carregue um arquivo de texto:", type=["txt"])
    if uploaded_file is not None:
        texto = uploaded_file.read().decode("utf-8")
    else:
        texto = ""

if texto:
    # Análise do texto
    st.subheader("Estatísticas do Texto")
    
    # Contar palavras
    palavras = re.findall(r'\b\w+\b', texto.lower())  # Lista de palavras (case insensitive)
    num_palavras = len(palavras)
    
    # Contar frases
    frases = re.split(r'[.!?]', texto)
    frases = [frase.strip() for frase in frases if frase.strip()]
    num_frases = len(frases)
    
    # Frequência de palavras
    frequencia_palavras = Counter(palavras)
    palavra_mais_frequente, freq_mais_frequente = frequencia_palavras.most_common(1)[0]
    
    # Contagem de caracteres por tipo
    letras = re.findall(r'[a-zA-Z]', texto)
    numeros = re.findall(r'\d', texto)
    pontuacoes = re.findall(r'[^\w\s]', texto)
    outros = re.findall(r'[^\w]', texto)  # Caracteres que não são palavras
    
    # Exibição dos resultados
    st.write(f"- **Número total de palavras:** {num_palavras}")
    st.write(f"- **Número total de frases:** {num_frases}")
    st.write(f"- **Palavra mais frequente:** '{palavra_mais_frequente}' (aparece {freq_mais_frequente} vezes)")
    
    # Frequência de palavras
    st.subheader("Frequência de Palavras")
    st.write("As 10 palavras mais frequentes são:")
    st.write(dict(frequencia_palavras.most_common(10)))
    
    # Contagem de caracteres
    st.subheader("Contagem de Tipos de Caracteres")
    st.write(f"- **Letras:** {len(letras)}")
    st.write(f"- **Números:** {len(numeros)}")
    st.write(f"- **Pontuações:** {len(pontuacoes)}")
    st.write(f"- **Outros caracteres:** {len(outros)}")
else:
    st.info("Por favor, forneça um texto ou carregue um arquivo para começar a análise.")
