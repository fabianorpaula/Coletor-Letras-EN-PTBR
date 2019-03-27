import json
import numpy as np
from pprint import pprint

with open('bandas_t.json') as f:
    data = json.load(f)

#pprint(data)
json_data = data
'''
with open('quotes.json', 'r') as f:
    distros_dict = json.load(f)
'''

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
#print(np.count_nonzero(linksfinais))

