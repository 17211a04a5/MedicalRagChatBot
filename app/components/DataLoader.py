import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
from app.components.pdfloder import load_pdfs_from_directory, create_text_chunks
from app.components.vectorStore import create_vector_store, save_vector_store, load_vector_store
from app.config.config import DATA_PATH
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def process_and_store_data():
    try:
        logger.info("Starting data processing and storage workflow")
        documents = load_pdfs_from_directory(DATA_PATH)
        if not documents:
            logger.warning("No documents loaded, skipping text chunking and vector store creation.")
            return
        
        text_chunks = create_text_chunks(documents)
        if not text_chunks:
            logger.warning("No text chunks created, skipping vector store creation.")
            return
        logger.info(f"Created {len(text_chunks)} text chunks from loaded documents")
        save_vector_store(text_chunks)
        logger.info("Data processing and storage workflow completed successfully")
    except Exception as e:
        error_detail = CustomException(f"Error in data processing and storage workflow",e)
        logger.error(str(error_detail))


if __name__ == "__main__":
    process_and_store_data()