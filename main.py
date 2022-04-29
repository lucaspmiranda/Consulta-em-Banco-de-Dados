import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxxxxxxx",
    database="hamb"
    )

class cliente:
    def __init__(self, nome, rua, numero, bairro, telefone, email, senha, emailRecuperacao):
        self.nome=nome
        self.rua=rua
        self.numero=numero
        self.bairro=bairro
        self.telefone=telefone
        self.email=email
        self.senha=senha
        self.emailRecuperacao=emailRecuperacao
            
    def incluir(self):
        mycursor = mydb.cursor()

        sql = "INSERT INTO cliente (nome, rua, numero, bairro, telefone, email,senha, emailRecuperacao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.nome, self.rua, self.numero, self.bairro, self.telefone, self.email, self.senha, self.emailRecuperacao)
        mycursor.execute(sql, val)

        mydb.commit()

        print("Cadastro inserido com sucesso!")

    def mostrar(self):
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM cliente")

        myresult = mycursor.fetchall()

        print('\n')
        for x in myresult:
            print(x)
        print('\n')

    def pesquisar(self, id):
        if id == 1:
            pesqNome=input('Qual nome você deseja pesquisar?')
            
            mycursor = mydb.cursor()

            sql = "SELECT * FROM cliente WHERE nome = %s"
            valNome=(pesqNome, )

            mycursor.execute(sql, valNome)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
        
        elif id == 2:
            pesqRua=input('Qual rua você deseja pesquisar?')
            
            mycursor = mydb.cursor()

            sql = "SELECT * FROM cliente WHERE rua = %s"
            valRua=(pesqRua, )

            mycursor.execute(sql, valRua)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

        elif id == 3:
            pesqNumero=input('Qual numero você deseja pesquisar?')
            
            mycursor = mydb.cursor()

            sql = "SELECT * FROM cliente WHERE numero = %s"
            valNumero=(pesqNumero, )

            mycursor.execute(sql, valNumero)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

        elif id == 4:
            pesqBairro=input('Qual bairro você deseja pesquisar?')
            
            mycursor = mydb.cursor()

            sql = "SELECT * FROM cliente WHERE bairro = %s"
            valBairro=(pesqBairro, )

            mycursor.execute(sql, valBairro)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

        elif id == 5:
            pesqTelefone=input('Qual telefone você deseja pesquisar?')
            
            mycursor = mydb.cursor()

            sql = "SELECT * FROM cliente WHERE telefone = %s"
            valTelefone=(pesqTelefone, )

            mycursor.execute(sql, valTelefone)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

        elif id == 6:
            pesqEmail=input('Qual e-mail você deseja pesquisar?')
            
            mycursor = mydb.cursor()

            sql = "SELECT * FROM cliente WHERE email = %s"
            valEmail=(pesqEmail, )

            mycursor.execute(sql, valEmail)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

    def excluir(self):
        mycursor = mydb.cursor()

        excEmail=input('Digite um e-mail para excluir um cadastro: ')

        sql = "DELETE FROM cliente WHERE email = %s"
        valEmail=(excEmail, )

        mycursor.execute(sql, valEmail)

        mydb.commit()

        print("Cadastro deletado com sucesso!")

    def alterar(self):

        print(''' [1] Nome
              [2] Rua
              [3] Numero
              [4] Bairro
              [5] Telefone
              [6] E-mail
              [7] Senha
              [6] E-mail de recuperação''')
        
        id = int(input('Selecione uma opção para alterar: '))    

        if id == 1:
            alterNome=input('Digite o novo nome: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET nome = %s WHERE email = %s"
            altNome=(alterNome, self.email)

            mycursor.execute(sql, altNome)

            mydb.commit()

            print("Nome alterado com sucesso!")
        
        elif id == 2:
            alterRua=input('Digite a nova rua: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET rua = %s WHERE email = %s"
            altRua=(alterRua, self.email)

            mycursor.execute(sql, altRua)

            mydb.commit()

            print("Rua alterado com sucesso!")          

        elif id == 3:
            alterNumero=input('Digite o novo numero: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET numero = %s WHERE email = %s"
            altNumero=(alterNumero, self.email)

            mycursor.execute(sql, altNumero)

            mydb.commit()

            print("Numero alterado com sucesso!")          

        elif id == 4:
            alterBairro=input('Digite o novo bairro: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET bairro = %s WHERE email = %s"
            altBairro=(alterBairro, self.email)

            mycursor.execute(sql, altBairro)

            mydb.commit()

            print("Bairro alterado com sucesso!")   

        elif id == 5:
            alterTelefone=input('Digite o novo telefone: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET telefone = %s WHERE email = %s"
            altTelefone=(alterTelefone, self.email)

            mycursor.execute(sql, altTelefone)

            mydb.commit()

            print("Telefone alterado com sucesso!")   

        elif id == 6:
            alterEmail=input('Digite o novo e-mail: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET email = %s WHERE email = %s"
            altEmail=(alterEmail, self.email)

            mycursor.execute(sql, altEmail)

            mydb.commit()

            print("E-mail alterado com sucesso!")   

        elif id == 7:
            alterSenha=input('Digite a nova senha: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET senha = %s WHERE email = %s"
            altSenha=(alterSenha, self.email)

            mycursor.execute(sql, altSenha)

            mydb.commit()

            print("Senha alterado com sucesso!")   

        elif id == 8:
            alteremailRecuperacao=input('Digite o novo e-mail de recuperação: ')

            mycursor = mydb.cursor()

            sql = "UPDATE cliente SET emailRecuperacao = %s WHERE email = %s"
            altemailRecuperacao=(alteremailRecuperacao, self.email)

            mycursor.execute(sql, altemailRecuperacao)

            mydb.commit()

            print("E-mail de recuração alterado com sucesso!")

opção = 0
while opção != 6:
    print(''' [1] Incluir cadastro
              [2] Alterar cadastro
              [3] Exluir cadastro
              [4] Mostrar todos os cadastros
              [5] Realizar pesquisa parametrizada
              [6] Sair''')
    opção = int(input('>>>>> Qual é a sua opção :'))

    if opção == 1:

        incluirNome = input('Digite um nome: ')
        incluirRua = input('Digete em rua: ')
        incluirNumero = input('Digite um numero: ')
        incluirBairro = input('Difite o bairro: ')
        incluirTelefone = input('Digite o telefone: ')
        incluirEmail = input('Digite um email: ')
        incluirSenha = input('Digite uma senha: ')
        incuiremailRecuperacao = input('Digite um e-mail de recuperação: ')

        varInserir = cliente(incluirNome, incluirRua, incluirNumero, incluirBairro, incluirTelefone, incluirEmail, incluirSenha, incuiremailRecuperacao)

        varInserir.incluir()

    elif opção == 2:

        varalt=input('Digite seu e-mail: ')



        incluirNome = ''
        incluirRua = ''
        incluirNumero = ''
        incluirBairro = ''
        incluirTelefone = ''
        incluirEmail = varalt
        incluirSenha = ''
        incuiremailRecuperacao = ''

        varAlterar=cliente(incluirNome, incluirRua, incluirNumero, incluirBairro, incluirTelefone, incluirEmail, incluirSenha, incuiremailRecuperacao)

        varAlterar.alterar()

    elif opção == 3:

        incluirNome = ''
        incluirRua = ''
        incluirNumero = ''
        incluirBairro = ''
        incluirTelefone = ''
        incluirEmail = ''
        incluirSenha = ''
        incuiremailRecuperacao = ''

        varExcluir=cliente(incluirNome, incluirRua, incluirNumero, incluirBairro, incluirTelefone, incluirEmail, incluirSenha, incuiremailRecuperacao)

        varExcluir.excluir()

    elif opção == 4:
        
        incluirNome = ''
        incluirRua = ''
        incluirNumero = ''
        incluirBairro = ''
        incluirTelefone = ''
        incluirEmail = ''
        incluirSenha = ''
        incuiremailRecuperacao = ''

        varMostrar=cliente(incluirNome, incluirRua, incluirNumero, incluirBairro, incluirTelefone, incluirEmail, incluirSenha, incuiremailRecuperacao)

        varMostrar.mostrar()

    elif opção == 5:    

        print(''' [1] Nome
              [2] Rua
              [3] Numero
              [4] Bairro
              [5] Telefone
              [6] E-mail''')
        
        varPesquisa = input('Selecione uma opção para pesquisar: ')

        incluirNome = ''
        incluirRua = ''
        incluirNumero = ''
        incluirBairro = ''
        incluirTelefone = ''
        incluirEmail = ''
        incluirSenha = ''
        incuiremailRecuperacao = ''

        varPesquisar=cliente(incluirNome, incluirRua, incluirNumero, incluirBairro, incluirTelefone, incluirEmail, incluirSenha, incuiremailRecuperacao)

        varPesquisar.pesquisar(int(varPesquisa))

    elif opção == 6:
        print('Teste 6')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa')
