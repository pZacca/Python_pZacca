d1 = {
    1: 2,
    2: 3,
    4: 5,
}

# d1.popitem() -> elimina o último item
# d1.pop(4) -> elimina o item com a chave 4

d2 = {
    'a': 'b',
    'c': 'd',
}

d1.update(d2)  # concatena dicionários.
print(d1)
