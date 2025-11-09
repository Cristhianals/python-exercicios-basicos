while True:
    n = str(input("digite um numero e veremos se ele é um polidromo ou 0 para sair"))
    a = int(n)
    if a == 0:
        print("0 é um numero palindromo")
        break
    elif a < 10:
        print(f"o numero {a} é palindromo")
    else:
        s = str()
        while a > 0:
            d = a % 10
            s += str(d)
            a = a // 10
        if n == s:
            print(f"o numero {n} é um palindromo")
        else:
            print(f"o numero {n} nao é um palindromo ")
