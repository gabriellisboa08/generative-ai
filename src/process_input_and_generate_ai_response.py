import logging
from langchain.document_loaders import PyPDFLoader

# Configurar o logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(__name__ + ".log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

from typing import Any, Dict
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.runnables.base import Runnable
from vectordb import knowledge_to_retriever
from llm import llm
from pre_process_input import pre_process_input
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.runnables import RunnableLambda 
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError  # Import the missing exception


def process_input_and_generate_ai_response(user_input :str) :

    # Aqui estou encapsulando a função pre_process_question em um RunnableLambda para depois passar para a cadeia de processamento
    pre_process_question_runnable = RunnableLambda(lambda input: pre_process_input(input))


    rag_template: ChatPromptTemplate = ChatPromptTemplate.from_template(template="""
    Responda a pergunta com base no contexto
    {context}
    Pergunta: {input}""")


    document_chain: Runnable[Dict[str, Any], Any] =  create_stuff_documents_chain(llm,rag_template)

    retrieval_chain  =  pre_process_question_runnable | create_retrieval_chain(knowledge_to_retriever(),document_chain)

    response = {}
    try:
        response= retrieval_chain.invoke( user_input)
    except ChatGoogleGenerativeAIError as e:
        logger.error("Erro ao gerar resposta com o modelo de linguagem: ", e)
        response["answer"] = "Houve um problema ao acessar a IA."
 
    return response["answer"]

    



    
    