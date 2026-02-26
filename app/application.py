from app.components.retriever import create_retriever
from dotenv import load_dotenv
from app.common.logger import get_logger
from flask import Flask, request, jsonify, session, render_template, redirect, url_for
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

app = Flask(__name__)
logger = get_logger(__name__)

app.secret_key = os.urandom(24)

from markupsafe import Markup

def nl2br(value):
    return Markup(value.replace("\n", "<br>"))

app.jinja_env.filters['nl2br'] = nl2br

@app.route('/', methods=['POST', 'GET'])
def index():
    if "messages" not in session:
        session["messages"] = []

    if request.method == 'POST':
        user_input = request.form.get('prompt')
        if user_input:
            session["messages"].append({"role": "user", "content": user_input})
            qa_chain = create_retriever()
            if qa_chain is None:
                logger.error("QA chain creation failed, cannot process user input.")
                return jsonify({"error": "Internal server error"}), 500
            try:
                answer = qa_chain.invoke({'input': user_input})
                logger.info(f"Retrieved context docs: {answer.get('context', [])}")
                result = answer.get('answer', 'No answer generated')
                session["messages"].append({"role": "assistant", "content": result})
                session.modified = True  # add this line
            except Exception as e:
                error_msg = f"Error processing user input through QA chain: {e}"
                logger.error(error_msg)
                return render_template('index.html', messages=session["messages"], error=error_msg)
        return redirect(url_for('index'))
    return render_template('index.html', messages=session.get("messages", []))


@app.route('/clear')
def clear_messages():
    session.pop("messages", None)
    return redirect(url_for('index'))