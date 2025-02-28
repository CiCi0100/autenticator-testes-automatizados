import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Diretório para armazenar os screenshots
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Configuração do WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    yield driver
    driver.quit()

# Função auxiliar para aguardar elementos
def wait_for_element(driver, xpath):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

# Função para tirar screenshot
def tirar_screenshot(driver, nome_arquivo):
    caminho_completo = os.path.join(SCREENSHOT_DIR, f"{nome_arquivo}.png")
    driver.save_screenshot(caminho_completo)
    print(f"Screenshot salvo: {caminho_completo}")

# CT001 - Login com credenciais válidas
def test_login_valido(driver):
    try:
        wait_for_element(driver, "//div/a[contains(.,'Login')]").click()
        wait_for_element(driver, "//div/input[@placeholder='Digite seu usuário']").send_keys("Marcos Vinicius Pedro Galvão")
        wait_for_element(driver, "//div/input[@placeholder='Digite sua senha']").send_keys("lala2408")
        wait_for_element(driver, "//button[contains(.,'Entrar')]").click()
        
        assert wait_for_element(driver, "//div/p[contains(.,'Você está logado no sistema.')]").is_displayed()
        tirar_screenshot(driver, "login_sucesso")
    
    except Exception as e:
        tirar_screenshot(driver, "login_falha")
        raise e  # Relança a exceção para que o pytest registre o erro corretamente

# CT002 - Login com senha inválida
def test_login_senha_invalida(driver):
    try:
        wait_for_element(driver, "//div/a[contains(.,'Login')]").click()
        wait_for_element(driver, "//div/input[@placeholder='Digite seu usuário']").send_keys("Marcos Vinicius Pedro Galvão")
        wait_for_element(driver, "//div/input[@placeholder='Digite sua senha']").send_keys("lal819373")
        wait_for_element(driver, "//button[contains(.,'Entrar')]").click()
        
        assert wait_for_element(driver, "//div/div/div/div[contains(.,'Credenciais inválidas')]").is_displayed()
        tirar_screenshot(driver, "login_senha_invalida")
    
    except Exception as e:
        tirar_screenshot(driver, "login_senha_invalida_falha")
        raise e

# CT003 - Cadastro com credenciais válidas
def test_cadastro_valido(driver):
    try:
        wait_for_element(driver, "//div/a[contains(.,'Registrar')]").click()
        wait_for_element(driver, "//form/div/input[@name='username']").send_keys("username123")
        wait_for_element(driver, "//form/div/input[@name='email']").send_keys("useremail123@maildrop.cc")
        wait_for_element(driver, "//form/div/input[@name='password1']").send_keys("password123")
        wait_for_element(driver, "//form/div/input[@name='password2']").send_keys("password123")
        wait_for_element(driver, "//form/button[contains(.,'Registrar')]").click()
        
        assert wait_for_element(driver, "//div/div/div/div[contains(.,'Cadastro realizado com sucesso! Faça login.')]").is_displayed()
        tirar_screenshot(driver, "cadastro_sucesso")
    
    except Exception as e:
        tirar_screenshot(driver, "cadastro_falha")
        raise e

# CT005 - Cadastro com confirmação de senha inválida
def test_cadastro_confirmacao_senha_invalida(driver):
    try:
        wait_for_element(driver, "//div/a[contains(.,'Registrar')]").click()
        wait_for_element(driver, "//form/div/input[@name='username']").send_keys("usuario_teste")
        wait_for_element(driver, "//form/div/input[@name='email']").send_keys("usuario@maildrop.cc")
        wait_for_element(driver, "//form/div/input[@name='password1']").send_keys("12345")
        wait_for_element(driver, "//form/div/input[@name='password2']").send_keys("1236789")
        wait_for_element(driver, "//form/button[contains(.,'Registrar')]").click()
        
        assert wait_for_element(driver, "//div/div/div/div[contains(.,'As senhas não coincidem')]").is_displayed()
        tirar_screenshot(driver, "cadastro_senha_invalida")
    
    except Exception as e:
        tirar_screenshot(driver, "cadastro_senha_invalida_falha")
        raise e

# CT006 - Recuperação de senha
def test_recuperacao_senha(driver):
    try:
        wait_for_element(driver, "//div/a[contains(.,'Login')]").click()
        wait_for_element(driver, "//div/a[contains(.,'Esqueceu sua senha?')]").click()
        wait_for_element(driver, "//div/input[@placeholder='Digite seu e-mail cadastrado']").send_keys("usuario@maildrop.cc")
        wait_for_element(driver, "//button[contains(.,'Enviar link de recuperação')]").click()
        
        assert wait_for_element(driver, "//div/div/div/div[contains(.,'Link enviado com sucesso')]").is_displayed()
        tirar_screenshot(driver, "recuperacao_sucesso")
    
    except Exception as e:
        tirar_screenshot(driver, "recuperacao_falha")
        raise e

