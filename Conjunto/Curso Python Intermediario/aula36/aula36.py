print('\nSeja bem vindo ao questionário!\n')
perguntas = {
    'Pergunta 1': {
        'pergunta' : 'Quanto é 2+2?',
        'respostas' : {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa' : 'b',
    },
    'Pergunta 2': {
        'pergunta' : 'Quanto é 3*2?',
        'respostas' : {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa' : 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 7^2?',
        'respostas': {
            'a': '14',
            'b': '49',
            'c': '77',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 9^0?',
        'respostas': {
            'a': '1',
            'b': '9',
            'c': '0',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Qual o nome do criador disso aqui?',
        'respostas': {
            'a': 'Pedro',
            'b': 'Augusto',
            'c': 'Leôncio',
        },
        'resposta_certa': 'a',
    },
}
resp_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv["respostas"].items():
        print(f'\t[{rk}]: {rv}')

    resp = input('Sua resposta: ')
    if resp == pv['resposta_certa']:
        print('Você acertou. É o mínimo, né...\n')
        resp_certas += 1
    else:
        print('Cara...  Você errou, espero que esteja só debugando.\n')

qtd_perguntas = len(perguntas)
porcentagem_acerto = resp_certas / qtd_perguntas * 100
print(f'Foram {qtd_perguntas} perguntas e você acertou {porcentagem_acerto:.0f}% delas.\n')
