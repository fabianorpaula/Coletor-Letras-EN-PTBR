import json
import numpy as np
from pprint import pprint
import os
import os.path


#print("Current: "+os.getcwd())


with open('/home/fabiano/eclipse-workspace/BuscaLetras/tutorial/bandas_t.json') as f:
    data = json.load(f)



#print(data)


json_data = data


musicas = []
linksfinais = []

for linksX in json_data:
    #print(linksX['Links'])
    playlist = linksX['Links']
    tamanho = np.count_nonzero(playlist)
    #print(tamanho)
    for x in range(0, tamanho):
        musicas.append(playlist[x])
        novolink = "https://www.letras.mus.br/"+playlist[x]
        linksfinais.append(novolink)

#print(np.count_nonzero(musicas))
start_urls = [
        'https://www.letras.mus.br/muse/27396/traducao.html',
        'https://www.letras.mus.br/the-killers/155055/traducao.html',
    ]
#FUNCIOANDO
print(linksfinais[0])
print(start_urls[0])
