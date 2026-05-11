"""
MICROATIVIDADE 1 - Estruturas de Condição: IF e ELSE

Descrição:
Este script verifica a temperatura e exibe uma mensagem correspondente
baseado em se está amena ou quente.
"""

# ==============================================================================
# FUNÇÃO PARA VERIFICAR A TEMPERATURA
# ==============================================================================

def verificar_temperatura(temperatura):
    """
    Verifica a temperatura e retorna uma mensagem apropriada.
    
    Args:
        temperatura (int/float): Valor da temperatura em graus Celsius
        
    Returns:
        str: Mensagem sobre a temperatura
    """
    if temperatura < 30:
        return "A temperatura hoje está amena"
    else:
        return "Hoje está fazendo calor"


# ==============================================================================
# FUNÇÃO PRINCIPAL
# ==============================================================================

def main():
    """
    Função principal que executa a demonstração da estrutura condicional.
    """
    
    print("=" * 70)
    print("MICROATIVIDADE 1 - ESTRUTURAS DE CONDIÇÃO: IF E ELSE")
    print("=" * 70)
    print()
    
    # ========================================
    # TESTE 1: Temperatura = 29 (Menor que 30)
    # ========================================
    print("--- Teste 1: Temperatura = 29°C ---")
    temperatura_1 = 29
    resultado_1 = verificar_temperatura(temperatura_1)
    
    print(f"Temperatura: {temperatura_1}°C")
    print(f"Resultado: {resultado_1}")
    print()
    
    # ========================================
    # TESTE 2: Temperatura = 31 (Maior que 30)
    # ========================================
    print("--- Teste 2: Temperatura = 31°C ---")
    temperatura_2 = 31
    resultado_2 = verificar_temperatura(temperatura_2)
    
    print(f"Temperatura: {temperatura_2}°C")
    print(f"Resultado: {resultado_2}")
    print()
    
    # ========================================
    # TESTE ADICIONAL: Temperatura = 30 (Exatamente)
    # ========================================
    print("--- Teste 3: Temperatura = 30°C (limite) ---")
    temperatura_3 = 30
    resultado_3 = verificar_temperatura(temperatura_3)
    
    print(f"Temperatura: {temperatura_3}°C")
    print(f"Resultado: {resultado_3}")
    print()
    
    print("=" * 70)
    print("Fim da Microatividade 1")
    print("=" * 70)


# ==============================================================================
# EXECUÇÃO DO PROGRAMA
# ==============================================================================

if __name__ == "__main__":
    main()
