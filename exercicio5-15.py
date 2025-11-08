print("os codigos dos produtos sao, 1 2 3 4 e 5")
a = 0.50
b = 1.00
c = 4.00
d = 7.00
e = 8.00
u = 0
s = 0
while True:
    cod = int(input("qual o codigo do produto, caso nao tenha mais produtos digite 0"))
    if cod == 0:
        break
    q = int(input("qual a quantidade"))
    if cod == 1:
        u = a * q
        s += u
    elif cod == 2:
        u = b * q
        s += u
    elif cod == 3:
        u = c * q
        s += u
    elif cod == 4:
        u = d * q
        s += u
    elif cod == 5:
        u = e* q
        s += u
    else:
        print("codigo invalido")
print(f"o total da compra foi de R${s:5.2f}")
