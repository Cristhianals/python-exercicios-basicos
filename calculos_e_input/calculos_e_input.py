#execicio 3.7
one =float(input("digite um numero: "))
print(one)
two = float(input("digite o segundo numero: "))
print(two)
x = one + two
print(f"a soma dos numeros é:{x}")
print("")
#exercicio 3.8
M = int(input("quantos metros"))
print(f"voce digitou {M} metros")
m = M * 1000
print(f"{M} metros em milemetros é {m}")
print("")
#execicio3.9
x = int(input("quantos dias vc usa nosso programa"))
h = int(input("quantas horas"))
d = int(input("quantos minutos"))
a = int(input("e quantos segundos"))
DemHemM = x * 24 * 60 * 60
HemM = h * 60 * 60
MemS = d * 60
total = DemHemM + HemM + MemS + a
print(f"vc tem um total de {total} segudos em nosso aplicativo")
print("")
#execicio 3.10
salario = float(input("qual e o seu salario"))
print(f"seu salario é {salario:5.2f}")
porcento = float(input("quantos % de aumento sera dado ?"))
print(f"o aumento sera de {porcento}%")
aumento = salario +(salario * porcento/100)
print(f"seu aumento foi de {porcento}% logo seu salario sera {aumento}")
print("")
#exercicio 3.11
x = float(input("qual é o preço do produto"))
desc = float(input("quantos % de desconto"))
a = x * desc/100
print(f"o desconto sera de R${a}")
pap = x - (x * desc/100)
print(f"o produto ficara R${pap}")
print("")
#exercicio 3.12
b = int(input("qual sera a velociadade media do carro em KM/H"))
c = float(input("qual sera a distancia a percorrer em KM"))
ddv = c / b
print(f"vcs chegaram ao destino em {ddv} horas")
print("")
#exercicio 3.13
c = int(input("quantos graus esta em celsios"))
cef = (9 * c / 5 )+ 32
print(f"em fahrenheit e temperatura seria {cef}")
f = int(input("agr digite a temperatura em fahrenheit"))
fec = 5/9 * (f - 32)
print(f"a temperatura em celsios é {fec}")
print("")
k = int(input("quantos km foram percorridos com o carro"))
d = int(input("quantos dias o carro ficou alugado"))
print("cobramos R$60 por dia e R$0.15 por KM")
ded = d * 60
ked = k * 0.15
total = ded + ked
print(f"total a pagar de de R${total}")
print("")
d = int(input("quantos cigarros voce fuma por dia"))
a = int(input("quantos anos voce fuma cigarro"))
aed = 365 * a
pdv = d * 10
pdvt = pdv * aed
emdias = pdvt / 1440
print(f"voce ja perdeu {pdvt} minutos de vida oq da aproximadamente {emdias} dias")
