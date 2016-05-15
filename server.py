from flask import Flask, redirect, url_for, session, request, jsonify, render_template, send_from_directory

app = Flask(__name__, static_url_path='', template_folder='static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')