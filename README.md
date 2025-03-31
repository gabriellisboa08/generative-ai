<h1>Generative AI Chatbot</h1>

<p>O <strong>Generative AI Chatbot</strong> é uma aplicação de chatbot interativa desenvolvida com Streamlit e LangChain. Ele utiliza modelos de linguagem generativa para responder perguntas com base em documentos carregados de fontes web e PDFs.</p>

<h2>Funcionalidades</h2>

<ul>
  <li><strong>Interface de Chat</strong>: Interaja com o chatbot diretamente na interface web.</li>
  <li><strong>Carregamento de Conhecimento</strong>:
    <ul>
      <li>Carrega documentos de sites e PDFs para criar uma base de conhecimento.</li>
    </ul>
  </li>
  <li><strong>Processamento de Entrada</strong>: Pré-processa as entradas do usuário para melhorar a precisão das respostas.</li>
  <li><strong>Recuperação de Documentos</strong>: Utiliza FAISS para indexar e recuperar documentos relevantes.</li>
  <li><strong>Modelo de Linguagem Generativa</strong>: Integração com o Google Generative AI para gerar respostas.</li>
</ul>

<h2>Estrutura do Projeto</h2>

<pre><code>src/

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
</code></pre>

<h2>Requisitos</h2>

<p>Certifique-se de ter o Python 3.10 ou superior instalado. As dependências do projeto estão listadas no arquivo <code>requirements.txt</code>.</p>

<h3>Instalação</h3>

<ol>
  <li>Clone o repositório.</li>
  <li>Crie um ambiente virtual e ative-o.</li>
  <li>Instale as dependências.</li>
</ol>

<pre><code>pip install -r requirements.txt</code></pre>

<ol start="4">
  <li>Configure as variáveis de ambiente no arquivo .env.</li>
</ol>

<pre><code>GOOGLE_API_KEY=&lt;SUA_CHAVE_API_GOOGLE&gt;

KNOWLEDGE_WEB_URL_PATH=&lt;URLS_SEPARADAS_POR_VIRGULA&gt;

KNOWLEDGE_PDF_PATH=&lt;CAMINHOS_DOS_PDFS_SEPARADOS_POR_VIRGULA&gt;</code></pre>

<h3>Execução</h3>

<p>Para iniciar o chatbot, execute o seguinte comando:</p>

<pre><code>streamlit run src/app.py</code></pre>

<p>Acesse o chatbot no navegador em <a href="http://localhost:8501">http://localhost:8501</a>.</p>

<h3>Como Funciona</h3>

<h4>Carregamento de Conhecimento:</h4>

<ul>
  <li>Os documentos são carregados de URLs e PDFs configurados no .env.</li>
  <li>Os documentos são divididos em pedaços menores para facilitar a recuperação.</li>
</ul>

<h4>Processamento de Entrada:</h4>

<ul>
  <li>A entrada do usuário é pré-processada para normalização.</li>
  <li>Um pipeline de recuperação e geração é executado para gerar a resposta.</li>
</ul>

<p>Desta forma é utilizado o modelo RAG para enviar informações a llm para que a mesma possa gerar resposta com base nas informações</p>

<h4>Modelo de Linguagem:</h4>

<p>O modelo gemini-2.0-flash da Google Generative AI é utilizado para gerar respostas.</p>
