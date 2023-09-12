import requests
import pandas as pd
import re

def obter_cep_por_lat_long(latitude, longitude, api_key):
    requisicao = f'https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key={api_key}' #faz a requisição do cep

    try:
        response = requests.get(requisicao)
        response.raise_for_status()  # verifica se a requisicao deu certo
        data = response.json()

        
        if data.get("results"): # extrai o cep da requisicao
            cep = None
            for result in data["results"]:
                components = result.get("components", {})
                cep = components.get("postcode")
                if cep:
                    break

            return cep

        return None  # retorna none senão tiver cep
    except requests.exceptions.RequestException as e:
        print(f"Erro de solicitação: {e}")
        return None



df = pd.read_excel('latlong.xlsx', sheet_name='latlong') #transforma o xlsx em um df para ser manipulado
lista_latitude = df['Latitude'].to_list() #transforma a coluna em lista
lista_longitude = df['Longitude'].to_list()
lista_ceps = [] 

for i in lista_latitude:
    i = float(i) #transformo a lista em float

for i in lista_longitude:
    x = re.sub(r'(\.\d+)+', '', i) #faz substituiçoes que NÃO permitem transformar em float
    i = float(x) #transformo em float

cont = 0
while cont < len(lista_latitude): #leitura de cada latitude e longitude
    latitude = lista_latitude[cont]
    longitude = lista_longitude[cont]
    api_key = 'sua_chave'

    cep = obter_cep_por_lat_long(latitude, longitude, api_key) #chama a função
    if cep: #verificação se não é none
        print(f"CEP: {cep}")
        lista_ceps.append(cep)
    else:
        print("CEP não encontrado para as coordenadas fornecidas.")    
        lista_ceps.append('Valor não encontrado')

    cont += 1


dfcep = pd.DataFrame(lista_ceps, columns=['CEPS']) #transforma a lista em df
arquivo = 'ceps.xlsx' 
dfcep.to_excel(arquivo, index=False) #extraio para um arquivo xlsx

