numero1 = int(input("1º número: "))
numero2 = int(input("2º número: "))

if numero1 > numero2:
    numeroMaior = numero1
    print(f"O maior número digitado foi {numero1}")
elif numero2 > numero1:
    numeroMaior = numero2
    print(f"O maior número digitado foi {numero2}")
else:
    print("Números iguais")