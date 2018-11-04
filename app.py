import config as cfg
import os
import yaml
from functools import wraps
from flask import Flask, request, jsonify, abort, session, send_from_directory, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = cfg.app_secret_key


#===================================================================
# auth
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'account' not in session:
            return redirect(url_for('login', next=request.url))
        return func(*args, **kwargs)
    return decorated_function


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'account' in session:
            return redirect(url_for('index'))
        return send_from_directory('public', 'login.html')
    else:
        try:
            account = request.json['account']
            passwd = request.json['passwd'].lower()
        except:
            abort(400)

        if (account not in cfg.app_users) or (passwd != cfg.app_users[account]):
            return 'unknown account or passwd', 401

        session['account'] = account

        return 'ok'
        

#===================================================================
# index
@app.route('/static/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory('static', path)

@app.route('/')
@app.route('/index')
@login_required
def index():
    return send_from_directory('public', 'index.html')


#===================================================================
# main
@app.route('/list', methods=['POST'])
@login_required
def list():
    if os.path.exists('case.yml'):
        return jsonify(yaml.load(open('case.yml', 'r', encoding='utf-8')))
    else:
        return jsonify({
            '動漫花園': [],
            'nyaa': [],
            'nyaa2': [],
        })


@app.route('/update', methods=['POST'])
@login_required
def update():
    data = {}

    for website, cases in request.json.items():
        data[website] = []
        for case in cases:
            if case['name'] != '' and case['keys'] != '':
                data[website].append({
                    'name': case['name'],
                    'keys': case['keys'],
                })

    yaml.dump(data, open('case.yml', 'w', encoding='utf-8'), allow_unicode=True)
    return 'ok'


if __name__ == '__main__':
    app.run(host=cfg.app_host, port=cfg.app_port, debug=cfg.app_debug)

