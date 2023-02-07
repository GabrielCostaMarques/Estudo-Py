import forca
import adivinhacao

print("*********************************")
print("******Escolha o se jogo**********")
print("*********************************")


print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if jogo ==1:
    print("Jogando forca")
    forca.jogo_forca()
elif jogo ==2:
    print("Jogando adivinhação")
    adivinhacao.jogo_adivinhacao()