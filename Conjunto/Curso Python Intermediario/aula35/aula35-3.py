import copy

d1 = {
    1: 'a',
    2: 'b',
    3: ['Pedro', 'Zaccaria'],
}

"""
# A sequência a seguir mostra que o que for mudado em v será mudado em d1 também.
# O código após o comentário terá a resolução para que isso não aconteça.
v = d1
v[1] = 'Pedro'

print(d1)
print(v)
"""

v = copy.deepcopy(d1)
v[3][0] = 'Angélica'

print(d1)
print(v)
# Resolvido.
