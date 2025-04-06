import logging
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.runnables.base import Runnable
from langchain_core.runnables import RunnableLambda
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from src.database.KnowledgeRetriever import KnowledgeRetriever
from src.ai_integration.LLMManager import LLMManager
from src.data_processing.InputPreProcessor import InputPreProcessor

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


class AIResponseProcessor:
    def __init__(self):
        """
        Classe responsável por processar a entrada do usuário e gerar respostas usando um modelo de linguagem.
        """
        self.pre_process_question_runnable = RunnableLambda(lambda input: InputPreProcessor(input).process())
        self.rag_template = ChatPromptTemplate.from_template(template="""
        Responda a pergunta com base no contexto
        {context}
        Pergunta: {input}""")
        self.document_chain = create_stuff_documents_chain( LLMManager().get_llm(), self.rag_template)

    def create_retrieval_chain(self) -> Runnable:
        """
        Cria a cadeia de recuperação de documentos.
        """
        return self.pre_process_question_runnable | create_retrieval_chain(
            KnowledgeRetriever().create_retriever(), self.document_chain
        )

    def process_input_and_generate_response(self, user_input: str) -> str:
        """
        Processa a entrada do usuário e gera uma resposta.

        :param user_input: Entrada do usuário.
        :return: Resposta gerada pelo modelo de linguagem.
        """
        retrieval_chain = self.create_retrieval_chain()
        response = {}

        try:
            response = retrieval_chain.invoke(user_input)
        except ChatGoogleGenerativeAIError as e:
            logger.error("Erro ao gerar resposta com o modelo de linguagem: ", e)
            response["answer"] = "Houve um problema ao acessar a IA."

        return response["answer"]