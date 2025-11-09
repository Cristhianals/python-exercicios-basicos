while True:
    d = int(input("escreva um numero para ser dividido, ou (0) zero para sair: "))
    if d == 0:
        break
    else:
        dd = int(input("escreva o numero pelo qual ele sera dividido: "))
        a = 0
        c = 0
        while dd < d:
            if dd == 0:
                print("nao ha divisao por 0")
                break
            elif (a + dd) <= d:
                a += dd
                c += 1
            else:
                break
        s = d - a
        print(f"{d} dividido por {dd} é: {c}. e a sobra é {s}")
