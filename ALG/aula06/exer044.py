# Cálculo de desconto: Escreva um programa que leia o valor de um produto e calcule o valor
# com desconto de 10%. Se o valor do produto for maior que R$ 50,00, aplique um desconto
# adicional de 5%. Exiba o valor final com desconto.

while True:

    valor_produto=float(input("Digite o valor do produto:\n"))

valor_desconto = (valor_produto/100)*10
desconto_extra = (valor_produto/100)*5
precodevenda=0

if valor_produto > 50:
    precodevenda = valor_produto - (valor_desconto + desconto_extra)
    print(f"O valor de venda é: R${precodevenda:.2f}\n")
else: 
    precodevenda = valor_produto - valor_desconto
print(f"O valor de venda é: R${precodevenda:.2f}\n")
