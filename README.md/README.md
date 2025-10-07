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

## Estrutura do Projeto

ValidadorDeSenhas_VA01/
│
├── src/ # Código-fonte do validador
│ └── validador.py
│
├── testes/ # Testes unitários
│ └── test_validador.py
│
├── .coverage # Relatório de cobertura de testes
└── README.md

bash
Copiar código

## Como Executar a Aplicação

1. Clone o repositório:
git clone https://github.com/LcamposF/ValidadorDeSenhas_VA01.git

2. Entre na pasta do projeto: cd ValidadorDeSenhas_VA01

3. Execute o validador: python src/validador.py


## Como Executar os Testes

O projeto utiliza pytest para testes unitários. Para rodar os testes:

1. Instale o pytest:
pip install pytest

2. Execute os testes:
python -m pytest testes --cov=src --cov-report=term-missing -v

