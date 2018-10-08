from  lib.scrapy_dadosAbertos import DadosAbertos
import datetime

api = DadosAbertos()

class Exercicios2:

  @staticmethod
  def exercise1():
    print('\n1. Listar os nomes em maiúscula dos deputados que tenham mais de 50 anos de idade: \n')
    year = datetime.datetime.now().year

    for x in api.deputados():
      deputado = api.deputado_id(int(x['id']))
      idade = year - int(deputado['dataNascimento'][:4])

      if idade > 50:
        print('Nome: {0}\nIdade: {1}\n'.format(deputado['nomeCivil'].upper(), idade))

  @staticmethod
  def exercise2():
    print('\n2. Listar as deputadas: \n')

    for x in api.deputados():
      deputado = api.deputado_id(int(x['id']))

      if deputado['sexo'] == 'F':
        print('Nome: {0}\n'.format(deputado['nomeCivil'].upper()))

  @staticmethod
  def exercise3():
    print('\n3. Mostre a soma dos gastos de um deputados especificos:\n')
    
    nome_deputado = input('Informe o nome do deputado: ').upper()

    for x in api.deputados():
      deputado = api.deputado_id(int(x['id']))
      
      if nome_deputado in deputado['nomeCivil'].upper():
        total_despesas = api.deputado_despesas(int(x['id']))
        print(total_despesas)
    
  @staticmethod
  def exercise4():
    print('\n4. Mostre o nome dos 3 deputados com maiores gastos:\n')
    print(api.deputados())

  @staticmethod
  def exercise5():
    print('\n5. Mostre as informações formatadas da comissão sobre \'PEC57402\':\n')

  @staticmethod
  def exercise6():
    print('\n6. Mostre os gastos mais comum dos deputados:\n')

  @staticmethod
  def exercise7():
    print('\n7. Mostre os nomes dos 3 deputados que tiveram o menor gastos:\n')

  @staticmethod
  def exercise8():
    print('\n8. Mostre os deputados que participam de mais comissão:\n')

  @staticmethod
  def exercise9():
    print('\n9. Mostre todos os votos (a favor ou contra) de um deputado e a descrição dos projetos:\n')

  @staticmethod
  def exercise10():
    print('\n10. Apresente todos os projetos para um usuário e solicite a votaçao para cada projeto. Verifique qual deputado votou mais semestre ao usuário.\n')

