def mostrar_opcao():
    print()
    print("-=-=-=-=-=-=-=-=-=-= MENU =-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" Opção 1 - Cadastrar mês de referência")
    print(" Opção 2 - Exibir dados do mês de referência")
    print(" Opção 3 - Relatório comparativo - Referência 2019")
    print(" Opção 4 - Mostrar todos os relatórios")
    print("-="*26)
    print()

lista=[]
relatorio={}




def imprime_pesquisa():
    print()
    print(" Data de pesquisa: ",relatorio["Data"],"\n",
            "Total de Habitantes: ",relatorio["Habitação"],"\n",
            "Total de Óbitos: ",relatorio["Óbitos"])
    print("-=" *30)
    



def cadastrar():
    while True:
        relatorio['Data']=str(input("Digite o mês-ano do relatório: "))
        if len(relatorio['Data'])>7:
            print("\033[7;49;31m DATA INVÁLIDA!!!\033[m")
            print()
            print(f'\033[1;49;32m USE O FORMATO "00-0000" (MÊS-ANO) \033[m')
            print()
            break
        
        relatorio['Habitação']= int(input("Digite o total de Habitantes: "))
        if relatorio['Habitação']<1:
            print()
            print("\033[7;49;31mPOR FAVOR COLOQUE APENAS NÚMEROS NATURAIS E POSITIVO!!!\033[m")
            break
        
        relatorio['Óbitos']=int(input("Digite o número de Óbitos: "))
        if relatorio['Óbitos']>relatorio['Habitação']:
            print()
            print("\033[7;49;31mO NÚMERO DE ÓBITOS TEM QUE SER MENOR OU IGUAL AOS DE HABITANTES\033[m")
            break
        lista.append(relatorio.copy())
        while True:
            resp=input("Quer continuar? [S/N]: ").upper()[0]
            if resp in 'SN':
                print()
                print("\033[7;49;32mRelatório cadastrado com sucesso !!!\033[m")
                print()
                imprime_pesquisa()
                break

            print()
            print("\033[7;49;31mResponda apenas com S ou N\033[m")
            print()

        if resp == 'N':
            break




def pesquisar():
    try:
        consulta=input("Qual mes-ano quer consultar?: ")
        for relatorio in lista:
            if consulta == relatorio['Data']:
                imprime_pesquisa()
                break
        if not consulta == relatorio['Data']:
            print()
            print("\033[7;49;31mMÊS NÃO ENCONTRADO!!!\033[m")
    except(ValueError,UnboundLocalError):
        print()
        print("\033[7;49;31mPOR FAVOR CADASTRAR ALGUM RELATÓRIO!!!\033[m")


def pesquisar_referencia():
    try:
        ano_comparacao=str(input("Digite o ano de comparação: "))
        total_habitacao=0
        total_obitos=0
        for relatorio in lista:
            if str(ano_comparacao)in relatorio['Data']:
                relatorio['Habitação']
                total_habitacao+=relatorio['Habitação']
                total_obitos+=relatorio['Óbitos']

                x_comparacao=15.00

                x_ano_comparacao=100000*total_obitos/total_habitacao
                comparacao_porcentagem=x_ano_comparacao*100/x_comparacao-100

                print("-=" *30)
                print("Taxa por 100k habitantes - ",ano_comparacao,"...:%.2f "%(x_ano_comparacao))
                print("Taxa por 100k habitantes - 2019...:",x_comparacao)
                print("Comparativo","%","entre ",ano_comparacao,"- 2019...: %.1f"%(comparacao_porcentagem),"%")
                print("-=" *30)
                break
        if not str(ano_comparacao)in relatorio['Data']:
            print()
            print("\033[7;49;31mANO NÃO ENCONTRADO!!!\033[m") 
    except(UnboundLocalError,ValueError):
        print()
        print("\033[7;49;31mPOR FAVOR CADASTRAR ALGUM RELATÓRIO!!!\033[m")
         
            


def listar_tudo():
    try:
        lt=input("Deseja exibir todos os relatórios? [S/N]: ").upper()[0]
        while True:
            if lt in'SN':
                for relatorio in lista:
                    imprime_pesquisa()
            if not lt in 'SN':
                print()
                print("\033[7;49;31mPOR FAVOR RESPONDA COM [S/N]: \033[m")
            break
            
        if lt=='N':
            print("\033[1;31;43mEntão vamos ao menu -->\033[m")
        if lt=='S' and relatorio=={}:
            print()
            print("\033[2;49;43mNENHUM RELATÓRIO FOI ENCONTRADO :-( \033[m")   
    except(UnboundLocalError,ValueError,KeyError,IndexError):
        print()
        print("\033[2;49;44mNENHUM RELATÓRIO FOI ENCONTRADO :-( \033[m")  
    except(AttributeError):
        print()