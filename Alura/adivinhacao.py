import random
def jogo_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1,100)
    total_de_tentativas = 5
    pontos = 1000


    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa: {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100 número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if (chute <1 or chute>100):
            print("VOcê deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertoue fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print()
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print()
                print("O seu chute foi menor do que o número secreto!")
                pontos_perdidos =abs(numero_secreto-chute) #Número absoluto, ele sempre vai desconsiderar o sinal
                pontos = pontos - pontos_perdidos
    print()            
    print("Fim do jogo número era o ",numero_secreto)