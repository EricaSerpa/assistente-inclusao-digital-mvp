import unittest
import os
import sqlite3
from acessibilidade import validar_entrada_texto
from banco import inicializar_banco, salvar_usuario_db

class TestAssistenteInclusao(unittest.TestCase):

    def test_validacao_texto_vazio(self):
        """Garante que entradas vazias ou com espaços sejam barradas."""
        self.assertFalse(validar_entrada_texto(""))
        self.assertFalse(validar_entrada_texto("   "))

    def test_validacao_texto_valido(self):
        """Garante que entradas válidas sejam aceitas."""
        self.assertTrue(validar_entrada_texto("1"))

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

if __name__ == "__main__":
    unittest.main()