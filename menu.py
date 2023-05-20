from dicionario import *

print("Bem vindo a Porto Seguro Bike")
loginCadastro()

while True :  
    
    print("\nMenu:")
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Cadastro de bicicletas.")
    print("\t2 - Minhas Bicicletas.")
    print("\t3 - Seguros Disponiveis.")
    print("\t4 - Meus Seguros.")
    print("\t5 - Vistoria.")
    print("\t6 - Historico.")
    print("\t7 - Dados do usuario.")
    print("\t8 - Sair.")
       
    menu = input("\n\tDigite a opção escolhida\n\t> ")

    if menu == '1':
        print("\nCadastro de bicicletas.\n")
        cadastro_bike()
    elif menu == '2':
        print("\nMinhas bicicletas.\n")
        minhas_bikes()
        print("\nEscolha uma das opções abaixo:\n")
        print("\t1 - Alterar dados.")
        print("\t2 - Voltar ao menu principal.")
        op_minhas_bikes = input("\n\tDigite a opção escolhida\n\t> ")
        if op_minhas_bikes == '1':
            print("\n")
            alterar_bikes()
        elif op_minhas_bikes == '2':
            None
        else:
            print("\nComando invalido. Tente novamente.\n")
    elif menu == '3':
        while True:
            print("\nSeguros disponiveis.\n")
            seguros_disponiveis()
            print("\nEscolha uma das opções abaixo:\n")
            print("\t1 - Mais informações")
            print("\t2 - Adquirir novo seguro")
            print("\t3 - Voltar ao menu principal")
            info = input("\n\tDigite a opção escolhida\n\t> ")
            if info == '1':
                print("\nSeguros:\n")
                seguros_info()
            elif info == '2':
                print("\nAdquirir seguro:\n")
                adquirir_seguro()
                break
            elif info == '3':
                break
            else:
                print("\nComando invalido. Tente novamente.\n")
    elif menu == '4':
        print("\nMeus seguros\n")
        meus_seguros()
    elif menu == '5':
        print("Vistoria")
    elif menu == '6':
        print("\nHistorico\n")
    elif menu == '7':
        print("\nDados do usuario\n")
        dados_cadastro()
        print("\n")
    elif menu == '8':
        print("\nAté logo!")
        break
    else:
        print("\nComando invalido. Tente novamente.\n")