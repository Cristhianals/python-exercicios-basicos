tabuada = 1
while tabuada <=10:
    numero = 1
    if numero == 1 and tabuada == 1:
        print(f"tabuada do {tabuada}")
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero +=1
    tabuada += 1
    if tabuada <= 10:
        print("")
        print(f"tabuada do {tabuada}")
print("")
tabuada = 1
numero = 1
while tabuada <= 10:
    if tabuada == 1 and numero == 1:
        print(f"tabuada do {tabuada}")
    print(f"{tabuada} x {numero} = {tabuada * numero}")
    numero += 1
    if numero == 11:
        tabuada +=1
        numero = 1
        if tabuada <=10:
            print("")
            print(f"tabuada do {tabuada}")
        
