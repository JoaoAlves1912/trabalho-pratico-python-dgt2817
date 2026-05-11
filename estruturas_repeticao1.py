"""
MICROATIVIDADE 3 - Estruturas de Repetição: WHILE


Descrição:
Este script solicita números ao usuário em um laço while e exibe
cada número digitado. O programa encerra quando o usuário digita 0.
"""

# ==============================================================================
# FUNÇÃO PARA VALIDAR ENTRADA DO USUÁRIO
# ==============================================================================

def validar_entrada(entrada):
    """
    Valida se a entrada é um número válido.
    
    Args:
        entrada (str): String do usuário
        
    Returns:
        tuple: (número convertido, booleano indicando sucesso)
    """
    try:
        numero = int(entrada)
        return numero, True
    except ValueError:
        return None, False


# ==============================================================================
# FUNÇÃO PARA PROCESSAR NÚMEROS
# ==============================================================================

def processar_numeros():
    """
    Processa números digitados pelo usuário em um laço while.
    Encerra quando o usuário digita 0.
    """
    
    print()
    print("  Instruções: Digite números inteiros")
    print("  Digite 0 para encerrar o programa")
    print()
    
    # Variável de controle do laço
    entrada_idade = ""
    
    # Laço while que continua até o usuário digitar 0
    while entrada_idade != "0":
        try:
            # Solicita entrada do usuário
            entrada_idade = input("  Digite um número (ou 0 para sair): ").strip()
            
            # Valida a entrada
            numero, valido = validar_entrada(entrada_idade)
            
            if not valido:
                print("  ⚠ Erro: Digite um número inteiro válido!")
                continue
            
            # Se o número for 0, encerra o laço
            if numero == 0:
                print("  ✓ Encerrando o programa...")
                break
            
            # Exibe o número digitado
            print(f"  Número digitado: {numero}")
            print()
            
        except KeyboardInterrupt:
            print()
            print("  ⚠ Programa interrompido pelo usuário!")
            break


# ==============================================================================
# FUNÇÃO PRINCIPAL
# ==============================================================================

def main():
    """
    Função principal que executa a demonstração da estrutura while.
    """
    
    # Exibe título do programa
    print("=" * 70)
    print("MICROATIVIDADE 3 - ESTRUTURAS DE REPETIÇÃO: WHILE")
    print("=" * 70)
    
    # Executa o processamento de números
    processar_numeros()
    
    print()
    print("=" * 70)
    print("Fim da Microatividade 3")
    print("=" * 70)


# ==============================================================================
# EXECUÇÃO DO PROGRAMA
# ==============================================================================

if __name__ == "__main__":
    main()
