import json
import os
from time import sleep

def limpar():
  sistema = os.name  # Detecta o sistema operacional
  if sistema == 'posix':  # Para sistemas Unix (Linux, macOS)
      os.system('clear')
  elif sistema == 'nt':  # Para Windows
      os.system('cls')

def conferir_pasta():
  print(f"Diretório atual: {os.getcwd()}")
  os.chdir(r"C:\Users\ferre\OneDrive\Área de Trabalho\Projetos\Python\dever2veiga")
  print(f"Diretório atual: {os.getcwd()}")
  sleep(2)
  limpar()

def outra_versao(dados, nome):
  x = 0
  padrao = ["Título", "Gênero", "Autor", "Total de capítulos", "Possui anime?"]
  for manga in dados["Mangas"]:
    if dados["Mangas"][manga]["Titulo"] == nome:
      sleep(1)
      print(f"{manga}° da lista de mangás:\n")

      for valor in dados['Mangas'][f'{manga}'].values():

        if type(valor) == str:
          valor = valor.lower()
          valor = valor.title()
        
        print(f"{padrao[x]} : {valor}")
        x += 1
  print("\n\n")
def ler():
  with open('animes.json', 'r') as animes:
        dados = json.load(animes)
  return dados

def procura(dados, manga=False):
  padrao = ["Título", "Gênero", "Autor", "Total de episódios", "Possui mangá?"]
  x = 0

  limpar()
  '''for manga in dados["Mangas"]:
        if dados["Mangas"][manga]["Titulo"] == nome:
          sleep(1)
          limpar()
          print(f"{manga}° da lista:\n")

          for valor in dados['Animes'][f'{anime}'].values():

            if type(valor) == str:
              valor = valor.lower()
              valor = valor.title()
            
            print(f"{padrao[x]} : {valor}")
            x += 1

            print("\n\n")'''
     

  if not manga:
     
    modo_leitura = input("Deseja listar todos os animes ou buscar um anime por nome?\n\n\t1 - Listar todos.\n\t2 - Buscar por nome.").lower()
    
    if modo_leitura in ['1', 'listar', 'listar todos', 'listar tds', 'primeiro']:
      limpar()
      for anime, informacoes in dados['Animes'].items():
        print(f"{anime}° Mangá:\n")
        
        for valor in informacoes.values():
          if type(valor) == str:
            valor = valor.lower()
            valor = valor.title()
          print(f"\t{padrao[x]} : {valor}\n")
          x += 1

          if x == 5:
            x = 0

    elif modo_leitura in ['2', 'buscar', 'buscar por nome', 'segundo']:
      limpar()
      nome = input("Insira o nome do anime: ").upper()
      for anime in dados["Animes"]:
          if dados["Animes"][anime]["Titulo"] == nome:
            limpar()
            print("Anime encontrado!")
            sleep(1)
            limpar()
            print(f"{anime}° da lista:\n")

            for valor in dados['Animes'][f'{anime}'].values():

              if type(valor) == str:
                valor = valor.lower()
                valor = valor.title()
              
              print(f"{padrao[x]} : {valor}")
              x += 1

          print("\n\n")
      
      x = 1
      escolhas = ["Voltar ao menu principal"]

      if valor == "Sim":
        escolhas.insert(0, "Ver a versão de mangá.")

      print("O que deseja fazer agora?")
      for escolha in escolhas:
          print(f"{x} - {escolha}")
          x += 1
      escolha = input("\nInsira sua resposta: ").lower()

      if len(escolhas) == 2 and escolha in ['1', 'ver', 'ver a versão do mangá', 'ver a versão do manga', 'manga', 'mangá']:
        outra_versao(dados, nome)
            
             
def inserir_anime(dados):
   limpar()
   print("Para inserir um anime, siga o seguinte padrão:\nNome, Gênero, Autor, Episódios, Possui mangá? (sim ou não)\n\nEx: ")

def escolha(primeira_vez=True):
  dados = ler()

  if primeira_vez:
    escolha = input("Seja bem-vindo ao depósito de animes!\nO que deseja?\n\n\t1 - Buscar por um anime\n\t2 - Inserir um novo anime.").lower()
  else:
     limpar()
     escolha = input("\nO que deseja?\n\n\t1 - Buscar por um anime\n\t2 - Inserir um novo anime.").lower()
  limpar()

  if escolha in ['1', 'buscar', 'primeiro', 'buscar por um anime', 'desgraça']:
    if dados['Animes'] == {}:
       print("Nenhum anime ainda adicionado!")
       sleep(2)
       limpar()
       escolha()
    
    procura(dados)

  elif escolha in ['2', 'segundo', 'inserir', 'inserir novo', 'inserir novo anime', 'de graça']:
    inserir_anime()


#Início do código abaixo:
conferir_pasta()
escolha()