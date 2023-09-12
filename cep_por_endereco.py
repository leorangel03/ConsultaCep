import pandas as pd
import requests

enderecos = pd.read_excel("baseEnderecos.xlsx", sheet_name='ruas') #transforma xlsx em df

listaEnderecos = enderecos['ENDEREÇO'].tolist() #pega lista do df e colca em coluna
listaMunicipio = enderecos['CIDADE'].tolist()
enderecosTratado = []

for i in listaEnderecos: #varreção por cada endereço para "padronizar" o formato

    x = str(i)
    caracteres = [',', '-', '&', '_', '(', '/']
    y = ""

    for i in x:
        if i not in caracteres:
            y += i
        else:
            break

	#serie de verificações e tratamentos por cada caso
    if y[0:2] == 'R.':
        y = y[2:]

    if y[0:3] == 'Rua':
        y = y[3:]

    if y[0] == ' ':
        y = y[1:]

    if y[-1] == ' ':
        y = y[:-1]
    
    if y[0:3] == 'Dr.' or y[0:3] == 'DR.':
        y = y[3:]

    if y[0:4] == 'Eng.' or y[0:4] == 'ENG.':
        y = y[4:]

    if y[0] == ' ':
        y = y[1:]

    enderecosTratado.append(y)
    


listaCEP = []

def verificaCep(cidade, rua): #criacao de funcao para realizar requerimento
    try: #tentativa de buscar endereço

        uf ='SP'
        link = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'
        response = requests.get(link, verify=False)
        requisicao = response.json() #transforma o .json em array de dict

        if len(requisicao) == 0: #caso o array esteja vazio
            # print('Endereço not found')
            listaCEP.append("Endereço não encontrado")
        else:
            x = str(requisicao[0]['cep']) #pegar o primeiro dict do array na chave do cep
            # print(f"O cep é: {x}")
            listaCEP.append(x)
    except Exception as e: #caso nao aceite a entrada da requisição
        listaCEP.append('Error')

for indice, rua in enumerate(enderecosTratado): #varreção da lista dos enderecos tratados
    cidade = listaMunicipio[indice] #usando o indice da rua respectivo a cidade
    verificaCep(cidade, rua) #chama a função 
