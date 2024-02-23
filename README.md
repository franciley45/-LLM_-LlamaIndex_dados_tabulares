# Llama Index Query Engine

## Descrição

Este projeto implementa uma aplicação web Flask que serve como uma interface para consultar e analisar um dataframe pandas chamado `df`. O dataframe é carregado a partir de um arquivo CSV, e a aplicação fornece aos usuários a capacidade de interativamente realizar consultas aos dados usando linguagem natural.

## Recursos

- **Consulta Interativa:** Os usuários podem inserir consultas em linguagem natural relacionadas aos dados, e o sistema utiliza o modelo OpenAI GPT-3 para interpretar e gerar respostas.

- **Manipulação de DataFrame Pandas:** O projeto utiliza a biblioteca Pandas para lidar e manipular o dataframe, tornando fácil a realização de consultas e extração de informações.

- **Interface Web:** A aplicação web Flask fornece uma interface amigável para enviar consultas e visualizar respostas formatadas.

## Dependências

- Flask
- Pandas
- OpenAI GPT-3

## Uso

1. Instale as dependências necessárias usando o seguinte comando:

    ```bash
    pip install flask pandas openai
    ```

2. Configure sua chave de API OpenAI atribuindo-a à variável de ambiente `OPENAI_API_KEY`:

    ```python
    os.environ["OPENAI_API_KEY"] = "sua_chave_api_aqui"
    ```

3. Execute a aplicação Flask:

    ```bash
    python nome_do_seu_app.py
    ```

4. Acesse a aplicação em seu navegador web em [http://localhost:5000](http://localhost:5000).

## Como Realizar Consultas

1. Insira sua consulta no campo de entrada fornecido na página inicial.
2. Clique no botão de envio para enviar sua consulta ao sistema.
3. Veja a resposta formatada na mesma página.

## Exemplo de Consulta

- "Me dê as informações que você pode obter na data '09-01-2023'?"

## Estrutura do Projeto

- `nome_do_seu_app.py`: Arquivo principal da aplicação contendo rotas e configuração do Flask.
- `llama_index/prompts.py`: Módulo que define um modelo para prompts usados nas consultas ao GPT-3.
- `llama_index/query_engine.py`: Módulo contendo a classe PandasQueryEngine para lidar com consultas ao dataframe.
- `data/df_100 1.csv`: Arquivo CSV de exemplo contendo o dataframe.

## Observação

Certifique-se de substituir `sua_chave_api_aqui` pela sua chave real da API OpenAI GPT-3.

Sinta-se à vontade para personalizar a aplicação, adicionar mais prompts e aprimorar as capacidades de consulta de acordo com o seu caso de uso específico. Boas consultas!
