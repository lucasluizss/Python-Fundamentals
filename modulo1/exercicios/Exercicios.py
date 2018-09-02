import operator
from  lib.scrapy_table import Scrapy_Table
url="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"

url1 = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"

url2 = "https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios"

site_connect = Scrapy_Table(url)
tables = site_connect.get_tables(0)

site_connect1 = Scrapy_Table(url1)
tables1 = site_connect1.get_tables(1)

site_connect2 = Scrapy_Table(url2)
tables2 = site_connect2.get_tables(1)

#1. Listar o nome de todos os municípios do Brasil com o código do IBGE: Exemplo de Resposta:
def exercise1():
  print('N IBGE  Municipio\n--------------------')

  for linha in tables[1:]:
    print('{0} {1}'.format(linha[1], linha[2]))

#2. Listar os municípios com menos de 70.000 habitantes:
def exercise2():
  print('N IBGE  Municipio\n--------------------')
  list_municipios = list(filter(lambda x : int(x[4]) < 70000, tables[1:]))
  
  for linha in list_municipios:
    print('{0} {1}'.format(linha[1], linha[2]))
  
#3. Mostrar o estado que tem o maior número de cidades acima 100.000 habitantes:
def exercise3():  
  states = {}
  for item in tables[1:]:    
    if item[3] not in states and int(item[4]) > 100000:
      states[item[3]] = 0
    elif item[3] in states and int(item[4]) > 100000:
      states[item[3]] += 1

  winner = max(states.items(), key=operator.itemgetter(1))[0]

  print('{0}: {1}'.format(winner, states[winner]))

#4. Qual município tem o menor número de habitantes. Mostre também em qual estado está esse município:
def exercise4():
  municipios = {}
  for item in tables[1:]:    
    municipios['{0}-{1}'.format(item[2], item[3])] = int(item[4])
  
  winner = min(municipios.items(), key=operator.itemgetter(1))[0]

  municipio = winner.split('-')[0]
  state = winner.split('-')[1]

  print('O município com a menor quantidade de habitantes é {0} com {1} habitantes e fica em {2}'.format(municipio, municipios[winner], state))

#5. Mostre a taxa de fecundidade para os estados:
  #que tem a cidade com maior número de habitantes
  #que tem a cidade com menor número de habitantes
def exercise5():
  cidades = {}
  for item in tables[1:]:    
    cidades['{0}-{1}'.format(item[2], item[3])] = int(item[4])
  
  greaterCity = max(cidades.items(), key=operator.itemgetter(1))[0]
  estadoGreaterCity = str(greaterCity.split('-')[1])

  lessCity = min(cidades.items(), key=operator.itemgetter(1))[0]
  estadoLessCity = str(lessCity.split('-')[1])

  for item in tables1[1:]:
    if str(item[1]) == estadoGreaterCity:
      print('Maior:\n{0} - {1}\n'.format(estadoGreaterCity, item[2]))
    elif str(item[1]) == estadoLessCity:
      print('Menor:\n{0} - {1}\n'.format(estadoLessCity, item[2]))

#6. Mostrar o total da população brasileira:
def exercise6():
  print('População brasileira: ', sum(map(lambda x: int(x[4]), tables[1:])))
  
#7. Quantos estados brasileiros estão abaixo da taxa de reposição populacional (2.10 filhos):
def exercise7():  
  beginTax = [x for x in tables1[1:] if x[1] == 'Taxa de reposição populacional'][0][2]  
  print('Estados brasileiros abaixo da taxa de reposição: ', 
        len(list(filter(lambda x: x[2] < beginTax, tables1[1:]))))

#8. Quantos habitantes moram no sudeste (São Paulo, Minas Gerais, Rio de Janeiro, Espírito Santo):
def exercise8():
  sudeste = ['São Paulo', 'Minas Gerais', 'Rio de Janeiro', 'Espírito Santo']
  habitantes_sudeste = list(filter(lambda x: x[3] in sudeste, tables[1:]))
  
  print('Habitantes no sudeste: ', sum(map(lambda x: int(x[4]), habitantes_sudeste)))

#9. Mostrar o nome, número de habitantes e taxa de fecundidade para as cidades brasileiras que estão 
#com taxa de homicídio acima de 60 por 100 Mil:
def exercise9():
  filtro_homicidio = list(filter(lambda x: float(x[5].replace(',','.')) > 60 and x[2] == 'Brasil', tables2[1:]))
  filtro_fecundidade = {}
  filtro_municipio = {}
  
  # município - estado
  for item in tables[1:]:
    filtro_municipio[str(item[2])] = item[3]

  # estado - fecundidade
  for item in tables1[1:]:
    filtro_fecundidade[item[1]] = item[2]

  for item in filtro_homicidio:
    if str(item[1]) in filtro_municipio:
      taxa_fecundidade = filtro_fecundidade[filtro_municipio[str(item[1])]]

    print('\nNome: {0}\nNúmero de Habitantes: {1}\nTaxa de fecundidade: {2}'.format(item[1], item[4], taxa_fecundidade))
  
#10. Quantos habitantes brasileiros estão morando nas 50 cidades mais violentas do mundo:
def exercise10():
  br_list = list(filter(lambda x: x[2] == 'Brasil', tables2[1:]))

  sum_br = sum(map(lambda x: int(x[4].replace(' ','')), br_list))

  print(sum_br, ' Brasileiros.')

