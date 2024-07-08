#Receber a idade do usuario como inteiro em uma variavél
var_idade = int(input("Qual sua idade? "))
if var_idade >= 16: 
    #Se é maior ou igual (verdade -> true)
    #Mostre a mensagem abaixo no terminal
    print ("Você pode votar")
else:
    #Se menor (menitra -> false)
    print("Você não pode votar...")