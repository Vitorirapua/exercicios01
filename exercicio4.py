numero1 = int(input("Digite o primeiro numero: "))
operacao = input("Escolha a opreração matematica: ")
numero2 = int(input("Digite o segundo numero: "))

if operacao == "+":
    print(numero1 + numero2)

elif operacao == "-":
    print(numero1 - numero2) 

elif operacao == "*":
    print(numero1 * numero2)

elif operacao == "/" :
    if numero2 != 0:
     print(f"{numero1 / numero2:.2f}")
    else:
        print("Não pode dividir por 0")
else:
    print("Operação invalida ")
 