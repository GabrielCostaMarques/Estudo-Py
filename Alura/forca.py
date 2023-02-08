def jogo_forca():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "Banana"
    enforcou = False
    acertou =False
    while (not enforcou and not acertou):
        print("Jogando...")
        chute=input("Qual Letra: ").strip()

        index =0
        for letra in palavra_secreta:
            if (chute.upper() ==letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index +=1


    print("Fim do jogo!!")

if __name__=="__main__":
    jogo_forca()