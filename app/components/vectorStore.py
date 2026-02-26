from langchain_community.vectorstores import FAISS
from app.components.embedding import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import sys
from app.config.config import DB_FIASS_PATH
import os

logger = get_logger(__name__)

def create_vector_store(text_chunks):
    try:
        if not text_chunks:
            logger.warning("No text chunks provided for vector store creation.")
            return None
        logger.info(f"Creating vector store for {len(text_chunks)} text chunks")
        embedding_model = get_embedding_model()
        if not embedding_model:
            raise CustomException("Failed to initialize embedding model.")
        vector_store = FAISS.from_texts(text_chunks, embedding_model)
        logger.info("Successfully created vector store")
        return vector_store
    except Exception as e:
        error_detail = CustomException(f"Error creating vector store",e)
        logger.error(str(error_detail))
        return None
    
def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        logger.info(f"Loading vector store from path: {DB_FIASS_PATH}")
        if not DB_FIASS_PATH or not os.path.exists(DB_FIASS_PATH):
            logger.warning(f"Vector store file does not exist at path: {DB_FIASS_PATH}")
            return None
        vector_store = FAISS.load_local(DB_FIASS_PATH, embedding_model,allow_dangerous_deserialization=True)
        logger.info("Successfully loaded vector store")
        return vector_store
    except Exception as e:
        error_detail = CustomException(f"Error loading vector store",e)
        logger.error(str(error_detail))
        return None
    

def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            logger.warning("No text chunks provided for saving vector store.")
            raise CustomException("No text chunks provided for saving vector store.", sys)
        vector_store = create_vector_store(text_chunks)
        if not vector_store:
            raise CustomException("Failed to create vector store for saving.")
        vector_store.save_local(DB_FIASS_PATH)
        logger.info(f"Successfully saved vector store to path: {DB_FIASS_PATH}")
    except Exception as e:
        print(f"Error saving vector store: {e}")
        error_detail = CustomException(f"Error saving vector store",e)
        logger.error(str(error_detail))
