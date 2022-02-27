"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funç~ioes podem ser usadas diretamente em cada tipo.

Mais em:
* https://docs.python.org/3/library/functions.html
* https://docs.python.org/3/library/stdtypes.html

"""

#  positivos [012345678]
texto = 'Python_s2'
print(texto[0::3])
for b in texto:
    print(b)
#  print(texto[0:6:2])
#  0:infinito:2 == 0::2
#  a partir de:até:pula de quanto em quanto

#  negativos -[987654321]

url = 'www.google.com.br/'
print(url[:-1])

#  texto[2:5] -> pega do elemento 2 até o 5, incluindo o 2 mas não pega o elemento 5
#  texto[2:] -> a partir do 2, incluindo o 2
#  texto[:5] -> nada depois do 5, nem mesmo o 5
#  texto[-1] -> pega o último caractere, apenas
#  texto[-9:-4] -> 'Python s2' -> 'Pytho'

#  texto[:-1] -> tira o último caractere

#  texto[0::2} ->