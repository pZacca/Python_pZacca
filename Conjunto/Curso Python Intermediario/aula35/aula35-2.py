
clientes = {
    'cliente1' : {
        'nome' : 'Pedro',
        'sobrenome' : 'Zaccaria',
    },

    'cliente2' : {
        'nome' : 'Alan',
        'sobrenome' : 'Turing',
    },

    'cliente3' : {
        'nome' : 'Marie',
        'sobrenome' : 'Curie',
    },

}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo: {clientes_k}')

    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k}: {dados_v}')

    print()
