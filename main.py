# Assistente de Inclusão Digital para Terceira Idade
# Módulo Principal de Inicialização (MVP Integrado)

from acessibilidade import aplicar_modo_acessivel, validar_entrada_texto
from cadastro import cadastrar_usuario
from tutorial import listar_tutoriais

def exibir_menu():
    print("\n========================================")
    print("   ASSISTENTE DE INCLUSÃO DIGITAL")
    print("========================================")
    print("1. Cadastrar Usuário / Aluno")
    print("2. Acessar Tutoriais Guiados")
    print("3. Solicitar Ajuda / Suporte por Voz")
    print("4. Sair")
    print("========================================")

def main():
    print("Bem-vindo ao Assistente de Inclusão Digital!")
    
    # Ativando acessibilidade visual na inicialização
    aplicar_modo_acessivel()
    
    usuario_atual = None
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1-4): ").strip()
        
        if not validar_entrada_texto(opcao):
            continue
        
        if opcao == "1":
            usuario_atual = cadastrar_usuario()
        elif opcao == "2":
            if usuario_atual:
                listar_tutoriais(usuario_atual)
            else:
                print("\n[Aviso] Por favor, realize o cadastro (Opção 1) antes de acessar os tutoriais.")
        elif opcao == "3":
            if usuario_atual:
                print(f"\n[Suporte] Conectando {usuario_atual['nome']} à central de ajuda por voz...")
            else:
                print("\n[Suporte] Conectando à central de ajuda simplificada...")
        elif opcao == "4":
            print("\nObrigado por usar o Assistente. Até logo!")
            break
        else:
            print("\n[Aviso] Opção inválida. Por favor, digite um número entre 1 e 4.")

if __name__ == "__main__":
    main()