fim = int(input("digite um numero"))
print(f"mostraremos apenas os impares de 0 a {fim}")
x = 0
while x <= fim:
     if x % 2 == 1:
         print(x)
     x = x + 1
# posso usar o != 0(diferente de zero)
print("outra forma mais simples do programa acima")
fim = int(input("digite o ultimo numero que aparecera na tela"))
print(f"mostraremos apenas os impares de 0 a {fim}")
x = 1
while x <= fim:
    print(x)
    x = x + 2
