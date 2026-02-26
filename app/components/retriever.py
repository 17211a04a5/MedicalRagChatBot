from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)
from app.components.llm import get_llm_model
from app.components.vectorStore import load_vector_store

from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{input}

Answer:
"""

def set_custom_prompt():
    return ChatPromptTemplate.from_template(CUSTOM_PROMPT_TEMPLATE)


def create_retriever():
    try:
        logger.info("Creating retriever for question answering")
        vector_store = load_vector_store()
        if not vector_store:
            raise CustomException("Failed to load vector store for retriever creation.")
        
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        llm = get_llm_model()
        
        if llm is None:
            raise CustomException("Failed to initialize LLM model for retriever creation.")
        
        question_answer_chain = create_stuff_documents_chain(llm, set_custom_prompt())
        chain = create_retrieval_chain(retriever, question_answer_chain)

        logger.info("Successfully created retriever")
        return chain  # was incorrectly returning retriever
    except Exception as e:
        error_detail = CustomException(f"Error creating retriever", e)
        logger.error(str(error_detail))
        return None

# from langchain.chains import RetrievalQA
# from langchain_core.prompts import PromptTemplate

# from app.components.llm import get_llm_model
# from app.components.vectorStore import load_vector_store

# from app.config.config import HUGGINGFACE_REPO_ID,HF_TOKEN
# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException


# logger = get_logger(__name__)

# CUSTOM_PROMPT_TEMPLATE = """ Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

# Context:
# {context}

# Question:
# {question}

# Answer:
# """

# def set_custom_prompt():
#     return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE,input_variables=["context" , "question"])

# def create_qa_chain():
#     try:
#         logger.info("Loading vector store for context")
#         db = load_vector_store()

#         if db is None:
#             raise CustomException("Vector store not present or empty")

#         llm = get_llm_model()

#         if llm is None:
#             raise CustomException("LLM not loaded")

#         qa_chain = RetrievalQA.from_chain_type(
#             llm=llm,
#             chain_type="stuff",
#             retriever=db.as_retriever(search_kwargs={'k': 1}),
#             return_source_documents=False,
#             chain_type_kwargs={'prompt': set_custom_prompt()}
#         )

#         logger.info("Successfully created the QA chain")
#         return qa_chain

#     except Exception as e:
#         error_message = CustomException("Failed to make a QA chain", e)
#         logger.error(str(error_message))
#         # 🚨 Explicitly return None on failure
#         return None
