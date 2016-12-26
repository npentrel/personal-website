# personal-website

1. virtualenv venv
2. source flask/bin/activate
3. pip install flask
4. Run server `python server.py`

# server side
`alias websiteupdate='(killall gunicorn; git pull; htmlminify static/index_verbose.html > static/index.html; gunicorn server:app -b 146.185.137.172:80 --access-logfile access.txt &)'`
