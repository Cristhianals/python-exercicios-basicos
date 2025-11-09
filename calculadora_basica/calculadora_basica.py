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