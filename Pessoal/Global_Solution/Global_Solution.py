#Gabriel Costa Marques RM: 94012
#Guilherme Colleto DE Oliveira RM:93818 
#Raphael Rezende Silveira Junior RM: 94489




import funcoes as g


txt_op = "Digite uma opção: "
print()
print("\033[1;49;32m“3.6 Até 2020, reduzir pela metade as mortes e os ferimentos","\n","globais por acidentes em estradas. No Brasil, em 2015","\n","ocorreu 19 mortes de trânsito para cada 100 mil habitantes.","\n", "Em 2019, a taxa reduziu para 15 mortes para cada 100 mil habitantes,","\n", "mas ainda longe da meta da ODS.”\033[m")


g.mostrar_opcao()
op = int(input(txt_op))
try:

    while op>0:
        if op == 1: 
            g.cadastrar()

        elif op == 2:   
            g.pesquisar()

        elif op == 3:
            g.pesquisar_referencia()

        elif op == 4:
            g.listar_tudo()
        else:
            print()
            print("\033[7;49;31mDIGITE APENAS AS OPÇÕES DISPONÍVEIS!\033[m")
        g.mostrar_opcao()
        op = int(input(txt_op))
except (ValueError):
    print()
    print("\033[7;49;31mDIGITE APENAS AS OPÇÕES DISPONÍVEIS!\033[m")
