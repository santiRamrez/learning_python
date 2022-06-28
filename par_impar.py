def par_impar():
    inp = input("Por favor ingrese un número para sumar: ")
    num:int = int(inp)
    cont:int = 1
    acum:int = num
    while (cont <= num):
        if num % 2 == 0:
            print(acum, "es par")
        else:
            print(acum, "es impar")
        cont = cont + 1
        acum = acum + num
    

par_impar()
