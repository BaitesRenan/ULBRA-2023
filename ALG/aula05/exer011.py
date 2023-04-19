nome = (input('Digite o nome da pessoa:'))
peso = float(input('Digite o peso da pessoa:'))
altura = float(input('Digite a altura da pessoa:'))

imc = peso / (altura ** 2)

print(f'olá nome:\n{nome}, seu peso:\n{peso} kg, sua altura é:\n{altura}, seu imc é:\n {imc:.2f}')

if imc < 18.5:
    print('Está classificado como abaixo do peso')
elif imc  >= 18.5 and imc < 24.9:
    print(' Está classificado com PESO NORMAL')
elif imc  >= 25.0 and imc < 29.9:
    print(' Está classificado com EXCESSO DE PESO')
elif imc  >= 30.0 and imc < 34.9:
    print(' Está classificado com OBESIDADE CLASSE I')
elif imc  >= 35.0 and imc < 39.0:
    print(' Está classificado OBESIDADE CLASS II')
else:
    print('Está classificado como OBESIDADE CLASSE III')
