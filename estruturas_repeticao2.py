"""
MICROATIVIDADE 4 - Estruturas de Repetição: FOR

Descrição:
Este script demonstra o uso de for de duas maneiras:
1. Iterando sobre caracteres de uma string
2. Iterando sobre um intervalo numérico com range()
"""

# ==============================================================================
# FUNÇÃO PARA ITERAR SOBRE CARACTERES
# ==============================================================================


def exibir_caracteres(texto):
    """
    Itera sobre cada caractere de uma string e exibe.

    Args:
        texto (str): String a ser iterada
    """
    print("  Iterando sobre caracteres da string:")
    print()

    for caractere in texto:
        print(f"    Caractere: {caractere}")

    print()


# ==============================================================================
# FUNÇÃO PARA ITERAR SOBRE INTERVALO NUMÉRICO
# ==============================================================================


def exibir_intervalo_numerico(inicio=1, fim=10):
    """
    Itera sobre um intervalo numérico e exibe cada número.

    Args:
        inicio (int): Início do intervalo
        fim (int): Final do intervalo (exclusive)
    """
    print(f"  Iterando sobre números de {inicio} até {fim - 1}:")
    print()

    for numero in range(inicio, fim):
        print(f"    Número do intervalo: {numero}")

    print()


# ==============================================================================
# FUNÇÃO PRINCIPAL
# ==============================================================================


def main():
    """
    Função principal que executa a demonstração da estrutura for.
    """

    print("=" * 70)
    print("MICROATIVIDADE 4 - ESTRUTURAS DE REPETIÇÃO: FOR")
    print("=" * 70)
    print()

    # ============================
    # PARTE 1: For com String
    # ============================
    print("--- Parte 1: FOR com String ---")
    print()

    texto = "Olá, laço for."

    exibir_caracteres(texto)

    # ============================
    # PARTE 2: For com Range
    # ============================
    print("--- Parte 2: FOR com Range ---")
    print()

    exibir_intervalo_numerico(1, 11)

    print("=" * 70)
    print("Fim da Microatividade 4")
    print("=" * 70)


# ==============================================================================
# EXECUÇÃO DO PROGRAMA
# ==============================================================================

if __name__ == "__main__":
    main()
