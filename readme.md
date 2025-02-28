Aqui está o README combinado com as informações que você forneceu, de forma organizada e clara:

---

# README para Automação de Testes e Configuração do Projeto

Este repositório contém uma suíte de testes automatizados usando Selenium e pytest para realizar testes de login, cadastro e recuperação de senha em uma aplicação Django local. A aplicação também é fornecida como parte do projeto para rodar localmente e realizar os testes de QA.

## 🚀 Configuração do Ambiente para o Projeto Django

Siga os passos abaixo para rodar o projeto Django localmente.

### 📌 Clonar o Repositório

Primeiro, clone o repositório do projeto:

```bash
git clone git@github.com:danellaclaudioluiz/autenticator.git
cd autenticator
```

### 🐍 Criar e Ativar Ambiente Virtual

Crie e ative o ambiente virtual para o projeto:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

### 📦 Instalar Dependências

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 🔄 Aplicar Migrações

Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```

### 🚀 Rodar o Servidor

Inicie o servidor Django para rodar a aplicação localmente:

```bash
python manage.py runserver
```

Agora a aplicação estará rodando em `http://127.0.0.1:8000/` 🎉

---

## 🚀 Configuração do Ambiente para Automação de Testes

### 1. Instalar o Python

A automação foi desenvolvida usando Python 3.x. Verifique se o Python está instalado com:

```bash
python --version
```

Caso o Python não esteja instalado, baixe e instale a versão mais recente de [python.org](https://www.python.org/).

### 2. Instalar Dependências do Teste

Instale as dependências do projeto de automação com:

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não esteja presente, instale as bibliotecas manualmente:

```bash
pip install selenium pytest
```

### 3. Instalar o WebDriver do Chrome

A automação foi configurada para usar o ChromeDriver. Baixe a versão compatível do [ChromeDriver](https://sites.google.com/chromium.org/driver/) e coloque-o em um diretório acessível. Adicione o diretório ao PATH do sistema para que o Selenium possa utilizá-lo.

### 4. Configuração do Ambiente

Verifique se o servidor Django está rodando em `http://127.0.0.1:8000/`. Caso o endereço da aplicação seja diferente, altere o código conforme necessário:

```python
driver.get("http://127.0.0.1:8000/")
```

### 5. Diretório de Screenshots

Os testes vão gerar capturas de tela (screenshots) que serão armazenadas no diretório `screenshots`. O diretório será criado automaticamente, mas o script precisa de permissão para criar novas pastas.

### 6. Execução dos Testes

Para rodar os testes automatizados, utilize o comando:

```bash
pytest
```

Os resultados dos testes serão exibidos no terminal, e as capturas de tela serão armazenadas no diretório `screenshots`.

---

## 📋 Detalhes dos Testes Automatizados

### Testes Implementados:

- **CT001 - Login com credenciais válidas**
- **CT002 - Login com senha inválida**
- **CT003 - Cadastro com credenciais válidas**
- **CT005 - Cadastro com confirmação de senha inválida**
- **CT006 - Recuperação de senha**

Cada um desses testes será executado e, em caso de falha ou sucesso, será gerada uma captura de tela. Abaixo estão os principais comandos utilizados durante os testes:

- `wait_for_element(driver, xpath)`: Função auxiliar para aguardar elementos na página.
- `tirar_screenshot(driver, nome_arquivo)`: Função para capturar screenshots dos resultados dos testes.

### Observações:

- Certifique-se de que a aplicação esteja rodando corretamente no servidor local antes de rodar os testes.
- Caso utilize um navegador diferente do Chrome, altere o WebDriver no código para o driver correspondente.

---

Esse README cobre tanto a configuração do ambiente para rodar a aplicação Django quanto os passos necessários para configurar e executar os testes automatizados. Caso precise de mais alguma coisa ou tenha dúvidas, estarei por aqui!