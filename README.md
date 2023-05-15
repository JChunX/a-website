# a-website

Just a website. nothing to see here.

## Run locally

```bash
pip install -r requirements.txt
gunicorn -b 127.0.0.1:5000 app:app
```

## Deploy

```bash
git push heroku master
heroku open
```