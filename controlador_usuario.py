def autenticar(login, senha):
    usuarios = [
        {"login": "teste", "senha": "admin"},
        {"login": "teste2", "senha": "admin2"},
        {"login": "teste3", "senha": "admin3"}
    ]
    
    for usuario in usuarios:
        if usuario["login"] == login and usuario["senha"] == senha:
            return True  
    
    return False  

if __name__ == "__main__":
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if autenticar(login, senha):
        print("Autenticação bem-sucedida!")
    else:
        print("Login ou senha incorretos.")
