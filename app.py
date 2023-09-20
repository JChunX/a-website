import os
from pathlib import Path

import markdown
from flask import Flask, Response, render_template, request

from src.llm.gpt import JasonGPT


# Function to read Markdown file
def read_markdown_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

app = Flask(__name__)
gpt = JasonGPT()

def generate_response(query):
    for response in gpt.process_query_logic(query):
        yield markdown.markdown(response)

# Route for the home page
@app.route('/')
def home():
    content = read_markdown_file('main.md')
    html = markdown.markdown(content)
    gpt.reset()
    return render_template('index.html', content=html)

# Route for processing the query
@app.route('/query', methods=['POST'])
def process_query():
    query = request.form['query']
    # Process the query and yield the result in text
    return Response(generate_response(query), mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(host="0.0.0.0", port=port, debug=True)
