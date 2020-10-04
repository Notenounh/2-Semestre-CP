def comparation ():     
    
    arq = input("Insira o nome do arquivo original: ")
    arq_bck = input("Insira o arquivo de comparação: ")

    open_arq = (open(arq, 'r').read())
    open_arq_bck = (open(arq_bck, 'r').read())

    if open_arq != open_arq_bck:
        ask = input("O arquivo está manipulado. Deseja restaurá-lo? (Sim/Nao) ").lower()
        if ask == "sim":
            archive = open(arq, 'r') 
            content = archive.readlines()
            archive.close()
            #Lê as mudanças
            archive = open(arq_bck, 'w') 
            archive.writelines(content)    
            #Aplica as mudanças
            archive.close()
            print("Backup realizado com sucesso!")
    else:
        print("Arquivo integro. ")


comparation()
