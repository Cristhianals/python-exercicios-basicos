fazer = 1
while fazer != 0:
    fazer = int(input("oq dezeja fazer, 1 para subtracao(-),2 para adicao(+),3 para multiplicacao(x), 4 para divisao(/),0 para sair"))
    t = 0
    pare = 1
    while pare != 0:
        v = 1
        t += 1
        if fazer == 1:
            op = "subtracao"
        elif fazer == 2:
            op = "adicao"
        elif fazer == 3:
            op = "multiplicacao"
        elif fazer == 4:
            op = "divisao"
        elif fazer == 0:
            print("saindo")
            break
        else:
            print("essa operacao nao existe")
            break
        print("")
        print(f"tabuada de {op} com {t}")
        while fazer == 3 and v <=10:
            print(f"{t} x {v} = {t * v}")
            v +=1
            if t >=10:
                pare = 0
        while fazer == 2 and v <=10:
            print(f"{t} + {v} = {t + v}")
            v += 1
            if t >=10:
                pare = 0
        while fazer == 1 and v <=10:
            print(f"{t} - {v} = {t - v}")
            v +=1
            if t >=10:
                pare = 0
        while fazer == 4 and v <=10:
            print(f"{t} / {v} = {t / v:.2f}")
            v +=1
            if t >=10:
                pare = 0
