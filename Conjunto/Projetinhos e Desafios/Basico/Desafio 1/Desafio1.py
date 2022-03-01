'''
1) Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa

2) Criar variável com o ano atual (int)

3) Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)

4) Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)

5) Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''

# 1)
nome = 'Pedro Henrique'
idade = 20
altura = 1.75
peso = 75

# 2)
ano_atual = 2022

# 3)
ano_nasc = ano_atual - idade

# 4)
# IMC -> Calcula-se através da divisão entre o peso (kg) e o quadrado da altura (m)
imc = peso / altura ** 2

# 5)
print('Nome: {}\nIdade: {}\nAltura: {}\nPeso: {}\nAno Atual: {}\nAno de Nascimento: {}\nIMC: {:.2f}\n'
      .format(nome, idade, altura, peso, ano_atual, ano_nasc, imc))
# Ou
print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}\nAno Atual: {ano_atual}\nAno de Nascimento: {ano_nasc}\nIMC: {imc:.2f}\n')
# Ou
print('Nome: {no}\nIdade: {id}\nAltura: {al}\nPeso: {pe}\nAno Atual: {aa}\nAno de Nascimento: {an}\nIMC: {im:.2f}'
      .format(no=nome, id=idade, al=altura, pe=peso, aa=ano_atual, an=ano_nasc, im=imc))
