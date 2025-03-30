from src.llm import model as llm


from langchain.prompts.chat import ChatPromptTemplate

# Definir a chave da API do Google

# Função para criar uma cadeia de prompts
def create_prompt_chain(context, q):
    # Definir o template de prompt
    rag_template = "{question}\n{documents}"
    
    # Criar um template de prompt
    prompt_template = ChatPromptTemplate.from_template(rag_template)
    
    # Criar a sequência de execução
    chain =  prompt_template | llm
    
    # Retornar a cadeia de prompts
    return chain

# Exemplo de uso
question = "Qual é a capital da França?"
documents = "Paris é a capital da França."
prompt_chain = create_prompt_chain(question, documents)

# Executar a cadeia de prompts
response = prompt_chain.invoke(input={"question": "Qual é a capital da França?",
    "documents": "Paris é a capital da França."})
print("Resposta gerada:", response)