while True:
    n = int(input("digite um numero, e veremos se ele é primo, ou 0 pra sair"))
    if n == 1:
     print("1 nao é primo, pois numeros primos tenque ser maior que 1")
    elif n == 0:
        print("zero nao é primo, pois numeros primos tenque ser maior que 1")
        print("saindo")
        n = 0
        break
    else:
        d = 2
        while d < n:
             v = n % d
             if v == 0:
                 print(f"o numero {n} nao é primo")
                 break
             d += 1
        else:
            print(f"o numero {n} é primo")

                
