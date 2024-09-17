# Ex 1: Ao final do processamento, qual será o valor da variável SOMA? 91

# Ex 2:
# number = int(input("Digite um numero para ver se esta presente na sequência de Fibonacci "))

# def Firbonacci(n):
#     a, b= 0,1

#     while a <= n:
#         if a == n:
#             return True
#         a,b = b,a + b

#     return 

# if Firbonacci(number):
#     print(f"O numero {number} pertence a sequencia de Fibonacci.")
# else:
#      print(f"O numero {number} não pertence a sequencia de Fibonacci.")


# Ex 3:

# import json

# def Calcular_Fat():
#     with open('faturamento.json' , 'r') as arquivo:
#       dados = json.load(arquivo)
    
#     valores = [item for item in dados if item['valor'] > 0]

#     menor_dado = min(valores, key=lambda x: x['valor'])
#     maior_dado = max(valores, key=lambda x: x['valor'])

#     menor_valor = menor_dado['valor']
#     dia_menor_valor = menor_dado['dia']

#     maior_valor = maior_dado['valor']
#     dia_maior_valor = maior_dado['dia']

#     media = sum(item['valor'] for item in valores) / len(valores) 

#     acima_da_media = sum(1 for item in valores if item['valor'] > media)


#     print(f"O menor faturamento: R${menor_valor: .2f} referete a o dia {dia_menor_valor}")
#     print(f"O maior faturamento: R${maior_valor: .2f} referete a o dia {dia_maior_valor}")
#     print(f"Número de dias com faturamento acima da média mensal: {acima_da_media}")

# Calcular_Fat()
# # OBS:
# # Usei chat gpt para criar a tabela.
# # O prompt: crie uma planilha com uma coluna de "dia" e outra de "valor" , o valor é o faturamento do dia da empresa.


# Ex: 4
# def Porcentagem():
#     SP = 67836.43
#     RJ = 36678.66
#     MG = 29229.88
#     ES = 27165.48
#     Outros = 19849.53

#     total = SP + RJ + MG + ES + Outros

#     SP_P = (SP / total) *100
#     RJ_P = (RJ / total) *100
#     MG_P = (MG / total) *100
#     ES_P = (ES / total) *100
#     Outros_P = (Outros / total) *100
#     print(f"São paulo teve {SP_P: .2f}%")
#     print(f"Rio de Janeiro teve {RJ_P: .2f}%")
#     print(f"Minas Gerais teve {MG_P: .2f}%")
#     print(f"Espirito Santo teve {ES_P: .2f}%")
#     print(f"Outros {Outros_P: .2f}%")
# Porcentagem()

# Ex 5:

# def inverter(s):
#     string = ""
#     for i in range(len(s) - 1, -1,-1):
#         string += s[i]
#     return string

# string = input("Digite uma palavra: ")

# res = inverter(string)
# print(f"String invertida: {res}")

