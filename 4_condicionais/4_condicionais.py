#Exercio 4.3
a = int(input("escreva um numero inteiro"))
b = int(input("escreva mais um numero inteiro"))
c = int(input("escreva outro numero inteiro"))

if a >= b:
    if a >= c:
         print(f"o mair numero digitado foi{a}")
if b >= c:
    if b >= a:
         print(f"o maior numero digitado foi{b}")
if c >= a:
    if c >= b:
         print(f"o maior numero digitado foi{c}")
if a <= b:
    if a <= c:
         print(f"o menor numero digitado foi{a}")
if b <= c:
   if b <= a:
         print(f"o menor numero digitado foi{b}")
if c <= a:
    if c <= b:
         print(f"o menor numero digitado foi{c}")
print("")
#exercico 4.4
s = float(input("digite o valor do seu salario"))
if s > 1250:
    s = s + (s * 10/100)
    print(f"seu aumento foi de 10%. seu salario sera {s}")
if s < 1250:
    s = s + (s * 15/100)
    print(f"seu aumento foi de 15%. seu salario sera{s}")


