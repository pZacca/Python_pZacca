frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

letrainp = input('Qual letra deseja colocar maiúscula?: ')

# Iteração <- Iterar
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letrainp.lower():
        nova_string += letrainp.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)