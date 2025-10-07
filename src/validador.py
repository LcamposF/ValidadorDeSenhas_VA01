import re

# Lista de senhas proibidas (muito comuns e inseguras)
SENHAS_PROIBIDAS = {"123456", "password", "qwerty", "abc123", "admin"}

def validar_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("pelo menos 8 caracteres")

    if senha.islower():
        erros.append("letra maiúscula")

    if senha.isupper():
        erros.append("letra minúscula")

    if not any(c.isdigit() for c in senha):
        erros.append("pelo menos um número")

    if not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/\\|" for c in senha):
        erros.append("caractere especial")

    if " " in senha:
        erros.append("não pode conter espaços")

    # Verificação de senhas muito comuns
    senhas_comuns = {"123456", "password", "qwerty", "abc123"}
    if senha in senhas_comuns:
        erros.append("muito comum e insegura")

    if erros:
        return False, "A senha apresenta os seguintes problemas: " + ", ".join(erros)

    return True, "Senha válida"
