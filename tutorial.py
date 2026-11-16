
# Módulo de Tutoriais Guiados (MVP)

LISTA_TUTORIAIS = [
    {
        "id": 1,
        "titulo": "WhatsApp: mensagens e áudios",
        "descricao": "Aprenda a conversar com familiares e amigos.",
        "nivel": "Iniciante",
        "passos": [
            "Abra o WhatsApp no seu celular.",
            "Toque no nome da pessoa com quem deseja conversar.",
            "Toque no campo de mensagem e escreva o que deseja enviar.",
            "Toque no botão de enviar, representado por uma seta.",
            "Para enviar um áudio, mantenha pressionado o botão do microfone e fale.",
            "Solte o botão para enviar sua gravação."
        ]
    },
    {
        "id": 2,
        "titulo": "Como fazer chamadas de vídeo",
        "descricao": "Aprenda a conversar vendo a pessoa pelo celular.",
        "nivel": "Iniciante",
        "passos": [
            "Abra o WhatsApp.",
            "Escolha o contato da pessoa com quem deseja conversar.",
            "Toque no símbolo de câmera para iniciar uma chamada de vídeo.",
            "Aguarde a pessoa atender.",
            "Para encerrar, toque no botão vermelho do telefone."
        ]
    },
    {
        "id": 3,
        "titulo": "Como fazer um Pix com segurança",
        "descricao": "Aprenda cuidados importantes antes de confirmar um Pix.",
        "nivel": "Iniciante",
        "passos": [
            "Abra o aplicativo oficial do seu banco.",
            "Entre na opção Pix.",
            "Escolha a forma de transferência indicada pelo banco.",
            "Digite os dados do destinatário com atenção.",
            "Confira o nome de quem vai receber e o valor.",
            "Somente confirme se todas as informações estiverem corretas.",
            "Guarde o comprovante da operação."
        ]
    },
    {
        "id": 4,
        "titulo": "Como evitar golpes no celular",
        "descricao": "Aprenda a reconhecer mensagens e pedidos suspeitos.",
        "nivel": "Iniciante",
        "passos": [
            "Desconfie de mensagens que pedem dinheiro com urgência.",
            "Não clique em links enviados por desconhecidos.",
            "Nunca informe senhas ou códigos recebidos por SMS.",
            "Não compartilhe sua senha bancária.",
            "Se alguém conhecido pedir dinheiro, confirme a solicitação por uma ligação.",
            "Em caso de dúvida, procure ajuda de alguém de confiança."
        ]
    },
    {
        "id": 5,
        "titulo": "Como navegar na internet",
        "descricao": "Aprenda a pesquisar receitas e informações.",
        "nivel": "Iniciante",
        "passos": [
            "Abra o navegador de internet do celular.",
            "Toque na barra de pesquisa.",
            "Digite o assunto que deseja encontrar.",
            "Toque no botão de pesquisar.",
            "Leia os resultados com atenção.",
            "Evite fornecer dados pessoais em sites desconhecidos."
        ]
    }
]


def obter_tutorial(id_tutorial):
    """Localiza um tutorial pelo seu identificador."""
    return next(
        (tutorial for tutorial in LISTA_TUTORIAIS
         if tutorial["id"] == id_tutorial),
        None
    )


def listar_tutoriais(usuario):
    """
    Exibe os tutoriais no terminal com linguagem simples
    e orientação passo a passo.
    """
    while True:
        print("\n" + "=" * 50)
        print(f" TUTORIAIS DISPONÍVEIS PARA: {usuario['nome'].upper()}")
        print("=" * 50)

        for tutorial in LISTA_TUTORIAIS:
            print(f"\n[{tutorial['id']}] {tutorial['titulo']}")
            print(f"Resumo: {tutorial['descricao']}")
            print(f"Nível: {tutorial['nivel']}")
            print("-" * 50)

        escolha = input(
            "\nDigite o número do tutorial ou 0 para voltar: "
        ).strip()

        if not escolha.isdigit():
            print("\n[Aviso] Digite apenas números.")
            continue

        id_escolhido = int(escolha)

        if id_escolhido == 0:
            print("\n[Navegação] Retornando ao menu principal...")
            return

        tutorial_selecionado = obter_tutorial(id_escolhido)

        if tutorial_selecionado:
            print("\n" + "~" * 50)
            print(f"AULA: {tutorial_selecionado['titulo'].upper()}")
            print(tutorial_selecionado["descricao"])
            print("\nPASSO A PASSO:")

            for numero, passo in enumerate(
                tutorial_selecionado["passos"], start=1
            ):
                print(f"\n{numero}. {passo}")

            print("\n" + "~" * 50)
            input("\nPressione ENTER para concluir a leitura...")

            print(
                f"\n[Concluído] Parabéns, {usuario['nome']}! "
                f"Você finalizou: {tutorial_selecionado['titulo']}."
            )
        else:
            print("\n[Aviso] Tutorial não encontrado.")
