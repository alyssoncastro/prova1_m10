# Prova 1 - módulo 10

###### autor: alysson c.c. cordeiro - engenharia da computação


## API de Pedidos

Esta é uma API para gerenciar pedidos, desenvolvida em Python utilizando Flask. A API permite criar, listar, editar e excluir pedidos.

## Estrutura do Projeto

- `app.py`: Contém a lógica principal da API.
- `models.py`: Define o modelo de dados para os pedidos.
- `requirements.txt`: Lista as dependências do projeto.
- `README.md`: Documentação do projeto.

## Estrutura de pasta

```bash
pedido_api/
├── app.py
├── models.py
├── requirements.txt
└── README.md
```


## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/alyssoncastro/prova1_m10.git

   cd prova1_m10
   ```
2. Crie e Ative um Ambiente Virtual

   ```python
   python -m venv ambiente
   cd ambiente\Scripts\activate
   ```
3. Instale as Dependências

   ```python
   pip install -r requirements.txt
   ```
4. Execute a Aplicação:
   ```python
   python app.py
   ```
A aplicação estará disponível em http://127.0.0.1:5000.

## Testar a API

1. Abra o thunder client e crie uma Nova Coleção

Adicione as seguintes requisições à sua coleção:

- POST /novo

URL: http://127.0.0.1:5000/novo

Método: POST

Body: (JSON)

```python
{
  "nome": "Nome do usuário",
  "email": "email@dominio.com",
  "descricao": "Descrição do pedido"
}
```

![Texto Alternativo](/img/post_novo.png)


-  GET /pedidos

Método: GET

URL: http://127.0.0.1:5000/pedidos

![Texto Alternativo](/img/img2_get_pedidos.png)




- GET /pedidos/1 (Substitua `1` pelo ID retornado na resposta do `POST/novo`)

Método: GET

URL: http://127.0.0.1:5000/pedidos/1

![Texto Alternativo](/img/img_3_get_pedidos_id_1_.png)


- PUT /pedidos/1 (Substitua `1` pelo ID retornado na resposta do `POST/novo`)

URL: http://127.0.0.1:5000/pedidos/1

Método: PUT

Body (JSON)

```python
{
  "nome": "Nome atualizado",
  "email": "email@dominio.com",
  "descricao": "Descrição atualizada"
}
```
![Texto Alternativo](/img/img_4_put_pedidos.png)


- DELETE /pedidos/1 (Substitua `1` pelo ID retornado na resposta do `POST/novo`)

URL: http://127.0.0.1:5000/pedidos/1

Método: DELETE

![Texto Alternativo](/img/delete.png)

OBS: No delete erro indica que o pedido com o ID 1 o qual não foi encontrado na memória. Acho que o pedido foi deletado anteriormente ou se não foi criado corretamente. Tentei varias vezes mas não obtive sucesso

OBS: NÃO DEU TEMPO DE SER DOCKERIZADA. INFELIZMENTE!


## Arquivo .gitignore

O arquivo `.gitignore` foi configurado para ignorar:

- Ambientes virtuais (venv/)
- Arquivos compilados do Python (*.pyc, *.pyo, __pycache__/)
- Configurações de IDEs (.idea/, .vscode/)
- Arquivos de logs (*.log)
- Dependências locais (env/)

   