# Assistente de Inclusão Digital para Terceira Idade

# Assistente de Inclusão Digital para Terceira Idade (MVP)

Sistema modular desenvolvido em Python com foco em acessibilidade visual, navegação simplificada e persistência de dados em SQLite para apoiar usuários da terceira idade no aprendizado de ferramentas digitais.

## Estrutura do Projeto

- `main.py`: Orquestração do menu principal e fluxo de controle.
- `cadastro.py`: Coleta simplificada de dados, validação amigável e classificação de perfil etário.
- `tutorial.py`: Catálogo de aulas guiadas com modo de leitura ampliada.
- `acessibilidade.py`: Diretrizes de contraste, padrão de fonte e sanitização de entradas.
- `banco.py`: Camada de persistência utilizando banco de dados relacional SQLite (`assistente.db`).
- `test_mvp.py`: Suíte de testes unitários automatizados.

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. No terminal, execute o módulo principal:
   ```bash
   python3 main.py

