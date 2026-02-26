# MedicalRaG

MedicalRaG is a Python application designed for medical document retrieval and question answering using advanced language models and vector stores. It leverages embeddings, PDF loading, and custom retrieval logic to provide accurate responses based on medical data.

## Project Structure

```
main.py                # Entry point for the application
pyproject.toml         # Project metadata and dependencies
requirements.txt       # Python package requirements
app/
  application.py       # Main application logic
  common/              # Common utilities (logger, exceptions)
  components/          # Core components (DataLoader, embedding, retriever, etc.)
  config/              # Configuration files
  templates/           # HTML templates for UI
data/                  # Data files
logs/                  # Log files
Vectorstore/           # Vector database files
```

## Features

- Medical document ingestion and processing
- Embedding generation for semantic search
- PDF loading and parsing
- Custom retriever and vector store integration
- Web interface for querying medical data
- Logging and error handling

## Setup Instructions

1. **Clone the repository**
	```bash
	git clone <repo-url>
	cd MedicalRaG
	```

2. **Create a virtual environment**
	```bash
	python -m venv .venv
	source .venv/bin/activate  # On Windows: .venv\Scripts\activate
	```

3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```

4. **Configure the application**
	- Edit configuration files in `app/config/` as needed.

5. **Run the application**
	```bash
	python main.py
	```

## Usage

1. Access the web interface (if available) via the provided URL.
2. Upload medical documents or query existing data.
3. Review results and logs in the `logs/` directory.

## Folder Details

- `app/common/`: Logging and custom exception handling
- `app/components/`: Data loading, embedding, PDF loader, retriever, vector store, LLM integration
- `app/config/`: Application configuration
- `app/templates/`: HTML templates for UI
- `Vectorstore/`: FAISS index and vector database

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact the project maintainer.
