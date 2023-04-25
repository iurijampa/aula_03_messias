numeros = []
for i in range(10):
    while True:
        try:
            entrada = input("Digite um número: ")
            numero = int(entrada)
            numeros.append(numero)
            break
        except ValueError:
            print("Erro: Por favor digite apenas números.")        

repetidos = []
for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] == numeros[j] and numeros[i] not in repetidos:
            repetidos.append(numeros[i])

for num in repetidos:
        posicoes = [i for i in range(len(numeros)) if numeros[i] == num]
        print(f"O numero {num} se repetiu e a posição dele é: {posicoes}")
if len(repetidos) == 0:
    print("Não tem números repetidos.") 
else:
    print("A sequencia dos numeros inversos fica:")
    for numero in reversed(numeros):
        print(numero)


    