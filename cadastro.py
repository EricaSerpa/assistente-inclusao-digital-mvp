# Módulo de Cadastro de Alunos (MVP)
# Integrado com banco de dados SQLite para persistência

from banco import inicializar_banco, salvar_usuario_db

def cadastrar_usuario():
    """
    Realiza o cadastro simplificado do usuário, valida as entradas
    e salva os dados de forma permanente no banco SQLite.
    """
    # Garante que o banco e a tabela existem antes de inserir
    inicializar_banco()
    
    print("\n--- CADASTRO SIMPLIFICADO DE ALUNO ---")
    nome = input("Digite o seu nome completo: ").strip()
    
    if not nome or len(nome) < 2:
        print("[Erro] O nome digitado é inválido ou muito curto.")
        return None

    while True:
        idade_str = input("Digite a sua idade: ").strip()
        if idade_str.isdigit():
            idade = int(idade_str)
            if 0 < idade < 120:
                break
            else:
                print("[Aviso] Por favor, digite uma idade realista (entre 1 e 119).")
        else:
            print("[Aviso] Por favor, digite apenas números para a idade.")

    # Definindo o perfil do usuário de forma automatizada
    perfil = "Terceira Idade" if idade >= 60 else "Iniciante Digital"
    
    usuario = {
        "nome": nome,
        "idade": idade,
        "perfil": perfil
    }
    
    # Salvando no SQLite
    try:
        salvar_usuario_db(usuario['nome'], usuario['idade'], usuario['perfil'])
        print(f"\n[Sucesso] Bem-vindo(a), {usuario['nome']}! Perfil configurado: {usuario['perfil']}.")
    except Exception as e:
        print(f"\n[Erro] Ocorreu um problema ao salvar no banco de dados: {e}")
        
    return usuario