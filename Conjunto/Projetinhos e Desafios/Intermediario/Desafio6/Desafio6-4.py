# 4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
# se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
# função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
# número enviado.
def fb(var):
    if var % 3 == 0 and var % 5 == 0:
        return f'{var} FizzBuzz'
    if var % 3 == 0:
        return f'{var} Fizz'
    if var % 5 == 0:
        return f'{var}     Buzz'
    return var

for i in range(100):
    print(fb(i))
