# 🔑 Validador de Senhas

Projeto desenvolvido para fins acadêmicos, com o objetivo de demonstrar a **implementação de regras de negócio** e **testes unitários** em Python.  
A aplicação realiza a validação de senhas seguindo critérios de segurança amplamente recomendados.

---

## 📚 Objetivo do Projeto

O projeto visa exercitar:

- Definição de **regras de negócio claras**.  
- Implementação de **testes unitários** para garantir a qualidade do código.  
- Utilização de **ferramentas de cobertura de testes** (Pytest + Pytest-Cov).  
- Integração com **Git e GitHub** para versionamento e entrega.


## ✅ Regras de Negócio Testadas

A função validar_senha(senha: str) segue as seguintes regras de segurança:

- A senha deve ter mínimo de 8 caracteres.
- Deve conter pelo menos uma letra maiúscula (A–Z).
- Deve conter pelo menos uma letra minúscula (a–z).
- Deve conter pelo menos um número (0–9).
- Deve conter pelo menos um caractere especial (ex.: !@#$%).
- Não pode conter espaços em branco.
- Não pode estar na lista de senhas proibidas/comuns ("123456", "password", "qwerty", etc.).

## Resultado esperado:

- Se todas as regras forem cumpridas → (True, "Senha válida")
- Caso contrário → (False, "Mensagem de erro correspondente")


##  Resultados dos Testes

A cobertura de testes foi obtida com pytest-cov.

<img width="1563" height="865" alt="image" src="https://github.com/user-attachments/assets/6abce288-229c-462e-b2d7-bfb852ad45da" />

✅ Todos os testes passaram.
✅ Cobertura do código: 100%

Se todas as regras forem cumpridas → (True, "Senha válida")

Caso contrário → (False, "Mensagem de erro correspondente")