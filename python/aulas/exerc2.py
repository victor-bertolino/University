valorDolar = float(input("Digite o valor do dólar: $"))
quantidadeReais = float(input("Digite o valor de reais a ser convertido: R$"))
realConvertido = quantidadeReais / valorDolar

print(f"R${quantidadeReais} = ${realConvertido:,.2f}")