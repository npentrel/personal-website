from flask import Flask, redirect, url_for, session, request, jsonify, abort, Response, send_file, render_template, send_from_directory, abort
import requests
import json
import sys
import pytz
from datetime import datetime
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__, static_url_path='', template_folder='static')
app.wsgi_app = ProxyFix(app.wsgi_app)

def track(source):
  ip = request.remote_addr
  tor = requests.get('http://istorexitnode.setgetgo.com/get.php?ip={ip}'.format(ip=ip))
  if tor.status_code == 200:
    if True in tor.json().values(): abort(403)

  location = requests.get('http://ip-api.com/json/{ip}'.format(ip=ip)).json()
  city = location['city'] if 'city' in location else 'None'
  country = location['country'] if 'country' in location else 'None'
  ip = location['query'] if 'query' in location else ip

  user_agent = request.user_agent
  os = user_agent.platform
  browser = user_agent.browser

  cet = datetime.now(pytz.timezone('Europe/London'))
  time = cet.strftime("%d.%m.%Y %H:%M:%S")
  data = [time, city, country, ip, os, browser, source]
  data = map(str, data)
  data = ';'.join(data)
  with open('analytics.csv', 'a+') as f: f.write(data + '\n')


@app.route('/<source>.png')
def pixel(source):
  track(source)
  return send_file('assets/profile.png')


@app.route('/a/<source>', methods=['POST'])
def link(source):
  track('a/' + source)
  return ('', 204)


@app.route('/analyt1cs')
def analytics():
  return render_table()


@app.route('/analyt1cs/<source>')
def filtered_analytics(source):
  return render_table(source)


def render_table(source=None):
  columns = ['Time', 'City', 'Country', 'IP', 'OS', 'Browser', 'From']
  csv = open('analytics.csv', 'r+').read()
  rows = csv.splitlines()
  rows = [row.split(';') for row in rows]
  if source: rows = filter(lambda x: x[-1] == source, rows)
  rows = reversed(rows[-50:])

  return render_template('table.html', columns=columns, data=rows)


@app.errorhandler(500)
def server_error(error):
  return json.dumps({'error': 'Server Error'}), 500


@app.errorhandler(400)
def bad_request(error):
  return json.dumps({'error': 'Bad Request'}), 400


@app.errorhandler(404)
def not_found(error):
  return json.dumps({'error': 'Not Found'}), 404

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
