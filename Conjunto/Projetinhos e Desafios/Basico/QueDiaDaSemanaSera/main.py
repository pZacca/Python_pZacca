#  Esse teste é para verificar meus conhecimentos de Python até o momento.
#  O propósito é que o usuário diga que dia da semana é hoje e a quantidade
#  de dias que ele quer pular para saber em qual dia da semana cairá.

"""
Considerações finais:
Cometi um equívoco ao pensar que em uma string  tst = 'Teste' retornaria 'T' se eu chamasse o vetor 5 através de
tst[5], já que tst[-1] retorna 'e' e tst[10^10] retorna T, achei que a "circularidade" de strings fosse algo válido,
então tive a ideia de fazer um algoritmo para calcular dias da semana através dessa lógica. Infelizmente, o que
relatei foram meras coincidências e não é possível executar o algoritmo desta forma.
"""
#  A ideia que me resta para fazer um dia funcionar é usar logaritmos de base 7. Bom, fica anotado.

dia_sem = input('0 = Domingo\n1 = Segunda-feira\n2 = Terça-feira\n3 = Quarta-feira\n4 = Quinta-feira'
                '\n5 = Sexta-feira\n6 = Sábado\n\nDigite o dia da semana de hoje: ')

if dia_sem.isdecimal():
    dia_sem = int(dia_sem)
    if dia_sem < 7:
        dia_pul = input('Digite a quantidade de dias a serem pulados: ')
        if dia_pul.isdecimal():
            dia_pul = int(dia_pul)
            dias = '0123456'
            if dia_sem == 0:
                dia_esc = 'Domingo'
            elif dia_sem == 1:
                dia_esc = 'Segunda-feira'
            elif dia_sem == 2:
                dia_esc = 'Terça-feira'
            elif dia_sem == 3:
                dia_esc = 'Quarta-feira'
            elif dia_sem == 4:
                dia_esc = 'Quinta-feira'
            elif dia_sem == 5:
                dia_esc = 'Sexta-feira'
            else:
                dia_esc = 'Sábado'
            #  Possível otimização encurtando os caminhos sabendo se o dia da semana é par ou ímpar?

            dia_finum = dias[dia_sem+dia_pul]
            dia_finum = int(dia_finum)
            if dia_finum == 0:
                dia_fim = 'Domingo'
            elif dia_finum == 1:
                dia_fim = 'Segunda-feira'
            elif dia_finum == 2:
                dia_fim = 'Terça-feira'
            elif dia_finum == 3:
                dia_fim = 'Quarta-feira'
            elif dia_finum == 4:
                dia_fim = 'Quinta-feira'
            elif dia_finum == 5:
                dia_fim = 'Sexta-feira'
            else:
                dia_fim = 'Sábado'

            print(f'Você escolheu {dia_esc.lower()} e quer saber que dia da semana cai se pularmos {dia_pul} dia(s), cairá em {dia_fim.lower()}.')

        else:
            print('Digite um valor válido.')
    else:
        print('Digite um dia da semana.')
else:
    print('Digite um valor válido.')


