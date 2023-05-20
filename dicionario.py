user = []

def loginCadastro():
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Login")
    print("\t2 - Cadastro")
    l = input("\n\tDigite a opção escolhida\n\t> ")
    if l == '1':
        print("Tela de login")
        login = input("\n\tDigite seu login\n\t> ")
        senha = input("\n\tDigite sua senha\n\t> ")
        nome = ""
        sobrenome = ""
        email = ""
        usuario = {"nome": nome, "sobrenome": sobrenome, "email": email, "login": login, "senha": senha}
        user.append(usuario)
        print("\tLogin: {}\n\tSenha: {}".format(login, senha))
    elif l == '2': 
        print("Tela de cadastro")
        nome = input("\n\tQual o seu nome?\n\t> ").title()
        sobrenome = input("\n\tQual o seu sobrenome?\n\t> ").title()
        email = input("\n\tInforme seu email para login\n\t> ")
        login = input("\n\tDigite seu login\n\t> ")
        senha = input("\n\tEscolha sua senha\n\t> ")
        usuario = {"nome": nome, "sobrenome": sobrenome, "email": email, "login": login, "senha": senha}
        user.append(usuario)
        print("\tDados do usuario:\n\t> Nome: {} {}\n\t> Email: {}\n\t> Senha: {}".format(nome, sobrenome, email, senha))
    else:
        print("Tente novamente")
        loginCadastro()

def dados_cadastro():
    for u in user:
        nome = u["nome"] if u["nome"] else "N/A"
        sobrenome = u["sobrenome"] if u["sobrenome"] else "N/A"
        email = u["email"] if u["email"] else "N/A"
        login = u["login"] if u["login"] else "N/A"
        senha = u["senha"] if u["senha"] else "N/A"
        print("Nome:      {:<20}".format(nome))
        print("Sobrenome: {:<20}".format(sobrenome))
        print("Email:     {:<30}".format(email))
        print("Login:     {:<30}".format(login))
        print("Senha:     {:<30}".format(senha))
        print("\nEscolha uma das opções abaixo:\n")
        print("\t1 - Alterar")
        print("\t2 - Sair")
        op = input("\n\tDigite a opção escolhida\n\t> ")
        if op == '1':
            while True:
                print("\nEscolha uma das opções abaixo para alterar:\n")
                print("\t1 - Nome e Sobrenome")
                print("\t2 - Email")
                print("\t3 - Login")
                print("\t4 - Senha")
                print("\t5 - Sair")
                op_alt = input("\n\tDigite a opção escolhida\n\t> ")
                if op_alt == '1':
                    u["nome"] = input("\n\tDigite o nome\n\t>  ").title()
                    u["sobrenome"] = input("\n\tDigite o sobrenome\n\t> ").title()
                    print("Nome e Sobrenome alterados com sucesso.")
                elif op_alt == '2':
                    u["email"] = input("\n\tDigite o email\n\t> ")
                    print("Email alterado com sucesso.")
                elif op_alt == '3':
                    u["login"] = input("\n\tDigite o login\n\t> ")
                    print("Login alterado com sucesso.")
                elif op_alt == '4':
                    u["senha"] = input("\n\tDigite a senha\n\t> ")
                    print("Senha alterada com sucesso.")
                elif op_alt == '5':
                    break
        elif op == '2':
            break

bikes = [
    {"apelido": "MINHA", "marca": "caloi", "modelo": "speed", "aro": "10"},
    {"apelido": "MINHA2", "marca": "caloi", "modelo": "speed", "aro": "10"}
]

def cadastro_bike():
    marca = input("\tQual a marca da bicicleta?\n\t> ").title()
    modelo = input("\tQual o modelo da bicicleta?\n\t> ").title()
    aro = input("\tQual o aro (tamanho) da bicicleta?\n\t> ")
    apelido = input("\tDe um apelido para essa bike:\n\t> ").upper()
    bike = {"marca": marca, "modelo": modelo, "aro": aro, "apelido": apelido}
    print("\tDados da bicicleta:\n\t> Apelido: {}\n\t> Marca: {}\n\t> Modelo: {}\n\t> Aro: {}".format(apelido, marca, modelo, aro))
    bikes.append(bike)
    print("Bicicleta cadastrada com sucesso.")

def minhas_bikes():
    for bike in bikes:
        print("\tApelido: {:<10}".format(bike["apelido"]))
        print("\tMarca: {:<10}".format(bike["marca"]))
        print("\tModelo: {:<10}".format(bike["modelo"]))
        print("\tAro: {:<10}".format(bike["aro"]))
        print("\n")

def alterar_bikes():
    minhas_bikes()
    print("\n\tDigite 1 para sair para o menu ou")
    busca_bikes = input("\tDigite o apelido da bicicleta que deseja alterar\n\t> ").upper()
    for b in bikes:
        if busca_bikes == b["apelido"]:
            print("Bicicleta encontrada: ")
            print("\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(b["apelido"], b["marca"], b["modelo"], b["aro"]))
            print("\nO que gostaria de fazer com a bicicleta:\n")
            print("\t1 - Alterar")
            print("\t2 - Excluir")
            print("\t3 - Voltar ao menu principal")
            op_busca_bike = input("\n\tDigite a opção escolhida\n\t> ")
            if op_busca_bike == '1':
                    b["marca"] = input("\tQual a marca da bicicleta?\n\t> ").title()
                    b["modelo"] = input("\tQual o modelo da bicicleta?\n\t> ").title()
                    b["aro"] = input("\tQual o aro (tamanho) da bicicleta?\n\t> ")
                    b["apelido"] = input("\tDe um apelido para essa bike:\n\t> ").upper()
                    print("Dados alterados com sucesso.")
            elif op_busca_bike == '2':
                bikes.remove(b)
            elif op_busca_bike == '3':
                None
        elif busca_bikes == '1':
            None

seguros = []

def seguros_disponiveis():
    print("1 - Urbana:\n\t- Cobertura basica\n\t- Acidentes pessoais individual\n\t- Subtração da bike\n\t- Garantia Internacional.\n")
    print("2 - Performance:\n\t- Cobertura basica\n\t- Acidentes pessoais individual\n\t- Subtração da bike\n\t- Garantia Internacional\n\t- Bike bagagem.\n")
    print("3 - Mountain bike:\n\t- Cobertura basica\n\t- Acidentes pessoais individual\n\t- Subtração da bike\n\t- Garantia Internacional\n\t- Bike bagagem.\n")

def seguro_urbana():
    print("\nUrbana:\n")
    print("\tCobertura basica: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tAcidentes pessoais individual: Garante a indenização aos beneficiários legais em caso de invalidez permanente total, parcial ou morte.\n")
    print("\tSubtração da bike*: Garante a cobertura/ressarcimento total, cometida ao segurado ou no local de guarda da bike.\n")
    print("\tGarantia Internacional: Garante o pagamento da indenização por perdas e danos materiais ocorridos em território internacional.\n")
    print("Observações:\n")
    print("\t*Não haverá cobertura quando tratar-se de subtração parcial.\n")

def seguro_performance():
    print("\nPerformance:\n")
    print("\tCobertura basica: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tAcidentes pessoais individual: Garante a indenização aos beneficiários legais em caso de invalidez permanente total, parcial ou morte.\n")
    print("\tSubtração da bike*: Garante a cobertura/ressarcimento total, cometida ao segurado ou no local de guarda da bike.\n")
    print("\tGarantia Internacional: Garante o pagamento da indenização por perdas e danos materiais ocorridos em território internacional.\n")
    print("\tBike bagagem**: Garante quando há ameaça direta ou uso de violência contra o segurado ou arrombamento do local onde a bicicleta estiver guardada.\n")
    print("Observações:\n")
    print("\t*Não haverá cobertura quando tratar-se de subtração parcial.\n")
    print("\t**Para efeito dessa cobertura entende-se como bagagem: a bicicleta segurada e mala utilizada para transporte da bicicleta, comprovadamente sob a responsabilidade da cia aérea ou rodoviária. Período de cobertura: durante o trajeto de ida e volta de viagem realizada pelo segurado.\n")

def seguro_mountain():
    print("\nMountain bike:\n")
    print("\tCobertura basica: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tAcidentes pessoais individual: Garante os danos decorrentes da tentativa de subtração, incêndio, acidentes decorrentes de causa externa ou causados à bicicleta por acidente com o veículo transportador.\n")
    print("\tSubtração da bike*: Garante a cobertura/ressarcimento total, cometida ao segurado ou no local de guarda da bike.\n")
    print("\tGarantia Internacional: Garante o pagamento da indenização por perdas e danos materiais ocorridos em território internacional.\n")
    print("\tBike bagagem**: Garante o extravio da bicicleta, quando em viagens aéreas e/ou rodoviárias.\n")
    print("Observações:\n")
    print("\t*Não haverá cobertura quando tratar-se de subtração parcial.\n")
    print("\t**Para efeito dessa cobertura entende-se como bagagem: a bicicleta segurada e mala utilizada para transporte da bicicleta, comprovadamente sob a responsabilidade da cia aérea ou rodoviária. Período de cobertura: durante o trajeto de ida e volta de viagem realizada pelo segurado.\n")

def seguros_info():
    while True:
        print("Para qual seguro deseja mais informações?\n")
        print("\t1 - Urbana")
        print("\t2 - Performance")
        print("\t3 - Mountain bike")
        print("\t4 - Sair")
        opc_seg = int(input("\n\tDigite a opção escolhida\n\t> "))
        if opc_seg == 1:
            print("\n")
            seguro_urbana()
            print("\n")
        elif opc_seg == 2:
            print("\n")
            seguro_performance()
            print("\n")
        elif opc_seg == 3:
            print("\n")
            seguro_mountain()
            print("\n")
        elif opc_seg == 4:
            break

def adquirir_seguro():
            print("Escolha um dos seguros disponiveis:\n")
            print("\t1 - Urbana")
            print("\t2 - Performance")
            print("\t3 - Mountain bike")
            print("\t4 - Retornar ao menu principal")
            escolha = int(input("\nDigite a opção escolhida\n\t> "))
            if escolha == 1:
                print("\n")
                adquirir_seguro_urbana()
                print("\n")
            elif escolha == 2:
                print("\n")
                adquirir_seguro_performance()
                print("\n")
            elif escolha == 3:
                print("\n")
                adquirir_seguro_mountain()
                print("\n")
            elif escolha == 4:
                None

        

def adquirir_seguro_urbana():
    print("\nDeseja adquirir este seguro?\n")
    seguro_urbana()
    print("\nDeseja adquirir este seguro?")
    print("\t1 - Confirmar")
    print("\t2 - Retornar ao menu principal")
    confirma = input("\nDigite a opção escolhida\n\t> ")
    if confirma == '1':
        print("\nPara qual bike é o seguro?\n")
        minhas_bikes()
        print("\n\tDigite o apelido da bike\nou Digite 1 para retornar ao menu principal:")
        busca_bike = input("\n\t>  ").upper()
        for bike in bikes:
            if busca_bike == bike["apelido"]:
                print("\n\tApelido: {:<10}".format(bike["apelido"]))
                print("\tMarca: {:<10}".format(bike["marca"]))
                print("\tModelo: {:<10}".format(bike["modelo"]))
                print("\tAro: {:<10}".format(bike["aro"]))
                print("\nDeseja adquirir o seguro para esta bicicleta?")
                print("Escolha uma das opções abaixo:\n")
                print("\t1 - Confirmar")
                print("\t2 - Retornar ao menu principal")
                confirma_busca = input("\n\tDigite a opção escolhida\n\t> ")
                if confirma_busca == '1':
                    ap_seguro = bike["apelido"]
                    s_urb = {"bicicleta": ap_seguro, "tipo": "Urbana", "cob": "Cobertura basica", "ac": "Acidentes pessoais individual", "sub": "Subtração da bike", "gi": "Garantia Internacional", "bag": ""}
                    seguros.append(s_urb)
                    print("\n\tSeguro adquirido com sucesso.")
                elif confirma_busca == '2':
                    break
                else:
                    print("\nComando invalido. Tente novamente.\n")
            elif busca_bike == '1':
                break
    elif confirma == '2':
        None

def adquirir_seguro_performance():
    print("\nDeseja adquirir este seguro?\n")
    seguro_performance()
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Confirmar")
    print("\t2 - Retornar ao menu principal")
    confirma = input("\n\tDigite a opção escolhida\n\t> ")
    if confirma == '1':
        print("\nPara qual bike é o seguro?\n ")
        minhas_bikes()
        print("\n\tDigite o apelido da bike\nou Digite 1 para retornar ao menu principal:")
        busca_bike = input("\n\t>  ").upper()
        for bike in bikes:
            if busca_bike == bike["apelido"]:
                print("\n\tApelido: {:<10}".format(bike["apelido"]))
                print("\tMarca: {:<10}".format(bike["marca"]))
                print("\tModelo: {:<10}".format(bike["modelo"]))
                print("\tAro: {:<10}".format(bike["aro"]))
                print("\nDeseja adquirir o seguro para esta bicicleta?")
                print("Escolha uma das opções abaixo:\n")
                print("\t1 - Confirmar")
                print("\t2 - Retornar ao menu principal")
                confirma_busca = input("\n\tDigite a opção escolhida\n\t> ")
                if confirma_busca == '1':
                    ap_seguro = bike["apelido"]
                    s_perf = {"apelido": ap_seguro, "tipo": "Performance", "cob": "Cobertura basica", "ac": "Acidentes pessoais individual", "sub": "Subtração da bike", "gi": "Garantia Internacional", "bag": "Bike bagagem"}
                    seguros.append(s_perf)
                    print("\n\tSeguro adquirido com sucesso.")
                    break
                elif confirma_busca == '2':
                    break
                else:
                    print("\nComando invalido. Tente novamente.\n")
                    None
        if busca_bike == '1':
            None
    elif confirma == '2':
        None

def adquirir_seguro_mountain():
    print("\nDeseja adquirir este seguro?\n")
    seguro_mountain()
    print("\nEscolha uma das opções abaixo:\n")
    print("\t1 - Confirmar")
    print("\t2 - Retornar ao menu principal")
    confirma = input("\n|tDigite a opção escolhida\n\t> ")
    if confirma == '1':
        print("\nPara qual bike é o seguro?\n")
        minhas_bikes()
        print("\n\tDigite o apelido da bike\nou Digite 1 para retornar ao menu principal:")
        busca_bike = input("\n\t>  ").upper()
        for bike in bikes:
            if busca_bike == bike["apelido"]:
                print("\tApelido: {:<10}".format(bike["apelido"]))
                print("\tMarca: {:<10}".format(bike["marca"]))
                print("\tModelo: {:<10}".format(bike["modelo"]))
                print("\tAro: {:<10}".format(bike["aro"]))
                print("\nDeseja adquirir o seguro para esta bicicleta?")
                print("Escolha uma das opções abaixo:\n")
                print("\t1 - Confirmar")
                print("\t2 - Retornar ao menu principal")
                confirma_busca = input("\n\tDigite a opção escolhida\n\t> ")
                if confirma_busca == '1':
                    ap_seguro = bike["apelido"]
                    s_mount = {"apelido": ap_seguro, "tipo": "Performance", "cob": "Cobertura basica", "ac": "Acidentes pessoais individual", "sub": "Subtração da bike", "gi": "Garantia Internacional", "bag": "Bike bagagem"}
                    seguros.append(s_mount)
                    print("Seguro adquirido com sucesso.")
                    break
                elif confirma_busca == '2':
                    break
                else:
                    print("Tente novamente") 
        if busca_bike == '1':
            None
    elif confirma == '2':
        None

def meus_seguros():
    if len(seguros) != 0:
        for b in seguros:
            print("\nSeguro {:<10}".format(b["bicicleta"]))
            print("\t> {:<10}".format(b["tipo"]))
            print("\t> {:<10}".format(b["cob"]))
            print("\t> {:<10}".format(b["ac"]))
            print("\t> {:<10}".format(b["sub"]))
            print("\t> {:<10}".format(b["gi"]))
            bag = b["bag"] if b["bag"] else "N/A"
            print("\t> {:<10}".format(bag))
            print("\n")
    elif len(seguros) == 0:
        print("Você não possui seguros.")