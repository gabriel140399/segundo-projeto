#Entrada de dados
salarioBrutoMes = float(input("Qual seu salário bruto: "))

inss = float(salarioBrutoMes * 0.08) #INSS de 8%
sindicato = float(salarioBrutoMes * 0.05) #Sindicato de 5%


#Calculando imposto de renda com base na renda
if salarioBrutoMes <= 2.112:
    impostoRenda = 0

elif salarioBrutoMes < 2.826:
    impostoRenda = salarioBrutoMes * 0.075 - 158.40


elif salarioBrutoMes < 3.751:
    impostoRenda = salarioBrutoMes * 0.15 - 370.40


elif salarioBrutoMes < 4.664:
    impostoRenda = salarioBrutoMes * 0.225 - 651.73


elif salarioBrutoMes > 4.664:
    impostoRenda = salarioBrutoMes * 0.275 - 884.96
    
    salarioLiquido = salarioBrutoMes - inss - sindicato - impostoRenda #Calculando salário liquido

#Imprimindo credito de descontos
print("Desconto de INSS: {}".format(inss))
print("Desconto de Sindicato: {}".format(sindicato))
print("Desconto de Imposto de renda: {:.2f}".format(impostoRenda))

#Imprimindo salario liquido
print("Seu salário liquido é de: {:.2f}".format(salarioLiquido-inss-sindicato))

input("Pressione enter para sair (ENTER)")
