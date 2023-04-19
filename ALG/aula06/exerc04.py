# Cálculo de desconto: Escreva um programa que leia o valor de um produto e calcule o valor
# com desconto de 10%. Se o valor do produto for maior que R$ 50,00, aplique um desconto
# adicional de 5%. Exiba o valor final com desconto.

valor_produto=float(input("Digite o valor do produto:"))

valor_desconto = (valor_produto/100)*10
desconto_extra = (valor_produto/100)*5
precodevenda=0

if valor_desconto > 50:
    precodevenda = valor_produto - (valor_desconto + desconto_extra)
    print("O valor de venda é: R${precodevenda}")
else: 
    precodevenda - valor_produto - valor_desconto
    print("O valor de venda:R${precodevenda}")





