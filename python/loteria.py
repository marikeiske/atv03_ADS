
import streamlit as st
import random

# Configuração inicial do aplicativo
st.title("Simulador de Jogo de Loteria")
st.write("Escolha o tipo de loteria, insira seus números da sorte e veja os resultados!")

# Dicionário de configurações das loterias
loterias = {
    "Mega Sena": {"intervalo": (1, 60), "quantidade": 6},
    "Quina": {"intervalo": (1, 80), "quantidade": 5},
    "Lotofácil": {"intervalo": (1, 25), "quantidade": 15},
}

# Seleção do tipo de loteria
tipo_loteria = st.selectbox("Escolha o tipo de loteria", loterias.keys())
config = loterias[tipo_loteria]

# Mostrar as configurações escolhidas
st.write(f"Você escolheu **{tipo_loteria}**:")
st.write(f"- Intervalo de números: {config['intervalo'][0]} a {config['intervalo'][1]}")
st.write(f"- Quantidade de números: {config['quantidade']}")

# Entrada dos números do usuário
st.subheader("Insira seus números da sorte:")
numeros_usuario = st.text_input(
    f"Digite {config['quantidade']} números separados por vírgula:",
    placeholder="Ex: 5, 12, 23, 34, 45, 56"
)

# Botão para gerar os números sorteados
if st.button("Sortear números"):
    try:
        # Processar entrada do usuário
        numeros_usuario = list(map(int, numeros_usuario.split(",")))

        # Validar quantidade de números
        if len(numeros_usuario) != config["quantidade"]:
            st.error(f"Você deve digitar exatamente {config['quantidade']} números.")
        # Validar intervalo dos números
        elif any(
            num < config["intervalo"][0] or num > config["intervalo"][1]
            for num in numeros_usuario
        ):
            st.error(
                f"Todos os números devem estar entre {config['intervalo'][0]} e {config['intervalo'][1]}."
            )
        # Caso a entrada seja válida
        else:
            # Gerar números sorteados
            random.seed()  # Inicializar a semente do gerador de números aleatórios
            numeros_sorteados = random.sample(
                range(config["intervalo"][0], config["intervalo"][1] + 1),
                config["quantidade"],
            )

            # Comparar os números
            acertos = set(numeros_usuario) & set(numeros_sorteados)

            # Exibir resultados
            st.subheader("Resultados:")
            st.write(f"Números sorteados: {sorted(numeros_sorteados)}")
            st.write(f"Seus números: {sorted(numeros_usuario)}")
            st.write(f"Você acertou {len(acertos)} número(s): {sorted(acertos)}")

            # Mensagem de parabéns
            if len(acertos) == config["quantidade"]:
                st.success("Parabéns! Você acertou todos os números!")
    except ValueError:
        st.error("Por favor, insira apenas números separados por vírgula.")
