# Generative AI Chatbot

O **Generative AI Chatbot** é uma aplicação de chatbot interativa desenvolvida com Streamlit e LangChain. Ele utiliza modelos de linguagem generativa para responder perguntas com base em documentos carregados de fontes web e PDFs.

## Funcionalidades

- **Interface de Chat**: Interaja com o chatbot diretamente na interface web.
- **Carregamento de Conhecimento**:
  - Carrega documentos de sites e PDFs para criar uma base de conhecimento.
- **Processamento de Entrada**: Pré-processa as entradas do usuário para melhorar a precisão das respostas.
- **Recuperação de Documentos**: Utiliza FAISS para indexar e recuperar documentos relevantes.
- **Modelo de Linguagem Generativa**: Integração com o Google Generative AI para gerar respostas.

## Estrutura do Projeto

src/ 

├── app.py # Interface principal do chatbot 

├── config.py # Configurações do projeto (chaves de API, caminhos) 

├── embeddings.py # Configuração de embeddings 

├── knowledge_base.py # Carregamento de conhecimento (PDFs e web) 

├── llm.py # Configuração do modelo de linguagem 

├── pdf_loader.py # Carregamento de documentos PDF 

├── pre_process_input.py # Pré-processamento de entradas do usuário 

├── process_input_and_generate_ai_response.py # Lógica principal de processamento 

├── prompt_chain.py # Cadeia de prompts para o modelo 

├── vectordb.py # Configuração do banco de vetores (FAISS) 

├── web_loader.py # Carregamento de documentos da web


## Requisitos

Certifique-se de ter o Python 3.10 ou superior instalado. As dependências do projeto estão listadas no arquivo `requirements.txt`.

### Instalação

1.Clone o repositório.

2.Crie um ambiente virtual e ative-o.

3.Instale as dependências.

pip install -r requirements.txt

4.Configure as variáveis de ambiente no arquivo .env.

GOOGLE_API_KEY=<SUA_CHAVE_API_GOOGLE>

KNOWLEDGE_WEB_URL_PATH=<URLS_SEPARADAS_POR_VIRGULA>

KNOWLEDGE_PDF_PATH=<CAMINHOS_DOS_PDFS_SEPARADOS_POR_VIRGULA>

### Execução

Para iniciar o chatbot, execute o seguinte comando:

streamlit run src/app.py


Acesse o chatbot no navegador em http://localhost:8501.

### Como Funciona

Carregamento de Conhecimento:

Os documentos são carregados de URLs e PDFs configurados no .env.
Os documentos são divididos em pedaços menores para facilitar a recuperação.
Processamento de Entrada:

A entrada do usuário é pré-processada para normalização.
Um pipeline de recuperação e geração é executado para gerar a resposta.

Desta forma é utilizado o modelo RAG para enviar informações a llm para que a mesma possa gerar resposta com base nas informações

Modelo de Linguagem:

O modelo gemini-2.0-flash da Google Generative AI é utilizado para gerar respostas.
