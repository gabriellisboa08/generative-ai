from knowledge_base import knowledge
from langchain_community.vectorstores import FAISS
from embeddings import embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter



def knowledge_to_retriever():
    # Configurar o splitter com parâmetros personalizados
    documents_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Tamanho máximo de cada pedaço
        chunk_overlap=200,  # Sobreposição entre os pedaços
        separators=["\n\n", "\n", ".", " "]  # Delimitadores para divisão
    )

    #Utilizamos esta tecnica para dividir os documentos em pedaços menores para facilitar a busca e a recuperação, 
    # bem como economia de recursos ao chamar o modleo 

    # Dividir os documentos usando o splitter configurado
    document_splitered = documents_splitter.split_documents(documents=knowledge)


    document_splitered = documents_splitter.split_documents(documents=knowledge)

    vector = FAISS.from_documents(documents=document_splitered, embedding=embeddings)
    
    return vector.as_retriever()

