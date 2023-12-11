import os
from pathlib import Path

import markdown
from flask import Flask, Response, render_template, request

from src.llm.gpt import JasonGPT
from src.utils import read_markdown_file
from pygments.formatters import HtmlFormatter

app = Flask(__name__)
gpt = JasonGPT()

def generate_response(query):
    for response in gpt.process_query_logic(query):
        mkd = markdown.markdown(response)
        yield mkd

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

@app.route('/blog/llm-agents')
def llm_agents_blog():
    content = read_markdown_file('blog/llm-agents-landing-page.md')
    html = markdown.markdown(content)
    return render_template('blog.html', content=html)

@app.route('/blog/llm-agents/llm-chess-1')
def llm_chess_1():
    content = read_markdown_file('blog/llm-chess-1.md')
    html = markdown.markdown(content, extensions=['fenced_code', 'codehilite'])
    return render_template('blog.html', content=html)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(host="0.0.0.0", port=port, debug=True)
