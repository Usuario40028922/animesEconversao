import json
import os
from time import sleep

primeira_vez = True

def limpar():
  sistema = os.name  # Detecta o sistema operacional
  if sistema == 'posix':  # Para sistemas Unix (Linux, macOS)
      os.system('clear')
  elif sistema == 'nt':  # Para Windows
      os.system('cls')

def conferir_pasta():
  print(f"Diretório atual: {os.getcwd()}")
  os.chdir(r"c:\Users\Aluno\Desktop\ian")
  print(f"Diretório atual: {os.getcwd()}")
  sleep(2)
  limpar()

def outra_versao(dados, nome, manga=False):
  x = 0
  padrao = ["Título", "Gênero", "Autor", "Total de capítulos", "Possui anime?"]

  
  if not manga:
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

  elif manga:
     for manga in dados["Animes"]:
        if dados["Animes"][manga]["Titulo"] == nome:
            sleep(1)
            print(f"{manga}° da lista de animes:\n")

        for valor in dados['Animes'][f'{manga}'].values():

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
     
  if manga:
     modo_leitura = input("Deseja listar todos os mangás ou buscar um mangá por nome?\n\n\t1 - Listar todos.\n\t2 - Buscar por nome.").lower()
     
     
     if modo_leitura in ['1', 'listar', 'listar todos', 'listar tds', 'primeiro']:
        limpar()
        for anime, informacoes in dados['Manga'].items():
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
        nome = input("Insira o nome do mangá: ").upper()
      
        escolhas = ["Voltar ao menu principal"]
      
        for anime in dados["Mangas"]:
            print(nome, dados["Mangas"][anime]["Titulo"])
            if dados["Mangas"][anime]["Titulo"] == nome:
                limpar()
                print("Mangá encontrado!")
                sleep(1)
                limpar()
                print(f"{anime}° da lista:\n")

            for valor in dados['Animes'][f'{anime}'].values():

                if type(valor) == str:
                    valor = valor.lower()
                    valor = valor.title()
                
                print(f"{padrao[x]} : {valor}")
                x += 1
            if valor == "Sim":
                escolhas.insert(0, "Ver a versão de anime.")
        else:
            print("Mangá não encontrado :(")
        print("\n\n")
      
        x = 1
      

        print("O que deseja fazer agora?")
        for escolha in escolhas:
           print(f"{x} - {escolha}")
           x += 1
        escolha = input("\nInsira sua resposta: ").lower()
        
        
        if len(escolhas) == 2 and escolha in ['1', 'ver', 'ver a versão do anime', 'ver a versão do anime', 'manga', 'mangá']:
            outra_versao(dados, nome)
     
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
      
      escolhas = ["Voltar ao menu principal"]
      
      for anime in dados["Animes"]:
        print(nome, dados["Animes"][anime]["Titulo"])
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
            if valor == "Sim":
                escolhas.insert(0, "Ver a versão de mangá.")
        else:
            print("Anime não encontrado :(")
        print("\n\n")
      
      x = 1
      

      print("O que deseja fazer agora?")
      for escolha in escolhas:
          print(f"{x} - {escolha}")
          x += 1
      escolha = input("\nInsira sua resposta: ").lower()

      if len(escolhas) == 2 and escolha in ['1', 'ver', 'ver a versão do mangá', 'ver a versão do manga', 'manga', 'mangá']:
        outra_versao(dados, nome, manga=True)
            
             
def inserir_anime(dados, manga=False):
  padrao = ['Titulo', 'Genero', 'Autor', 'Episodios', 'Manga', 'Titulo', 'Genero', 'Autor', 'Capitulos', 'Anime']
  
  total_anime = list(dados['Animes'])
  total_manga = list(dados['Mangas'])

  if manga:
    print("Para inserir um mangá, siga o seguinte padrão:\nNome,Gênero,Autor,Capítulos,Possui anime? (sim ou não)\n\nEx: \n\tHunter x Hunter,Aventura,Yoshihiro Togashi,410,Sim")
    novo_manga = input("\n\t").upper().split(",")

    #Checking the data whether is equal to five detailments of the anime 
    if len(novo_manga) == 5:
        novo_manga[3] = int(novo_manga[3])
    else:
        limpar()
        print("Informações fornecidas não são igual à 5.")
        sleep(1)
        limpar()
        inserir_anime(dados, manga=True)

    
    #Making sure the user wants to insert these data into the anime.json file

    limpar()
    for datum in novo_manga:
        print(datum)
        
    agreement = input("\nSão essas mesmo as informações que deseja inserir?\n1 - Sim\n2 - Não\n\t").lower()

    if agreement in ['sim', '1', 'primeiro']:
        limpar()
        print("blz")
    #if there's another version of media

        if novo_manga[4] in ['sim', 'Sim']:
            limpar()
            print("Como existe a versão de anime, por favor, insira as informações conforme o padrao.\nTítulo,gênero,autor,quantos episódios.")
            print("Ex\n\tHunter x Hunter,aventura,Yoshiro Togashi,410.")
            novo_anime = input("\n:\t").upper().split(",")

            novo_anime[3] = int(novo_anime[3])

            limpar()

        for informacao in novo_anime:
            print(informacao)

        crtz = input("\nÉ isso aí memo?\n1 - Sim\n2 - Não\t: ").lower()

        if crtz in ['é', 'sim', 'e', 'aham', '1']:
            print("blz")
            novo_anime.append('Sim')
            limpar()

        else:
            print("Ah vai cagar vai")
            sleep(0.4)
            limpar()
            inserir_anime(dados, manga=True)
            
        if novo_anime:
            #len(novo_anime) = 5
            #len(novo_manga) = 5

            novo_manga = novo_anime + novo_manga
            manga = {}

            #len(novo_anime) = 10
            anime = {}

        for slaVei in range(len(novo_manga)):
            if slaVei <= 4:
                manga[f'{padrao[slaVei]}'] = novo_manga[slaVei]
                print(slaVei, anime, manga)
            
            elif slaVei > 4:
                anime[f'{padrao[slaVei]}'] = novo_manga[slaVei]
                print(slaVei, anime, manga)
        

        print(anime, manga)
        input(".B.")
        limpar()
        dados['Animes'][len(total_anime) + 1] = anime
        dados['Mangas'][len(total_manga) + 1] = manga
        
        print(dados)
        input("_Z_")
        with open(r'C:\Users\Aluno\Desktop\pastadoian\deverVeiga\animes.json', 'w') as animes:
            json.dump(dados, animes)
            print("V c  foi")


    else:
        print("vai la ent dnv")
        sleep(0.5)
        limpar()
        inserir_anime(dados, anime=True)
  


  elif not manga:
    limpar()
    print("Para inserir um anime, siga o seguinte padrão:\nNome,Gênero,Autor,Episódios,Possui mangá? (sim ou não)\n\nEx: \n\tHunter x Hunter,Aventura,Yoshihiro Togashi,148,Sim")
    novo_anime = input("\n\t").upper().split(",")

    #Checking the data whether is equal to five detailments of the anime 
    if len(novo_anime) == 5:
        novo_anime[3] = int(novo_anime[3])
    else:
        limpar()
        print("Informações fornecidas não são igual à 5.")
        sleep(1)
        limpar()
        inserir_anime(dados)


    #Making sure the user wants to insert these data into the anime.json file

    limpar()
    for datum in novo_anime:
        print(datum)
        
    agreement = input("\nSão essas mesmo as informações que deseja inserir?\n1 - Sim\n2 - Não\n\t").lower()

    if agreement in ['sim', '1', 'primeiro']:
        limpar()
        print("blz")


        #if there's another version of media

        if novo_anime[4] in ['sim', 'Sim']:
            limpar()
            print("Como existe a versão de mangá, por favor, insira as informações conforme o padrao.\nTítulo,gênero,autor,quantos capítulos.")
            print("Ex\n\tHunter x Hunter,aventura,Yoshiro Togashi,410.")
            novo_manga = input("\n:\t").upper().split(",")

            novo_manga[3] = int(novo_manga[3])

            limpar()
        for informacao in novo_manga:
            print(informacao)
        crtz = input("\nÉ isso aí memo?\n1 - Sim\n2 - Não\t: ").lower()

        if crtz in ['é', 'sim', 'e', 'aham', '1']:
            print("blz")
            novo_manga.append('Sim')
            limpar()

        else:
            print("Ah vai cagar vai")
            sleep(0.4)
            limpar()
            inserir_anime(dados)
            
        if novo_manga:
            #len(novo_anime) = 5
            #len(novo_manga) = 5

            novo_anime = novo_anime + novo_manga
            manga = {}

            #len(novo_anime) = 10
            anime = {}

            for slaVei in range(len(novo_anime)):
                if slaVei <= 4:
                    anime[f'{padrao[slaVei]}'] = novo_anime[slaVei]
                    print(slaVei, anime, manga)
            
                elif slaVei > 4:
                    manga[f'{padrao[slaVei]}'] = novo_anime[slaVei]
                    print(slaVei, anime, manga)
            

        print(anime, manga)
        input(".A.")
        limpar()
        dados['Animes'][len(total_anime) + 1] = anime
        dados['Mangas'][len(total_manga) + 1] = manga
        
        print(dados)
        input("_Z_")
        with open(r'C:\Users\Aluno\Desktop\pastadoian\deverVeiga\animes.json', 'w') as animes:
            json.dump(dados, animes)
            print("V c  foi")


    else:
        print("vai la ent dnv")
        sleep(0.5)
        limpar()
        inserir_anime(dados)




def escolha():
  dados = ler()
  global primeira_vez

  if primeira_vez:
    escolha = input("Seja bem-vindo ao depósito de animes!\nO que deseja?\n\n\t1 - Buscar por um anime/mangá\n\t2 - Inserir um novo anime/mangá.").lower()
    primeira_vez = False

  else:
     limpar()
     escolha = input("\nO que deseja?\n\n\t1 - Buscar por um anime\n\t2 - Inserir um novo anime.").lower()
  limpar()

  if escolha in ['1', 'buscar', 'primeiro', 'buscar por um anime', 'desgraça']:
    limpar()
    animes_ou_mangas = input("Deseja buscar um anime ou mangá?\n\t1 - Anime\n\t2 - Mangá\n\t: ")

    if animes_ou_mangas in ['1', 'animes', 'primeiro']:
      if dados['Animes'] == {}:
        print("Nenhum anime ainda adicionado!")
        sleep(2)
        limpar()
        escolha()

        procura(dados)

    elif animes_ou_mangas in ['2', 'mangas', 'segundo']:
       if dados['Mangas'] == {}:
         print("Nenhum anime ainda adicionado!")
         sleep(2)
         limpar()
         escolha()

         procura(dados, manga=True)

  elif escolha in ['2', 'segundo', 'inserir', 'inserir novo', 'inserir novo anime', 'de graça']:
    limpar()
    animes_ou_mangas = input("Deseja inserir um anime ou mangá?\n\t1 - Anime\n\t2 - Mangá\n\t: ")

    if animes_ou_mangas in ['1', 'animes', 'primeiro']:
        inserir_anime(dados)
    elif animes_ou_mangas in ['2', 'mangas', 'segundo']:
        inserir_anime()

#Início do código abaixo:
conferir_pasta()

while True:
    escolha()
    input("\n\n...")
