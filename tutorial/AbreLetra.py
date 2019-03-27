import json
import numpy as np
from pprint import pprint

with open('songs.json') as f:
    data = json.load(f)

#pprint(data)
json_data = []
originais = []
traduzidas = []
tamanho = np.count_nonzero(data)
for x in range(0, tamanho):
    if(x%2 == 0):
        json_data.append(data[x]['Original'])
        originais.append(data[x]['Original'])
    else:
        json_data.append(data[x]['Traduzido'])
        traduzidas.append(data[x]['Traduzido'])



print("Tamanho Orignal")
print(np.count_nonzero(originais))
print("Tamanho Traduzido")
print(np.count_nonzero(traduzidas))