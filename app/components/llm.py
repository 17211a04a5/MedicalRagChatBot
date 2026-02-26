# from langchain_huggingface import HuggingFaceEndpoint
# from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN
# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException

# logger = get_logger(__name__)
# HUGGINGFACE_REPO_ID = "google/flan-t5-base"
# def get_llm_model(huggingface_repo_id=HUGGINGFACE_REPO_ID, hf_token=HF_TOKEN):
#     try:
#         logger.info(f"Initializing HuggingFace LLM model: {huggingface_repo_id}")
#         llm = HuggingFaceEndpoint(
#             repo_id=huggingface_repo_id,
#             huggingfacehub_api_token=hf_token,
#             task="text2text-generation",
#             temperature=0.3,
#             max_new_tokens=512,
#         )
#         logger.info("Successfully initialized HuggingFace LLM model")
#         return llm
#     except Exception as e:
#         error_detail = CustomException(f"Error initializing HuggingFace LLM model", e)
#         logger.error(str(error_detail))
#         return None
    

#     azure_openai_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT", "https://xplatform-openai-shared.openai.azure.com/")
#     azure_openai_deployment: str = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-2024-11-20")
#     azure_openai_api_key: str = os.getenv("AZURE_OPENAI_KEY", "")
#     azure_openai_api_version: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21")

from langchain_openai import AzureChatOpenAI
from app.config.config import HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os

logger = get_logger(__name__)

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "https://xplatform-openai-shared.openai.azure.com/")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-2024-11-20")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_KEY", "")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21")

def get_llm_model():
    try:
        logger.info(f"Initializing Azure OpenAI LLM model: {AZURE_OPENAI_DEPLOYMENT}")
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            azure_deployment=AZURE_OPENAI_DEPLOYMENT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        logger.info("Successfully initialized Azure OpenAI LLM model")
        return llm
    except Exception as e:
        error_detail = CustomException(f"Error initializing Azure OpenAI LLM model", e)
        logger.error(str(error_detail))
        return None