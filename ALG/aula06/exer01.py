# Cálculo de média: Escreva um programa que leia três notas e calcule a média do aluno. Se a
# média for maior ou igual a 7, exiba a mensagem "Aprovado". Caso contrário, exiba
# "Reprovado".

nota1=float(input("Digite a nota do aluno:\n"))
nota2=float(input("Digite a nota do aluno:\n"))
nota3=float(input("Digite a nota do aluno:\n"))

media=(nota1+nota2+nota3)/3

if media >= 7:
    print(("O aluno esta aprovado!"))
elif media <= 7:
    print("O aluno está reprovado")




