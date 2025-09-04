# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 09/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR
#Ketelin kauany c souza 
peso = float(input("Digite seu peso:" ))
altura = float(input("Digite sua altura"))

imc = peso / altura**2
print(imc)


if imc <=18.5:
          print("abaixo do peso ")
elif imc <= 24.9:
          print ("Peso normal.")
elif imc <= 29.9:
          print ("Sobrepeso.")
elif imc <= 34.9:
          print ("Obesidade Grau I")
elif imc <= 39.9:
         print ("Obesidade Grau II")
else:
        print ("Obesidade Grau III")
     

     
     