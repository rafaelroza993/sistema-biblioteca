# Sistema Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python, com persistência de dados em PostgreSQL. Permite cadastrar livros e usuários, controlar empréstimos e devoluções, tudo através de um menu interativo via terminal.

## Funcionalidades

- Cadastro de novos livros (título, autor, ISBN, quantidade disponível)
- Listagem de todos os livros cadastrados
- Cadastro de novos usuários
- Listagem de todos os usuários cadastrados
- Empréstimo de livros, com controle de disponibilidade
- Devolução de livros, com atualização automática de status

## Tecnologias utilizadas

- Python 3
- PostgreSQL
- [psycopg](https://www.psycopg.org/) (driver de conexão com o PostgreSQL)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (gerenciamento de variáveis de ambiente)

## Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL instalado e em execução
- pip

## Instalação

1. Clone o repositório:

```bash
   git clone https://github.com/rafaelroza993/sistema-biblioteca.git
   cd sistema-biblioteca
```

2. Crie e ative um ambiente virtual:

```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Instale as dependências:

```bash
   pip install -r requirements.txt
```

4. Crie o banco de dados no PostgreSQL (exemplo via terminal):

```bash
   createdb biblioteca
```

5. Execute o script de criação das tabelas:

```bash
   psql -d biblioteca -f database/schema.sql
```

6. Crie um arquivo `.env` na raiz do projeto com suas credenciais de banco:

```env
   DB_NAME=biblioteca
   DB_USER=postgres
   DB_PASSWORD=sua_senha
   DB_HOST=localhost
   DB_PORT=5432
```

## Como executar

```bash
python app.py
```

Ou, utilizando o script de inicialização incluído:

```bash
bash iniciar_biblioteca.sh
```

## Estrutura do banco de dados

O banco possui três tabelas principais:

- **livros**: armazena título, autor, ISBN e quantidade disponível.
- **usuarios**: armazena nome, e-mail e data de cadastro.
- **emprestimos**: registra cada empréstimo, relacionando usuário e livro, com datas e status (`Ativo`, `Devolvido` ou `Atrasado`).

O script completo de criação está em [`database/schema.sql`](database/schema.sql).

## Estrutura do projeto

```
sistema-biblioteca/
├── app.py
├── core/
│   ├── database.py
│   └── queries.py
├── database/
│   └── schema.sql
├── iniciar_biblioteca.sh
├── requirements.txt
└── README.md
```

## Autor

Desenvolvido por Rafael Roza como projeto de estudo em Python e PostgreSQL.
