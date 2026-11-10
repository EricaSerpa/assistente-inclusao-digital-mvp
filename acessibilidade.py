# Módulo de Validação de Acessibilidade e Fontes (MVP)

def aplicar_modo_acessivel(tamanho_fonte="Grande (18pt)"):
    """
    Simula a aplicação de diretrizes de acessibilidade visual,
    garantindo alto contraste e espaçamento adequado.
    """
    print("\n" + "~"*50)
    print(" [ACESSIBILIDADE VISUAL ATIVADA]")
    print(f" -> Padrão de Fonte: {tamanho_fonte}")
    print(" -> Contraste otimizado e navegação simplificada prontos.")
    print("~"*50)

def validar_entrada_texto(texto):
    """
    Valida se a entrada do usuário não está vazia, emitindo
    mensagens de apoio acolhedoras.
    """
    if not texto or len(texto.strip()) == 0:
        print("\n[Aviso de Acessibilidade]: Por favor, digite uma opção válida para continuar.")
        return False
    return True