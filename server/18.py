def verifica_idade(idade):
    if (idade < 18):
        print("Não está liberado")
    elif (18<=idade<21):
        print("Liberado BRASIL")
    else:
        print("Liberado EUA e BRASIL")