# Sistema de Login com Flask e JWT

Este projeto é uma API simples de autenticação, desenvolvida em Python com o framework Flask. Utiliza autenticação via JSON Web Token (JWT) e registro de tentativas de login em arquivo de texto.

## Funcionalidades

- Autenticação de usuários com email e senha
- Senhas armazenadas de forma segura com hash (bcrypt via werkzeug)
- Geração de tokens JWT para sessões autenticadas
- Registro de tentativas de login (sucesso ou falha) em arquivo `.txt`
- Front-end simples com página HTML de login 

## Tecnologias utilizadas

- Python 3.x
- Flask
- Werkzeug (para hash de senhas)
- PyJWT (para geração e validação dos tokens)
- HTML (para a página de login)

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
