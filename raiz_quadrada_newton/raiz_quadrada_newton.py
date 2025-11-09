while True:
    n = int(input("digite um numero e diremos sua raiz quadrada, ou 0 para sair"))
    if n == 0:
        break
    else:
        b = 2
        c = 1
        while True:
            p = (b+(n/b)) / 2
            b = p
            a = p**2
            x = a - n 
            print(f"na {c} iteracao, a aproximacao atual da raiz é {p:.6f}, que da {a:.4f}")
            c += 1
            if x < 0.0001:
                break
    
