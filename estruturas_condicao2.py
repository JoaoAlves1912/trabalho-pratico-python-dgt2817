"""
MICROATIVIDADE 2 - Estruturas de Condição: IF, ELIF e ELSE

Descrição:
Este script classifica o nível de conhecimento de um usuário baseado
em seus anos de experiência usando a estrutura condicional if/elif/else.
"""

# ==============================================================================
# FUNÇÃO PARA CLASSIFICAR NÍVEL DE EXPERIÊNCIA
# ==============================================================================

def classificar_nivel(tempo_experiencia):
    """
    Classifica o nível de conhecimento de um profissional baseado
    na experiência.
    
    Regras:
        - Menor que 2 anos: Nível Júnior
        - Entre 2 e 5 anos: Nível Pleno
        - 5 anos ou mais: Nível Sênior
    
    Args:
        tempo_experiencia (int/float): Tempo de experiência em anos
        
    Returns:
        str: Classificação do nível de conhecimento
    """
    
    if tempo_experiencia < 2:
        return "Nível de conhecimento júnior"
    elif tempo_experiencia <= 5:
        return "Nível de conhecimento pleno"
    else:
        return "Nível de conhecimento sênior"


# ==============================================================================
# FUNÇÃO PARA FORMATAR E EXIBIR RESULTADO
# ==============================================================================

def exibir_resultado(tempo_experiencia, nivel):
    """
    Exibe o resultado da classificação de forma formatada.
    
    Args:
        tempo_experiencia (int/float): Tempo de experiência
        nivel (str): Classificação do nível
    """
    print(f"  Tempo de Experiência: {tempo_experiencia} ano(s)")
    print(f"  Classificação: {nivel}")
    print()


# ==============================================================================
# FUNÇÃO PRINCIPAL
# ==============================================================================

def main():
    """
    Função principal que executa a demonstração da estrutura condicional
    com if, elif e else.
    """
    
   
    print("=" * 70)
    print("MICROATIVIDADE 2 - ESTRUTURAS DE CONDIÇÃO: IF, ELIF E ELSE")
    print("=" * 70)
    print()
    
  
    valores_teste = [5, 1, 3]
    
    
    for i, tempo in enumerate(valores_teste, 1):
        print(f"--- Teste {i} ---")
        
       
        nivel = classificar_nivel(tempo)
        
       
        exibir_resultado(tempo, nivel)
    
    print("=" * 70)
    print("Fim da Microatividade 2")
    print("=" * 70)


# ==============================================================================
# EXECUÇÃO DO PROGRAMA
# ==============================================================================

if __name__ == "__main__":
    main()
