
# Projeto Backend de Gerenciamento Bancário

Este projeto é um sistema backend desenvolvido em **Python** que implementa funcionalidades como cadastro de usuário, autenticação, edição de saldo e gerenciamento seguro de dados usando JWT. O código é estruturado em módulos seguindo boas práticas de separação de responsabilidades.
É parte do curso de **Autenticação JWT e Segurança** da Rocketseat.

## Estrutura de Diretórios

```plaintext
src/
├── configs/        # Configurações do projeto (ex: JWT)
├── controllers/    # Lógica de negócio (ex: cadastro, login, saldo)
├── drivers/        # Manipuladores auxiliares (JWT, senha, etc)
├── main/           # Inicialização do app, rotas principais
├── models/         # Modelos e acesso ao banco de dados
├── tests/          # Testes unitários e de integração
├── views/          # Interfaces HTTP das funcionalidades
├── storage.db      # Banco de dados SQLite local
└── __init__.py
```

## Funcionalidades

- **Cadastro de Usuários**: Registro, autenticação e gerenciamento com JWT.
- **Login**: Validação de credenciais de forma segura.
- **Edição de Saldo**: Alteração de saldo bancário de usuários.
- **Testes Automatizados**: Com Pytest e Coverage.
- **Arquitetura Limpa**: Padrão MVC com separation of concerns.

## Instalação e Execução

> **Pré-requisitos**: Python 3.13+ e [uv](https://github.com/astral-sh/uv) instalado.

1. **Instale as dependências:**
    ```bash
    uv install
    ```

2. **Execute o servidor:**
    ```bash
    python run.py
    ```
 

3. **As rotas principais estão em `src/main/routes/`. O servidor é iniciado via `src/main/server/server.py`.

## Dependências do Projeto

As dependências são gerenciadas pelo [uv](https://github.com/astral-sh/uv) e estão declaradas em `pyproject.toml`:

- `bcrypt>=4.3.0`
- `flask>=3.1.1`
- `pyjwt>=2.10.1`
- `pytest>=8.4.1`
- `pytest-cov>=6.2.1`
- `python-dotenv>=1.1.1`
- `ruff>=0.12.8`



## Testes

Todos os testes ficam em `src/tests/`.

Para executar:
```bash
pytest
```

Para relatório de cobertura:
```bash
coverage run -m pytest
coverage report
```


## Observações

- O projeto utiliza um banco SQLite embutido (`storage.db`), sendo facilmente adaptável para outros SGBDs.
- JWT é utilizado para autenticação e autorização segura de usuários.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests!

---

