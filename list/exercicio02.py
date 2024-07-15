numeros = list(range(1,11))
print("A lista é:")
print(numeros)
print("-----------------------")
print("Os números pares são")
pares = numeros[1::2]
print(pares)
print("-----------------------")
pares.insert(2, 15)
#pares[2] = 15
print(pares)
print("O número 15 foi colocado na terceira posição dos pares")
