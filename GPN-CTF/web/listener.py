 save as listener.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Request received!")
    print("Headers:", request.headers)
    print("Args:", request.args)
    print("Data:", request.data)
    print("Cookies:", request.cookies)
    return '', 200

@app.route('/leak')
def leak():
    flag = request.args.get('flag')
    print(f"Received leak: {flag}")
    return 'OK', 200

app.run(host='0.0.0.0', port=80)
