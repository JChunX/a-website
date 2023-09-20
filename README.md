# a-website

My very own website.
It could be yours too, if you want.

## Features🔥

**Markdown pages** 
Not a webdev? No problem. Skip the bells and whistles and render raw markdown files as webpages. It even looks cleaner!

**Blog posts**
Ever wanted to become a *blogger* 🤓🤓?? Now you can!

**Chatbot**
Too busy to respond to recruiters? Let a GPT chatbot do it for you using personalized responses!

## Run locally 🏃‍♂️

```bash
pip install -r requirements.txt
gunicorn -b 127.0.0.1:5000 app:app
```

## Deploy 🚀

```bash
heroku login
git push heroku main
heroku open
```