''' 11. Crie um sistema de login que não permite que o nome de usuário e a senha sejam iguais.'''
usuario = input('Nome do usuário: ').strip()
senha = input('Senha: ').strip()
if usuario.lower() == senha.lower():
    print('Validação Impossível! Usuário e senha são iguais.')
else:
    print('Usuário e senha cadastrados!')