'''
+ Adição
- Subtração
* Multiplicação
/ Divisão
// Divisão inteira
** Potência
% Resto da divisão
()
'''

'''
# Operações feitas com 10 _ 10

print('OPERAÇÃO        OPERADOR  RESULTADO')
print('Adição           "+"  -> ', 10 + 10)
print('Subtração        "-"  -> ', 10 - 10)
print('Multiplicação    "*"  -> ', 10 * 10)
print('Divisão          "/"  -> ', 10 / 10)
print('Divisão inteira  "//" -> ', 10 // 10)
print('Potenciação      "**" -> ', 10 ** 10)
print('Resto da divisão "%"  -> ', 10 % 10)
'''

# Repetição de strings por multiplicação
print('Ai'+('ai')*10)

# Concatenação de strings por adição
print('5'+'5')
print('Pedro' + ' ' + 'Henrique')

# OBS: Não se concatena uma string (str) e um inteiro (int)

# Conversão de dados
# Número para string
str(32)

print(10/3)
# Dois ints podem virar um float ao realizar uma divisão

print(10//3)

print(10.5//3)

print(25**0.5)

print(10%3)

# Precedência Matemática
'''
Precedência dos Operadores Aritméticos

Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses (como descrito na aula anterior).
Abaixo, segue uma lista_de_lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas (de maior para menor precedência).

( n + n ) Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro
** Depois vem a exponenciação
* / //  % Na sequência multiplicação, divisão, divisão inteira e módulo
+  - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles também têm precedência,
você pode ver a lista_de_lista completa em https://docs.python.org/3/reference/expressions.html#operator-precedence
(sempre utilize a documentação oficial como reforço caso necessário).
'''


# Poliformismo -> Um operador fazer coisas diferentes:
print(10*'a')
print(10*2)






