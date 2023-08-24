minhaLista = ['Daniel' , 'Python', 'C#', 3.18, 'Java', 15]

# listando
for posicao in range (len(minhaLista)):
    print(f"{posicao} - {minhaLista[posicao]}")


#add = input("Adicionar item na lista: ")

#minhaLista.append(add) # aqui adiciona um novo item na lista

#print(minhaLista)

busca = input ("Digite o que você está procurando: ")

resultadoBusca = minhaLista.index(busca)

print(resultadoBusca)