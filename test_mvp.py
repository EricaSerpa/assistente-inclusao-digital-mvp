import unittest
from unittest.mock import patch
import sqlite3
from acessibilidade import validar_entrada_texto, aplicar_modo_acessivel
from banco import inicializar_banco, salvar_usuario_db
from cadastro import cadastrar_usuario
from tutorial import LISTA_TUTORIAIS, listar_tutoriais

class TestAssistenteInclusao(unittest.TestCase):

    def test_validacao_texto_vazio(self):
        """Garante que entradas vazias ou com espaços sejam barradas."""
        self.assertFalse(validar_entrada_texto(""))
        self.assertFalse(validar_entrada_texto("   "))

    def test_validacao_texto_valido(self):
        """Garante que entradas válidas sejam aceitas."""
        self.assertTrue(validar_entrada_texto("1"))

    def test_aplicar_modo_acessivel(self):
        """Valida se a função de acessibilidade executa sem erros."""
        try:
            aplicar_modo_acessivel("Grande (18pt)")
            sucesso = True
        except Exception:
            sucesso = False
        self.assertTrue(sucesso)

    def test_lista_tutoriais_existencia(self):
        """Garante que os tutoriais cadastrados possuem dados válidos."""
        self.assertGreater(len(LISTA_TUTORIAIS), 0)
        self.assertEqual(LISTA_TUTORIAIS[0]["id"], 1)

    def test_persistencia_banco_sqlite(self):
        """Verifica se o banco inicializa e grava um usuário corretamente."""
        inicializar_banco()
        salvar_usuario_db("Teste Unitário", 72, "Terceira Idade")
        
        conn = sqlite3.connect("assistente.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome, idade, perfil FROM usuarios WHERE nome = 'Teste Unitário'")
        resultado = cursor.fetchone()
        
        # Limpa o registro de teste para não sujar o banco
        cursor.execute("DELETE FROM usuarios WHERE nome = 'Teste Unitário'")
        conn.commit()
        conn.close()
        
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], "Teste Unitário")
        self.assertEqual(resultado[1], 72)

    @patch("builtins.input", side_effect=["2", "A", "Joana Silva", "65"])
    def test_cadastro_resiliente_apos_erro_nome(self, mock_input):
        """Valida se o cadastro solicita novo nome após entrada inválida sem abortar."""
        usuario = cadastrar_usuario()
        
        # Limpa o registro de teste do banco
        conn = sqlite3.connect("assistente.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE nome = 'Joana Silva'")
        conn.commit()
        conn.close()

        self.assertIsNotNone(usuario)
        self.assertEqual(usuario["nome"], "Joana Silva")
        self.assertEqual(usuario["perfil"], "Terceira Idade")

    @patch("builtins.input", side_effect=["99", "1", "", "0"])
    def test_navegacao_resiliente_tutoriais(self, mock_input):
        """Valida tratamento de opção inválida, conclusão de aula e retorno seguro."""
        usuario_teste = {"nome": "Maria Silva", "idade": 62, "perfil": "Terceira Idade"}
        try:
            listar_tutoriais(usuario_teste)
            executou_sem_erro = True
        except Exception:
            executou_sem_erro = False
        self.assertTrue(executou_sem_erro)

if __name__ == "__main__":
    unittest.main()