# Exemplo de uso do *args

def world_cup_titles(country, *args):
    print(f'Country: {country}')

    for title in args:
        print(f'Year: {title}')


world_cup_titles('Brasil', '1958', 1962, 1970, 1994, 2002)


# Exemplo de uso do **kwargs
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')

    if tax_percentage:
        value += value * (tax_percentage / 100)

    if discount:
        value -= discount

    return value


valor_final = calculate_price(100, tax_percentage=20, discount=10)
print(valor_final)
