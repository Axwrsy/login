from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)

# chave secreta usada para assinar e validar os tokens JWT
secret_key = 's9d8f7s6df87s6df7s8d7f6s7df8s7df6s7df6s7df6sdf7s6df7sd'

# simula um banco de dados ja q é so pra teste
# se nao tiver o usuário dentro do banco de dados a pessoa nao vai conseguir entrar 
usuarios = {
    "ana@gmail.com": generate_password_hash("ana#$#"),
    "carol@gmail.com": generate_password_hash("ana456")
}

# função que registra tentativas (sucesso ou fracasso) no arquivo txt
def registrar_login(email, sucesso):
    with open("logins.txt", "a") as arquivo:
        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        status = "SUCESSO" if sucesso else "FALHA"
        arquivo.write(f"{data} - {email} - {status}\n")

# aq é onde vai direcionar pra pág de login no html 
@app.route('/')
def login_page():
    return render_template('login.html')

# página inicial que o usuário vai acessar após o login
@app.route('/home')
def home_page():
    return render_template('index.html')

# pega os dados enviados na requisição e valida o login
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    senha = request.json.get('senha')

    if email in usuarios and check_password_hash(usuarios[email], senha):
        # payload é a seção que tem as info sobre o usuário autenticado
        payload = {
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # expiração do token
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        # registra login bem-sucedido
        registrar_login(email, sucesso=True)

        return jsonify({"success": True, "token": token})

    # registra tentativa de login inválida
    registrar_login(email, sucesso=False)

    return jsonify({"success": False, "message": "usúario não cadastrado"}), 401

# parte opcional
# 'debug=True' ativa o modo de desenvolvimento, útil durante a criação do projeto
if __name__ == '__main__':
    app.run(debug=True)