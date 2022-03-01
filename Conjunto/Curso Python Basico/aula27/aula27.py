"""
Operador ternário em Python
"""
# logged_user = True
#
# if logged_user:
#     msg = 'Usuário logado.'
# else:
#     msg = 'Usuário precisa logar.'
#
# print(msg)

# logged_user = False
# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
# print(msg)

# idade = 18
# if idade >= 18:
#     print('Pode acessar.')
# else:
#     print('Não pode acessar.')

while True:
    idade = input('Qual sua idade? ')

    if not idade.isnumeric():
        print('Digite apenas números.')
        continue
    else:
        idade = int(idade)
        de_maior = (idade>=18)
        print('Pode acessar' if de_maior else 'Não pode acessar')
        break