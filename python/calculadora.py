
import streamlit as st
import math
import matplotlib.pyplot as plt

# Funções auxiliares
def calcular_terceiro_lado(a, b):
    return math.sqrt(a**2 + b**2)

def calcular_lados_e_angulos(a=None, b=None, c=None, angle=None):
    resultados = {}
    if a and b:
        c = calcular_terceiro_lado(a, b)
        angle_a = math.degrees(math.atan(a / b))
        angle_b = math.degrees(math.atan(b / a))
        angle_c = 90.0
        resultados = {'a': a, 'b': b, 'c': c, 'angle_a': angle_a, 'angle_b': angle_b, 'angle_c': angle_c}
    elif a and angle:
        angle_rad = math.radians(angle)
        b = a / math.tan(angle_rad)
        c = calcular_terceiro_lado(a, b)
        angle_b = 90.0 - angle
        angle_c = 90.0
        resultados = {'a': a, 'b': b, 'c': c, 'angle_a': angle, 'angle_b': angle_b, 'angle_c': angle_c}
    elif b and angle:
        angle_rad = math.radians(angle)
        a = b * math.tan(angle_rad)
        c = calcular_terceiro_lado(a, b)
        angle_a = 90.0 - angle
        angle_c = 90.0
        resultados = {'a': a, 'b': b, 'c': c, 'angle_a': angle_a, 'angle_b': angle, 'angle_c': angle_c}
    return resultados

def desenhar_triangulo(a, b, c):
    fig, ax = plt.subplots()
    ax.plot([0, b, 0, 0], [0, 0, a, 0], 'b-')
    ax.text(b / 2, -0.5, f"b = {b:.2f}", ha='center')
    ax.text(-0.5, a / 2, f"a = {a:.2f}", va='center')
    ax.text(b / 2, a / 2, f"c = {c:.2f}", va='center', color='red')
    ax.set_xlim(-1, b + 1)
    ax.set_ylim(-1, a + 1)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    return fig

st.title("Calculadora de Triângulo Retângulo")
st.write("Calcule os lados e ângulos de um triângulo retângulo e veja a visualização.")

st.sidebar.header("Entradas")
option = st.sidebar.selectbox("Escolha uma opção:", ["Dois lados", "Um lado e um ângulo"])
if option == "Dois lados":
    lado1 = st.sidebar.number_input("Comprimento do primeiro lado (a):", min_value=0.01, step=0.1)
    lado2 = st.sidebar.number_input("Comprimento do segundo lado (b):", min_value=0.01, step=0.1)
    if st.sidebar.button("Calcular"):
        resultados = calcular_lados_e_angulos(a=lado1, b=lado2)
        if resultados:
            st.subheader("Resultados")
            st.write(f"Lado a: {resultados['a']:.2f}")
            st.write(f"Lado b: {resultados['b']:.2f}")
            st.write(f"Hipotenusa c: {resultados['c']:.2f}")
            st.write(f"Ângulo A: {resultados['angle_a']:.2f}°")
            st.write(f"Ângulo B: {resultados['angle_b']:.2f}°")
            st.write(f"Ângulo C: {resultados['angle_c']:.2f}°")
            fig = desenhar_triangulo(resultados['a'], resultados['b'], resultados['c'])
            st.pyplot(fig)

elif option == "Um lado e um ângulo":
    lado = st.sidebar.number_input("Comprimento de um lado (a ou b):", min_value=0.01, step=0.1)
    angulo = st.sidebar.number_input("Ângulo (em graus):", min_value=0.01, max_value=89.99, step=0.1)
    if st.sidebar.button("Calcular"):
        resultados = calcular_lados_e_angulos(a=lado, angle=angulo)
        if resultados:
            st.subheader("Resultados")
            st.write(f"Lado a: {resultados['a']:.2f}")
            st.write(f"Lado b: {resultados['b']:.2f}")
            st.write(f"Hipotenusa c: {resultados['c']:.2f}")
            st.write(f"Ângulo A: {resultados['angle_a']:.2f}°")
            st.write(f"Ângulo B: {resultados['angle_b']:.2f}°")
            st.write(f"Ângulo C: {resultados['angle_c']:.2f}°")
            fig = desenhar_triangulo(resultados['a'], resultados['b'], resultados['c'])
            st.pyplot(fig)
