"""
MICROATIVIDADE 6 - Funções com Parâmetros e Validação

Objetivo: Demonstrar funções que recebem argumentos e processam regras de negócio.
"""


def loginUsuario(perfil):
    """
    Verifica o nível de acesso do utilizador com base no perfil fornecido.
    A validação é feita de forma 'case-insensitive' usando .lower().

    Args:
        perfil (str): O nome do perfil do utilizador.
    """
    perfil_processado = perfil.strip().lower()

    if perfil_processado == "admin":
        print(f"  Entrada: '{perfil}' -> Resultado: Bem-vindo, Administrador")
    else:
        print(f"  Entrada: '{perfil}' -> Resultado: Bem-vindo, Usuário")


def main():
    """
    Função principal que executa o menu de testes para a função de login.
    """
    print("=" * 70)
    print("MICROATIVIDADE 6 - FUNÇÕES COM PARÂMETROS E VALIDAÇÃO")
    print("=" * 70)
    print("\nIniciando bateria de testes de login...\n")

    testes = ["Admin", "admin", "User", "usuário", "GUEST", "ADMINISTRADOR"]

    for i, caso in enumerate(testes, 1):
        print(f"Teste {i}:")
        loginUsuario(caso)
        print("-" * 30)

    print("\n" + "=" * 70)
    print("Fim da Microatividade 6")
    print("=" * 70)


if __name__ == "__main__":
    main()
