x = 1
ren = 0
n = float(input("digite o valor do deposito inicial"))
t = float(input("qual é a texa de juros da poupança, MENSAL"))
soma = n 
while x <= 24:
    soma = soma + (soma * t / 100 )
    ren = soma - n
    print(f"o {x} mes sera de {soma:8.2f}, redeu {ren:8.2f} comparado com o valor inicial")
    x = x + 1
print(f"o total ganho foi de {ren:5.2f}")
print("")
x = 1
ren = 0
t = float(input("qual é a texa de juros da poupança, MENSAL"))
d = 0
n = 0
soma = 0 
while x <= 24:
    d = float(input("digite o valor do deposito, se nao dor depositar digite 0: "))
    soma = soma + d
    n = n + d
    soma = soma + (soma * t / 100 )
    ren = soma - n  
    print(f"o {x} mes sera de {soma:5.2f}, redeu {ren:5.2f} comparado com o valor inicial")
    d = 0
    x = x + 1
print(f"o total ganho foi de {ren:5.2f}") 
print("")
d = float(input("qual é o valor da divida R$"))
j = float(input("qual é o valor do juros da divida ?"))
p = float(input("quantos vc pagara por mes para quitar a divida"))
t = d
m = 0
a = 0
x = 0
while p <= d:
    t = t + (t * j /100)
    m = t - p
    a = t - d
    x = x + 1
    p = p + p
    if p > d:
        g = p - d
        print(f"restara uma parcela de R${g}")
print(f"o numero de meses que a divida sera quitada é de {x}")
print(f"e o valor total de juros foi de R${a}")
print(m)
    
