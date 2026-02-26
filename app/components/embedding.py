from langchain_huggingface import HuggingFaceEmbeddings
from app.config.config import HUGGINGFACE_API_TOKEN, HUGGINGFACE_REPO_ID
from app.common.logger import get_logger    
from app.common.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def get_embedding_model():
    try:
        logger.info(f"Creating embeddings for text chunks using HuggingFace model: {HUGGINGFACE_REPO_ID}")
        model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        logger.info("Successfully initialized HuggingFace embeddings model")
        return model
    except Exception as e:
        error_detail = CustomException(f"Error loading embeddings",e)
        logger.error(str(error_detail))
        return None