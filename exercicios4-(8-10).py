#programa 4.8
x = float(input("digite o primeiro numero "))
b = float(input("digite o segundo numero"))
ope = str(input("qual operacao vc deseja realizar? coloque os sinais (+) pra soma (-) para subtracao (x) para multiplicacao e (/) para divisao"))
if ope == "+":
    c = x + b
    print(f"a soma de {x} mais {b} é {c}")
elif ope == "-":
    c = x - b
    print(f"a subtracao de {x} menos {b} é {c}")
elif ope == "x":
    c = x * b
    print(f"a multiplicacao de {x} por {b} é {c}")
elif ope == "/":
    c = x / b
    print(f"a divisao de {x} por {b} é {c}")
else:
    print("coloque somente uma das operacoes mencionadas")
#programa 4.9
print("")
v = float(input("qual o valor da casa que vc ira comprar ?"))
s = float(input("qual o seu salario"))
age = int(input("em quantos meses o emprestimo sera pago"))
p = v / age
m =  s * 30 / 100
a = p > m
e = v / m
print("")
if a == True:
    print(f"em {age} meses o valor da prestacao ficara R${p:8.2f} que é maior que 30% do seu salario,e nao sera possivel realizar o emprestimo")
    print(f"recomendamos aumentar o valor de meses que o emprestimo sera pago.")
    print(f"caso vc queira pagar 30% do salario, ficara {int(e):d} meses com parcelas de R${m:8.2f} por mes")
if a == False:
    print(f"o emprestimos foi aprovado,o valor da pretacao sera R${p:8.2f} por mes")
    print(f"{age} meses de R${p:8.2f}")
    print(f"caso vc queira pagar 30% do salario, ficara {int(e):d} meses com parcelas de R${m:8.2f} ")
#programa4.10
print("")
kwh = int(input("qual a quantidade de kwh que foi consumida"))
i = str(input("qual o tipo de intalcao: (r) para residencial (i) para indutrial e (c) para comercial "))
if i == "r":
    if kwh <=500:
        p = kwh * 0.40
    else:
        p = kwh * 0.65
if i == "c":
    if kwh <=1000:
        p = kwh * 0.55
    else:
        p = kwh * 0.60
if i == "i":
    if kwh <=5000:
        p = kwh * 0.55
    else:
        p = kwh * 0.60
else:
    print("esse tipo de instalcao nao existe")
    p = 0
print(f"o preço a pegar pelo comsumo de energia é de R${p:8.2f}")

        
