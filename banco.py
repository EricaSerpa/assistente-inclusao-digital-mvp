# Módulo de Banco de Dados SQLite para o MVP
import sqlite3

def inicializar_banco():
    """Cria o arquivo do banco de dados e a tabela de usuários se não existirem."""
    conexao = sqlite3.connect("assistente.db")
    cursor = conexao.cursor()
    
    # Criando a tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            perfil TEXT NOT NULL
        )
    """)
    
    conexao.commit()
    conexao.close()

def salvar_usuario_db(nome, idade, perfil):
    """Insere um novo usuário na tabela do SQLite."""
    conexao = sqlite3.connect("assistente.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
        INSERT INTO usuarios (nome, idade, perfil)
        VALUES (?, ?, ?)
    """, (nome, idade, perfil))
    
    conexao.commit()
    conexao.close()
    print("[Banco de Dados] Usuário salvo com sucesso no SQLite!")