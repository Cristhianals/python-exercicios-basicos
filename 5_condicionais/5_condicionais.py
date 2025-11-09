idade = int(input("digite a idade de seu carro: "))
if idade <= 3:
    print("seu carro é novo")
else:
    print("seu carro é velho")
print("")
#exercicio 4.6
x = int(input("qual a distancia do seu destino em km"))
if x <= 200:
    p = 0.50 * x
    print(f"cobramos R$0.50 por km, sua corrida saira por R${p:5.2f}")
else:
    p = 0.45*x
    print(f"cobramos R$0.45 por km, em viagem maiores que 200 km, sua corrida saira por R${p:5.2f}")
print("")

