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
#programa 4.5
print("usando estruturas alinhadas")
minutos = int(input("quantos minutos  voce utilizou nossos serviços este mes"))
if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print(f"voce tera que pagar este mes: R${minutos * preço}")
    
