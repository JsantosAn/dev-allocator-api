# Instruções de Instalação e Execução Local

Este guia contém as instruções detalhadas para instalar e executar a aplicação localmente em sua máquina. Siga os passos abaixo para garantir que a aplicação funcione corretamente.

## Instalação
Antes de começar, é necessário ter as seguintes ferramentas instaladas em sua máquina:

* Git: Para clonar o repositório da aplicação.

* Python: Certifique-se de ter o Python 3.x instalado. Você pode verificar com o comando:

```bash
python --version
```

* Pip: O gerenciador de pacotes Python. Pode ser instalado junto com o Python.

* Banco de Dados: PostgreSQL.

* Editor de Código: Como o Visual Studio Code, PyCharm, ou qualquer editor de sua preferência.



## Clonando o Repositório
1. Abra o terminal e navegue até o diretório onde deseja clonar o projeto.

2. Clone o repositório com o comando:
```bash
git clone <URL_DO_REPOSITORIO>
```

## Instalando Dependências
1. Navegue até o diretório do projeto:
```bash
    cd nome-do-repositorio
```


2. Crie um ambiente virtual para o projeto:
* Para Windows:
 ```bash
    python -m venv venv
 ```
* Para Mac/Linux:

 ```bash
    python3 -m venv venv
 ```

3. Ative o ambiente virtual:
* Para Windows:
 ```bash
    .\venv\Scripts\activate
 ```
* Para Mac/Linux:
 ```bash
   source venv/bin/activate
 ```

4. Instale as dependências do projeto:

 ```bash
   pip install -r requirements.txt
 ```


## Configurações Adicionais

1. Crie um arquivo  ```.env``` (se não houver) na raiz do projeto e adicione as variáveis de ambiente necessárias. Um exemplo de arquivo ```.env```
 ```bash
DB_DRIVER=django.db.backends.postgresql
PG_DB= DB_NAME
PG_USER= postgres
PG_PASSWORD= postgres
PG_HOST=localhost
PG_PORT=5432
 ```
2. Execute as migrações:
 ```bash
  python manage.py migrate
 ```
### Criando um Superusuário
1. Após realizar a migração, execute o seguinte comando para criar um superusuário:

 ```bash
   python manage.py createsuperuser
 ```
2. O comando pedirá para você fornecer informações como nome de usuário, email e senha. Preencha os campos conforme desejado.

## Executando a Aplicação
1. Para rodar a aplicação localmente, basta executar o seguinte comando no terminal:
 ```bash
  python manage.py runserver
 ```
