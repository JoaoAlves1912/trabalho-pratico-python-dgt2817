"""
TRABALHO PRÁTICO FINAL - Calculadora v2

Descrição:
Este script implementa uma calculadora interativa operada via terminal. 
O sistema recebe entradas numéricas e a operação matemática desejada, 
valida os dados, processa o cálculo de forma modularizada (com tratamento 
específico para divisão por zero) e mantém um laço de execução contínuo 
até que o usuário decida encerrar.
"""

saida = ""


def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2


def calculadora(num1, num2, operacao):
    if operacao == "+" or operacao.lower() == "adicao":
        resultado = adicao(num1, num2)
    elif operacao == "-" or operacao.lower() == "subtracao":
        resultado = subtracao(num1, num2)
    elif operacao == "*" or operacao.lower() == "multiplicacao":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/" or operacao.lower() == "divisao":
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida. Verifique o sinal ou nome digitado."

    return resultado


while saida.lower() != "n":
    print("\n--- Nova Operação ---")

    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))
        operador = input(
            "Digite a operação desejada (+, -, *, / ou o nome da operação): "
        )

        resultado_final = calculadora(primeiro_numero, segundo_numero, operador)

        print(f"\nResultado da operação: {resultado_final}")

    except ValueError:
        print("\nErro: Você deve digitar valores numéricos válidos para os cálculos.")

    print("-" * 21)
    saida = input("Deseja continuar executando o programa? (S/N): ")
