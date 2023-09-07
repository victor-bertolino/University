primeiroLado = int(input("1º Lado: "))
segundoLado = int(input("2º Lado: "))
terceiroLado = int(input("3º Lado: "))

if primeiroLado == segundoLado and primeiroLado == terceiroLado:
    print("Triângulo Equilátero")
elif primeiroLado != segundoLado and primeiroLado != terceiroLado:
    print("Triângulo Escaleno")
else:
    print("Triângulo Isósceles")

#Triângulo Equilátero: Todos os lados são iguais
#Triângulo Isósceles: Dois lados iguais
#Triângulo Escaleno: Nenhum dos lados são iguais
