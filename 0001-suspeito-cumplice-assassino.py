import os
os.system('cls')

# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre
# um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa
# no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente"

print('Suspeito, Cúmplice e Assassino.')
print('Responda com S para Sim ou N para Não. ')
pergunta1 = input("a. Telefonou para a vítima ? ").upper()
pergunta2 = input("b. Esteve no local do crime ? ").upper()
pergunta3 = input("c. Mora perto da vítima ? ").upper()
pergunta4 = input("d. Devia para a vítima ? ").upper()
pergunta5 = input("e. Já trabalhou com a vítima ? ").upper()
perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
contagem = perguntas.count("S")
S = True
N = False
if contagem == 2:
    print('Você está classificado como Suspeito')
elif contagem == 3 or contagem == 4:
    print('Você está classificado como Cúmplice. ')
elif contagem == 5:
    print('Você está classificado como  Assasino')
else: print('Você está classificado como Inocente')

