# personal-website

1. virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. Run server `python main.py`

# server side
`alias websitelocalupdate='docker stop website_local; docker rm website_local; docker rmi website_app_local; sudo docker build -t website_app_local .; docker run --name website_local -p 5000:80 -t website_app_local'`

`alias websiteupdate='git pull; docker stop website; docker rm website; docker rmi website_app; sudo docker build -t website_app .; docker run -d --restart=always --name website -p 80:80 -t website_app'`

`alias minify='python3 css-minify.py app/static/styles/custom.css; htmlmin app/static/index_verbose.html app/static/index.html'`

Old:
`alias websiteupdate='(killall gunicorn; git pull; wget --post-data="input=`cat static/styles/custom.css`" --output-document=static/styles/custom.min.css https://cssminifier.com/raw;  htmlminify static/index_verbose.html > static/index.html; gunicorn server:app -b 146.185.137.172:80 --access-logfile access.txt &)'`
