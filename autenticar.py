from controlador_usuario import autenticar 


login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if autenticar(login, senha):
    print("Autenticação bem-sucedida!")
else:
    print("Login ou senha incorretos.")
