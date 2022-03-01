'''
Operadores Lógicos
and
or
not

in
not in
'''



#  Verificador de preenchimento de campo

a = ''
b = 0

if not a:
    print('Favor digitar no campo de A.')

#  Falso = não executa
#  Não verdadeiro = não executa
#  Verdadeiro = executa
#  Não falso = executa

'''
#  Caça letra em string
nome = input('Digite seu nome: ')
if 'u' or 'U' in nome:
    print('Tem "u" no seu nome!')
else:
    print('Não tem "u" no seu nome.')
'''

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'pedro'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Logado com sucesso.')
else:
    print('Dados incorretos.')
