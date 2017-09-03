FROM tiangolo/uwsgi-nginx-flask:python2.7

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./app /app
COPY ./analytics.csv .

# Minify
RUN wget --post-data="input=`cat static/styles/custom.css`" --output-document=static/styles/custom.min.css https://cssminifier.com/raw; htmlmin static/index_verbose.html > static/index.html
