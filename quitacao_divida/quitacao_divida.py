d = float(input("qual o valor da divida"))
j = int(input("qual e a taxa de juros mensal"))
p = float(input("quantos vc ira pagar por mes pra quitar a divida"))
a = d
tj = 0
tp = d
m = 0
if j > p:
    print("o juros e maior que o valor que sera pago por mes, logo a divida nunca sera quitda")
    a = 0
while a > 0:
    a = a +(a * j /100)
    tj = tj + (a - d)
    a = a - p
    d = a 
    if a < 0:
        g = p + a
        print(f"a ultima parcela vai ser de R${g:5.2f}")
        a = 0
    m = m + 1
tp = tp + tj
print(f"a divida sera paga em {m} meses, o total pago sera de R${tp:5.2f} e o total de juros sera de R${tj:5.2f}")

