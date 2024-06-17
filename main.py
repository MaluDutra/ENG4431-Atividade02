from bs4 import BeautifulSoup
from time import sleep
import requests
import re
from webscrapping import entrar_conta,cadastrar_conta

#Funções
def menu():
  print('\n\n')
  print('='*90)
  print("\nBoas Vindas à Wiki sobre o Studio Ghibli!!\n")
  print("Escolha uma das opções abaixo:")
  print("1 - Consultar data de fundação")
  print("2 - Consultar fundadores")
  print("3 - Consultar local da sede")
  print("4 - Consultar atual presidente e vice-presidente")
  print("5 - Listar filmes")
  print("6 - Listar curta-metragens")
  print("7 - Listar séries")
  print("8 - Listar documentários")
  print("9 - Listar jogos")
  print("10 - Listar filmes antes da fundação do Studio Ghibli")
  print("11 - Extrair imagem de um filme")
  print("12 - Entrar na conta do site do Studio Ghibli")
  print("13 - Cadastrar conta no site Studio Ghibli")
  print("14 - Sair\n")
  print('='*90,'\n')
  return

def acessar_pagina(url):
  headers = {
    "User-Agent": "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"
  }
  response = requests.get(url,headers=headers)
  if response.status_code !=200:
    return False
  sopa = BeautifulSoup(response.text, "html.parser")
  return sopa

def busca(lista, palavra):
  for (i,elemento) in enumerate(lista):
    if palavra in elemento.text:
      return i
  return None

def salvar_arquivo(texto, nome_arquivo):
  with open(nome_arquivo, "a") as arquivo:
    arquivo.write(texto + '\n')
  return

    
#Bloco Principal
continuar = True

while continuar:
  menu()
 
  sopa_dados = acessar_pagina("https://studioghibli.com.br/studioghibli/")
  sopa_filmes = acessar_pagina("https://studioghibli.com.br/filmografia/")
  if not sopa_dados or not sopa_filmes:
    print("Erro ao acessar a página! Tente novamente mais tarde.")
    break
  
  try:
    opcao = int(input("Digite o número da opção desejada: "))
  except ValueError:
    print("Opção inválida. Digite um número!")
    opcao = False
  
  if opcao == 1:
    lista = sopa_dados.find_all('td')
    indice = busca(lista, "Fundação")
    if not indice:
      print("Não foi possível encontrar a data de fundação do Studio Ghibli.")
      break
    print("\nA data de fundação do Studio Ghibli é: ", lista[indice+1].text)
    salvar_arquivo('Data: ' + lista[indice+1].text, "dados.txt")
  
  elif opcao == 2:
    lista = sopa_dados.find_all('td')
    indice = busca(lista, "Fundadores")
    if not indice:
      print("Não foi possível encontrar os fundadores do Studio Ghibli.")
      break
    print("\nOs fundadores do Studio Ghibli são: \n")
    print(lista[indice+1].text)
    salvar_arquivo('Fundadores:\n' + lista[indice+1].text, "dados.txt")
  
  elif opcao == 3:
    lista = sopa_dados.find_all('td')
    indice = busca(lista, "Sede")
    if not indice:
      print("Não foi possível encontrar a sede do Studio Ghibli.")
      break
    print("\nO local da sede do Studio Ghibli é: ", lista[indice+1].text)
    salvar_arquivo('Sede: ' + lista[indice+1].text, "dados.txt")
  
  elif opcao == 4:
    lista = sopa_dados.find_all('td')
    indice1 = busca(lista, "Presidente")
    if not indice1:
      print("Não foi possível encontrar o presidente do Studio Ghibli.")
      break
    indice2 = busca(lista, "Vice-presidente")
    if not indice2:
      print("Não foi possível encontrar o vice-presidente do Studio Ghibli.")
      break
    print("\nO atual presidente e o vice do Studio Ghibli são: ", lista[indice1+1].text,'e',lista[indice2+1].text)
    salvar_arquivo('Presidente: ' + lista[indice1+1].text, "dados.txt")
    salvar_arquivo('Vice-presidente: ' + lista[indice2+1].text, "dados.txt")
  
  elif opcao == 5:
    lista = sopa_filmes.find_all('p')
    indice = busca(lista, "Nausicaä do Vale do Vento (1984)")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    indice_fim = busca(lista, "On Your Mark")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    print("\n\nListando filmes...\n")
    for filme in lista[indice:indice_fim]:
      auxiliar = filme.find_all('br')
      if len(auxiliar) == 1:
        listinha = filme.text.split('\n')
        print("%s %s" %(listinha[0],listinha[1]))
        salvar_arquivo(listinha[0] + listinha[1], "dados.txt")
      else:
        print(filme.text)
        salvar_arquivo(filme.text, "dados.txt")

  elif opcao == 6:
    lista = sopa_filmes.find_all('p')
    indice = busca(lista, "On Your Mark")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    indice_fim = busca(lista, "Ronja, A Filha do Ladrão")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    print("\n\nListando curta-metragens...\n")
    for filme in lista[indice:indice_fim]:
      auxiliar = filme.find_all('br')
      if len(auxiliar) == 1:
        listinha = filme.text.split('\n')
        print("%s %s" %(listinha[0],listinha[1]))
        salvar_arquivo(listinha[0] + listinha[1], "dados.txt")
      else:
        print(filme.text)
        salvar_arquivo(filme.text, "dados.txt")
  
  elif opcao == 7:
    lista = sopa_filmes.find_all('p')
    indice = busca(lista, "Ronja, A Filha do Ladrão")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    indice_fim = busca(lista, "Nandaro")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    print("\n\nListando séries...\n")
    for serie in lista[indice:indice_fim]:
      auxiliar = serie.find_all('br')
      if len(auxiliar) == 1:
        listinha = serie.text.split('\n')
        print("%s %s" %(listinha[0],listinha[1]))
        salvar_arquivo(listinha[0] + listinha[1], "dados.txt")
      else:
        print(serie.text)
        salvar_arquivo(filme.text, "dados.txt")
  
  elif opcao == 8:
    lista = sopa_filmes.find_all('p')
    indice = busca(lista, "The Story of Yanagawa’s Canals (2003)")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    indice_fim = busca(lista, "Ni no Kuni: Dominion of the Dark Djinn (2010)")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    print("\n\nListando documentários...\n")
    for filme in lista[indice:indice_fim]:
      auxiliar = filme.find_all('br')
      if len(auxiliar) == 1:
        listinha = filme.text.split('\n')
        print("%s %s" %(listinha[0],listinha[1]))
        salvar_arquivo(listinha[0] + listinha[1], "dados.txt")
      else:
        print(filme.text)
        salvar_arquivo(filme.text, "dados.txt")
  
  elif opcao == 9:
    lista = sopa_filmes.find_all('p')
    indice = busca(lista, "Ni no Kuni: Dominion of the Dark Djinn (2010)")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    indice_fim = busca(lista, "Animações ocidentais")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    print("\n\nListando jogos...\n")
    for jogo in lista[indice:indice_fim]:
      auxiliar = jogo.find_all('br')
      if len(auxiliar) == 1:
        listinha = jogo.text.split('\n')
        print("%s %s" %(listinha[0],listinha[1]))
        salvar_arquivo(listinha[0] + listinha[1], "dados.txt")
      else:
        print(jogo.text)
        salvar_arquivo(filme.text, "dados.txt")
  
  elif opcao == 10:
    lista = sopa_filmes.find_all('p')
    indice = busca(lista, "Horus: O Príncipe do Sol (1968)")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    indice_fim = busca(lista, "The Story of Yanagawa’s Canals")
    if not indice:
      print("Não foi possível encontrar os filmes do Studio Ghibli.")
      break
    print("\n\nListando filmes pré-Studio Ghibli...\n")
    for filme in lista[indice:indice_fim]:
      auxiliar = filme.find_all('br')
      if len(auxiliar) == 1:
        listinha = filme.text.split('\n')
        print("%s %s" %(listinha[0],listinha[1]))
        salvar_arquivo(listinha[0] + listinha[1], "dados.txt")
      else:
        print(filme.text)
        salvar_arquivo(filme.text, "dados.txt")
  
  elif opcao == 11:
    nome_filme = input("Digite o nome do filme: ")
    img_poster = sopa_filmes.find('img', attrs={
      "data-image-title": nome_filme
    }) 
    
    if img_poster is None:
      ano_filme = input("Digite o ano em que o filme foi lançado: ")
      string_filme = ano_filme + ' – ' + nome_filme
      img_poster = sopa_filmes.find('img', attrs={
        "data-image-title": string_filme
      })
      if img_poster is None:
        print("\nVerifique se digitou corretamente!\n")
        break
    img_link = img_poster["src"]
    response = requests.get(img_link)
    img_content = response.content
    with open("%s.jpeg" %(nome_filme), "wb") as arq:
      arq.write(img_content)
    print("\nImagem salva com sucesso!\n")

  elif opcao == 12:
      entrar_conta()

  elif opcao == 13:
    cadastrar_conta()
    
  elif opcao == 14:
    continuar = False

  elif opcao:
    print("Número inválido. Digite um dos números listados!")

    