# Módulo de Tutoriais Guiados (MVP)

LISTA_TUTORIAIS = [
    {
        "id": 1,
        "titulo": "Como usar o WhatsApp para falar com a família",
        "descricao": "Aprenda a enviar mensagens de texto e áudio de forma simples e segura.",
        "nivel": "Iniciante"
    },
    {
        "id": 2,
        "titulo": "Fazendo chamadas de vídeo",
        "descricao": "Passo a passo para ver e conversar com seus netos e amigos à distância.",
        "nivel": "Iniciante"
    },
    {
        "id": 3,
        "titulo": "Navegando na internet e buscando receitas",
        "descricao": "Como usar o navegador para encontrar notícias e receitas do dia a dia.",
        "nivel": "Intermediário"
    }
]

def listar_tutoriais(usuario):
    """
    Exibe a lista de tutoriais disponíveis formatados com linguagem simplificada
    e fontes amigáveis para a terceira idade.
    """
    print(f"\n" + "="*50)
    print(f"   TUTORIAIS DISPONÍVEIS PARA: {usuario['nome'].upper()}")
    print("="*50)
    print("Dica de acessibilidade: Conteúdo adaptado com leitura facilitada.\n")
    
    for tutorial in LISTA_TUTORIAIS:
        print(f"[{tutorial['id']}] {tutorial['titulo']}")
        print(f"    Resumo: {tutorial['descricao']}")
        print(f"    Nível: {tutorial['nivel']}")
        print("-" * 50)
        
    escolha = input("Digite o número do tutorial que deseja abrir (ou 0 para voltar): ").strip()
    
    if escolha.isdigit():
        id_escolhido = int(escolha)
        if id_escolhido == 0:
            return
            
        tutorial_selecionado = next((t for t in LISTA_TUTORIAIS if t['id'] == id_escolhido), None)
        
        if tutorial_selecionado:
            print(f"\n" + "~"*50)
            print(f" >>> AULA ATIVA: {tutorial_selecionado['titulo'].upper()}")
            print(f" >>> {tutorial_selecionado['descricao']}")
            print(" [Modo de Leitura Ampliada Ativo - Fonte 18pt]")
            print("~"*50)
            input("\nPressione ENTER para concluir a leitura e voltar ao menu...")
        else:
            print("\n[Aviso] Tutorial não encontrado. Verifique o número digitado.")
    else:
        print("\n[Aviso] Entrada inválida.")