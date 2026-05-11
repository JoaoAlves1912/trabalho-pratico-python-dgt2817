"""
MICROATIVIDADE 5 - Funções Básicas em Python

Descrição:
Este script demonstra como criar uma função simples, armazenar dados
em variáveis dentro dela e exibir o conteúdo.
"""

# ==============================================================================
# FUNÇÃO PARA IMPRIMIR UMA VARIÁVEL
# ==============================================================================


def imprimir_variavel():
    """
    Função que demonstra como trabalhar com variáveis e exibir conteúdo.

    Comportamento:
        - Cria uma variável chamada 'texto'
        - Atribui um valor a ela
        - Exibe o conteúdo da variável
    """

    texto = "Olá, funções em Python"

    print(f"  {texto}")


# ==============================================================================
# FUNÇÃO PRINCIPAL
# ==============================================================================


def main():
    """
    Função main que organiza a execução do programa.

    Responsabilidades:
        - Exibir informações do programa
        - Chamar as funções necessárias
        - Gerenciar o fluxo de execução
    """

    # Exibe título do programa
    print("=" * 70)
    print("MICROATIVIDADE 5 - FUNÇÕES BÁSICAS EM PYTHON")
    print("=" * 70)
    print()

    print("--- Chamando a função imprimir_variavel() ---")
    print()

    imprimir_variavel()

    print()
    print("=" * 70)
    print("Fim da Microatividade 5")
    print("=" * 70)


# ==============================================================================
# EXECUÇÃO DO PROGRAMA
# ==============================================================================

if __name__ == "__main__":
    main()
