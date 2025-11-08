one = int(input("digite um numero"))
two = int(input("digite outro numero para dividirmos o primeiro"))
x = 0
while one != 0:
    if one < two:
        print("escolheu o dividendo menor que o divisor, o programa e limitado a uma casa decimal apos a vrigula")
        one = int(input("o dividendo e menor que o divisor, precisamos que vc reescreva o numero e adicione um zero no final dele, para preseguirmos a conta"))
        while one != 0:
             one = one - two
             x = x + 1
             if one != 0 and two > one:
                 print(f"a sobra foi {one}")
                 #one = int(input(""))
                 one = 0
                 print(f"0,{x}")
             elif one == 0:
                 print(f"0,{x}")
    else:
        one = one - two
        x = x + 1
        if one == 0:
            print(x)
        if one != 0 and two > one:
            print(f"a sobra foi {one}")
            one = 0
            print(x)
