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
