repete = 1
atual = 100
cedulas = 0
while repete != 0:
    valor = float(input("digite o valor a pagar"))
    repete = valor
    apagar = valor
    while valor != 0:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            if atual >= 1:
                print(f"{cedulas} cédula(s) de R${atual}")
            elif atual < 1 and atual != 0:
                print(f"{cedulas} moeda(s) de R${atual:.2f}")
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.25
            elif atual == 0.25:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05 and apagar < atual:
                print(f"Valor residual de R${apagar} não contabilizado.")
                valor = 0           
            cedulas = 0


