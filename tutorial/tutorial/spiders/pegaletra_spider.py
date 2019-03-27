import json
import numpy as np
from pprint import pprint
import os
import os.path
import scrapy


class QuotesSpider(scrapy.Spider):
    #Abre Arquivo Com AS bandas
    with open('/home/fabiano/eclipse-workspace/BuscaLetras/tutorial/bandas_t.json') as f:
        data = json.load(f)
    
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
            
            
    name = "letras"
    '''
    start_urls = [
        'https://www.letras.mus.br/muse/27396/traducao.html',
        'https://www.letras.mus.br/the-killers/155055/traducao.html',
    ]
    '''
    start_urls  = linksfinais

    def parse(self, response):
        for quote in response.css('div.cnt-trad_l'):
            yield {
                
                'Original': quote.css('::text').getall(),
                #'Traduzido': quote.css('div.cnt-trad_r.p::text').getall(),
                
            }
        for quote in response.css('div.cnt-trad_r'):
            yield {
                
                #'Original': quote.css('div.cnt-trad_l p::text').getall(),
                'Traduzido': quote.css('::text').getall(),
                
            }