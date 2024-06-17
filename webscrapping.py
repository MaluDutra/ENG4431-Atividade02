from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

def entrar_conta():
  service = Service(ChromeDriverManager().install())

  browser = webdriver.Chrome(service=service)
  browser.get("https://studioghibli.com.br/ghiblistore/minha-conta/")
  sleep(5) 

  input_usuario = input("Digite o seu nome de usuário ou e-mail: ")
  usuario = browser.find_element(by=By.ID, value='username')
  usuario.send_keys('%s'%input_usuario)
  sleep(2)

  input_senha = input("Digite sua senha: ")
  senha = browser.find_element(by=By.ID, value='password')
  senha.send_keys('%s'%input_senha)
  sleep(2)

  input_senha = input("Deseja que o site lembre de seu log-in (s/n)? ")
  if input_senha.upper() == "S":
      botao_lembrar = browser.find_element(by=By.ID, value='rememberme')
      botao_lembrar.click()
  sleep(2)

  botao_login = browser.find_element(by=By.NAME, value='login')
  botao_login.click()
  sleep(5)
  
  return

def cadastrar_conta():
  service = Service(ChromeDriverManager().install())

  browser = webdriver.Chrome(service=service)
  browser.get("https://studioghibli.com.br/ghiblistore/minha-conta/")
  sleep(5) 

  input_email = input("Digite o seu e-mail: ")
  email = browser.find_element(by=By.ID, value='reg_email')
  email.send_keys('%s'%input_email)
  sleep(2)

  input_nova_senha = input("Digite uma senha: ")
  nova_senha = browser.find_element(by=By.ID, value='reg_password')
  nova_senha.send_keys('%s'%input_nova_senha)
  sleep(2)

  botao_cadastrar = browser.find_element(by=By.NAME, value='register')
  botao_cadastrar.click()
  sleep(5)
  
  return
