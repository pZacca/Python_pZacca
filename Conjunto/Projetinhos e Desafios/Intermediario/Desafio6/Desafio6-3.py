# 3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
# percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
# do aumento do percentual do mesmo.  funcao(50, 10) -> 55
def porcentador(valor_inicial, porcentagem):
    return valor_inicial + (valor_inicial * (porcentagem / 100))


ap = porcentador(100, 5)
print(ap)
