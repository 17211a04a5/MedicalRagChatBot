import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Configuration class to hold all configuration variables

HF_TOKEN = os.getenv("HF_TOKEN")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")  


DB_FIASS_PATH = "Vectorstore/fiassDB"
DATA_PATH = r'data/'
CHUNK_SIZE = 500
CHUNK_OVERLAP =  50
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
HUGGINGFACE_REPO_ID = "google/flan-t5-base"
#HUGGINGFACE_REPO_ID="mistralai/Mistral-7B-Instruct-v0.3"