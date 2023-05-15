import argparse
import os
import time
from pathlib import Path

import markdown
import openai
from flask import Flask, jsonify, render_template, request


# Function to read Markdown file
def read_markdown_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


class JasonGPT:
    
    def __init__(self):
        self.gpt_name = 'JasonGPT🤖'
        self.user_alias = 'You'
        self.knowledge_cutoff_date = '2023-05-14'
        self.system_prompt = self.create_system_prompt()
        self.query_prompt = Path('gpt/query_prompt.txt').read_text()
        self.max_tokens = 300
        self.temperature = 0.4
        self.max_history = 5
        self.reset()
        
    def reset(self):
        print("Resetting conversation history...")
        self.responses = []
        self.queries = []
        
    @staticmethod
    # Function to simplify text for gpt prompting
    def simplify_text(text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": 
                        "Please simplify the following text into concise bullet points: {}".format(text)},
                ]
            )
        
        text = response.choices[0].message.content
        return text
        
    def create_system_prompt(self):
        system_prompt_root = Path('gpt/system_prompt.txt').read_text()
        jason_basic_info = Path('gpt/jason_basic_info.txt').read_text()
        jason_portfolio = read_markdown_file('main.md') #JasonGPT.simplify_text(
        meta_data = "Jason's portfolio update date: {}, today's date: {}".format(self.knowledge_cutoff_date, time.strftime("%Y-%m-%d"))
        
        system_prompt = ' '.join([system_prompt_root, jason_basic_info, jason_portfolio, meta_data])
        return system_prompt
    
    def process_query_logic(self, query):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.create_chat_history_prompt() + [{"role": "user", "content": query + self.query_prompt}],
                max_tokens=self.max_tokens,
                temperature=self.temperature,
            )
            response_str = response.choices[0].message.content
            finish_reason = response.choices[0].finish_reason
            if finish_reason == 'length':
                response_str += "..."
            if response_str[0] == '#' or response_str[0] == '*':
                response_str = '\n' + response_str
        except Exception as e:
            print(e)
            response_str = "Sorry, I am currently unable to answer this question. Please try again later."
            
        self.add_to_chat_history(query, response_str)
    
    def add_to_chat_history(self, query, response_str):
        self.responses.append(response_str)
        self.queries.append(query)    
        if len(self.responses) > self.max_history:
            self.responses.pop(0)
            self.queries.pop(0)
        
    def create_chat_history_prompt(self):
        chat_history_prompt = []
        chat_history_prompt.append({"role": "system", "content": self.system_prompt})
        for i in range(len(self.responses)):
            chat_history_prompt.append({"role": "user", "content": self.queries[i]})
            chat_history_prompt.append({"role": "assistant", "content": self.responses[i]})
            
        return chat_history_prompt
    
    def render_conversation(self):
        conversation = ""
        for i in range(len(self.responses)):
            conversation += f"**{self.user_alias}**: {self.queries[i]}<br />"
            conversation += f"**{self.gpt_name}**: {self.responses[i]}<br /><br />\n\n"
            
        print(conversation)
        return conversation
    
    
app = Flask(__name__)
gpt = JasonGPT()

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
    # Process the query and return the result
    gpt.process_query_logic(query)
    result = gpt.render_conversation()
    result_html = markdown.markdown(result)
    return jsonify({'result': result_html})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
