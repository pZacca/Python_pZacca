"""
Funções - def em Python (Parte 1)
"""
def saudacao(msg = 'Olá', nome = 'Pedro'):
    nome = nome.replace('e', '3')  # Sempre que achar uma letra 'e', mudará para '3'.
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)