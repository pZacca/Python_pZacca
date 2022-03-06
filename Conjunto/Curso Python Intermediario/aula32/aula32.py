
variavel = 'valor'  # Escopo global.
lol = 'bardo'

def func():
    print(variavel)

def func2(arg=None):
    # global variavel  # Torna a variável declarada localmente em global
    # variavel = 'Outro valor'  # Escopo local.
    arg = arg.replace('b', 'd')
    print(arg, 'aq eh func')
    return arg

func()
func2(arg=variavel)
func2(arg=lol)
outra_variavel = func2(lol)
print(outra_variavel, 'aq eh outra variavel')

print(variavel)
print(lol)



# Não é possível alterar uma variável global dentro de uma local.
# É possível alterar ela localmente, mas não é uma boa prática.