import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters  import RecursiveCharacterTextSplitter

from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP
from app.common.logger import get_logger    
from app.common.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def load_pdfs_from_directory(directory_path):
    try:
        logger.info(f"Loading PDFs from directory: {directory_path}")
        if not os.path.exists(directory_path):
            raise CustomException(f"Directory {directory_path} does not exist.", sys)
        loader = DirectoryLoader(directory_path, glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
        documents = loader.load()
        if not documents:
            logger.warning(f"No PDF documents found in directory: {directory_path}")

        logger.info(f"Successfully loaded {len(documents)} documents from {directory_path}")
        return documents
    except Exception as e:
        logger.error(f"Error loading PDFs from directory: {e}")
        raise CustomException(f"Error loading PDFs from directory: {e}", sys)
    

def create_text_chunks(documents, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    try:
        
        if not documents:
            logger.warning("No documents provided for text chunking.")
            return []
        logger.info(f"Creating text chunks with chunk size: {chunk_size} and chunk overlap: {chunk_overlap}")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        all_chunks = []
        for doc in documents:
            chunks = text_splitter.split_text(doc.page_content)
            all_chunks.extend(chunks)
        logger.info(f"Successfully created {len(all_chunks)} text chunks")
        return all_chunks
    except Exception as e:
        error_detail = CustomException(f"Error creating text chunks",e)
        logger.error(str(error_detail))
        return []