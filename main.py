
# Assistente de Inclusão Digital para Terceira Idade
# Módulo Principal de Inicialização (MVP Integrado com Flask e Web UI)
import os

from flask import Flask, render_template, request, flash, redirect, url_for
from banco import inicializar_banco, salvar_usuario_db
from acessibilidade import aplicar_modo_acessivel, validar_entrada_texto
from cadastro import cadastrar_usuario
from tutorial import listar_tutoriais, LISTA_TUTORIAIS, obter_tutorial

# Inicialização do Flask
app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "chave-local-mvp-assistente")


# ==============================
# ROTAS DAS TELAS WEB
# ==============================

@app.route('/')
def home():
    """Exibe a página inicial do aplicativo."""
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    """Exibe a tela de cadastro."""
    return render_template('cadastro.html')


@app.route('/aprendizado')
def tutoriais():
    """Exibe o menu com os assuntos disponíveis para aprendizado."""
    return render_template(
        'menu.html',
        tutoriais=LISTA_TUTORIAIS
    )


@app.route('/seguranca')
def seguranca():
    """Exibe orientações de segurança digital."""
    return render_template('seguranca.html')


@app.route('/ajuda')
def ajuda():
    """Exibe a tela de ajuda e suporte."""
    return render_template('ajuda.html')


# ==============================
# ROTA PARA ABRIR UMA AULA
# ==============================

@app.route('/tutorial/<int:id_tutorial>')
def abrir_tutorial(id_tutorial):
    """Abre o conteúdo do assunto selecionado."""
    tutorial = obter_tutorial(id_tutorial)

    if tutorial is None:
        return "Conteúdo não encontrado.", 404

    return render_template(
        'tutorial.html',
        tutorial=tutorial
    )


# ==============================
# ROTA PARA CADASTRO WEB
# ==============================

@app.route('/cadastrar', methods=['POST'])
def cadastrar_web():
    nome = request.form.get('nome', '').strip()
    idade_str = request.form.get('idade', '').strip()

    if not nome or len(nome) < 2 or nome.isdigit():
        return "Nome inválido. Informe seu nome completo.", 400

    if not idade_str.isdigit():
        return "Idade inválida. Informe apenas números.", 400

    idade = int(idade_str)

    if not 0 < idade < 120:
        return "Informe uma idade entre 1 e 119 anos.", 400

    perfil = "Terceira Idade" if idade >= 60 else "Iniciante Digital"

    inicializar_banco()
    salvar_usuario_db(nome, idade, perfil)

    flash(
        f"Cadastro realizado com sucesso! Bem-vindo(a), {nome}.",
        "success"
    )

    return redirect(url_for('home'))


# ==============================
# MENU DO TERMINAL
# ==============================

def exibir_menu():
    print("\n========================================")
    print("   ASSISTENTE DE INCLUSÃO DIGITAL")
    print("========================================")
    print("1. Cadastrar Usuário / Aluno")
    print("2. Acessar Tutoriais Guiados")
    print("3. Solicitar Ajuda / Suporte por Voz")
    print("4. Iniciar Servidor Web do Aplicativo")
    print("5. Sair")
    print("========================================")


def main():
    print("Bem-vindo ao Assistente de Inclusão Digital!")

    # Ativando acessibilidade visual na inicialização
    aplicar_modo_acessivel()

    usuario_atual = None

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1-5): ").strip()

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
            print("\n[Web] Iniciando o servidor web do aplicativo...")
            print("[Web] Acesse no navegador: http://127.0.0.1:5001")
            app.run(debug=True, port=5001, use_reloader=False)

        elif opcao == "5":
            print("\nObrigado por usar o Assistente. Até logo!")
            break

        else:
            print("\n[Aviso] Opção inválida. Por favor, digite um número entre 1 e 5.")


if __name__ == "__main__":
    main()