print("imposto é cobrado pra quem ganha mais de 1200")
salario = float(input("qual é seu salario :"))
imposto = salario > 1200
print(imposto)
print("se obteve a respota TRUE vc devera pagar imposto, se obteve FALSE vc nao pagara")
print("usando logica e operadores")
a = 1
print("a recebe",a)
b = 2
print("b recebe",b)
c = True
print("c recebe",c)
d = False
print("d recebe",d)
print("a > b and c or d")
print(a > b and c or d)#falso
print("novos valores")
a = 10
print("a recebe",a)
b = 3
print("b recebe",b)
c = False
print("c recebe",c)
d = True
print("c recebe",d)
print("a > b and c or d")
print(a > b and c or d)#true
print("novos valores")
a = 5
print("a recebe",a)
b = 1
print("c recebe",b)
c = True
print("c recebe",c)
d = True
print("c recebe",d)
print("a > b and c or d")
print(a > b and c or d)#true
print("como saber se vc foi aprovado")
print("para ser aprovado a media da suas notas devem ser maior que 7")
materia1= float(input("digite sua primeira nota"))
materia2= float(input("digite sua segunda nota"))
materia3= float(input("digite sua terceira nota"))
aprovado = ((1*materia1 + 1*materia2 + 1*materia3)/3)
print("a media das suas notas fomram",aprovado)
print("resposta",aprovado > 7)
print("se vc obeteve a resposta TRUE, vc foi aprovado, se obteve FALSE,vc nao foi")
