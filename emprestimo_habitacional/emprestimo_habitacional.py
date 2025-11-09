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
