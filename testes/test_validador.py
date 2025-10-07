import pytest
from src.validador import validar_senha

# -------------------------------
# Teste de senha válida única
# -------------------------------
def test_senha_valida():
    senha = "SenhaForte123!"
    resultado, msg = validar_senha(senha)
    assert resultado is True
    assert "Senha válida" in msg  # mais flexível que comparar string exata

# -------------------------------
# Teste de várias senhas válidas
# -------------------------------
@pytest.mark.parametrize("senha", [
    "Abcdef1!",
    "StrongPass123$",
    "MyPass@2025",
    "Valid123!$"
])
def test_varias_senhas_validas(senha):
    resultado, msg = validar_senha(senha)
    assert resultado is True
    assert "Senha válida" in msg

# -------------------------------
# Teste de várias senhas inválidas
# -------------------------------
@pytest.mark.parametrize("senha, motivo", [
    ("abc", "pelo menos 8 caracteres"),
    ("abcdefghi", "letra maiúscula"),
    ("ABCDEFGHI", "letra minúscula"),
    ("Abcdefgh", "pelo menos um número"),
    ("Abcdef12", "caractere especial"),
    ("Abc 123!", "não pode conter espaços"),
    ("123456", "muito comum e insegura")
])
def test_varias_senhas_invalidas(senha, motivo):
    resultado, msg = validar_senha(senha)
    assert resultado is False
    assert motivo in msg  # verifica se a mensagem contém o motivo esperado

# -------------------------------
# Testes individuais (opcional)
# -------------------------------
def test_senha_curta():
    resultado, msg = validar_senha("abc")
    assert resultado is False
    assert "pelo menos 8 caracteres" in msg

def test_senha_sem_maiuscula():
    resultado, msg = validar_senha("abcdenfghi")
    assert resultado is False
    assert "letra maiúscula" in msg

def test_senha_sem_minuscula():
    resultado, msg = validar_senha("ABCDEFGHI")
    assert resultado is False
    assert "letra minúscula" in msg

def test_senha_sem_numero():
    resultado, msg = validar_senha("Abcdefgh")
    assert resultado is False
    assert "pelo menos um número" in msg

def test_senha_sem_caractere_especial():
    resultado, msg = validar_senha("Abcdef12")
    assert resultado is False
    assert "caractere especial" in msg

def test_senha_com_espaco():
    resultado, msg = validar_senha("Abc 123!")
    assert resultado is False
    assert "não pode conter espaços" in msg

def test_senha_proibida():
    resultado, msg = validar_senha("123456")
    assert resultado is False
    assert "muito comum e insegura" in msg
