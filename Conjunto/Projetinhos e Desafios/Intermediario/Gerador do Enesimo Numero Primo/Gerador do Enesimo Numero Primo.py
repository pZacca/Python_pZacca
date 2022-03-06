# Esse algoritmo é uma função de gerador do enésimo número primo.
# Considerando que 1 não é primo, para primo(1) o retorno é 2,
# primo(2) retorna 3, primo(3) retorna 5 e assim por diante.
# **************** E M   P R O G R E S S O ****************

primos = '2 / '
n = 2
count = 2
x = int(input('Digite um numero: '))

while n < x:
    while count < x:
        n +=1
        count = 2
        mult = 0

        if not n == count:
            while n > count:
                if (n % count == 0):
                    mult += 1
                count += 1

        if(mult==0):
            primos += f' {n} / '

print(primos)

# anotações, favor ignorar
# if 49 % 1 != 0
#
#
# 49 =+ 1
#
#
#
#
# x = range(3, tentativa)
#
# if tentativa % x == 0:
#     continue
# else:
#     tentativa // x == tentativa % x