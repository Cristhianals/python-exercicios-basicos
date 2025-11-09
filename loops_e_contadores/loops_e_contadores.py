x = 1
while x < 101:
    print(x)
    x += 1
print("\nexercicio 5.2\n")
x = 50
while x <= 101:
    print(x)
    x = x + 1

print("")
x = 10
print("contagem regressiva para lancar o foguete")
while x >= 0:
    print(x)
    if x == 0:
        print("fogo")
    x = x - 1

print("")
fim = int(input("digite o ultimo numero que aparecera na tela"))
x = 0
while x <= fim:
    print(x)
    x = x + 1
# x é um contador
print("")
print("agr iremos imprimir apenas os numeros pares")
fim = int(input("digite um numero"))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
        
    x = x + 1
print("")
print("agr iremos imprimir apenas os numeros pares, mas de forma mais simples")
print("simplificando o programa de cima")
fim = int(input("digite um numero "))
x = 0
while x <= fim:
    print(x)
    x = x + 2
