from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "ryu": "hello",
    "k": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

languages = [{'name' : 'java'}, {'name' : 'php'}, {'name' : 'ruby'}]

@app.route("/", methods = ['GET'])
@auth.login_required
def test():
    return jsonify({'message': "Hello, %s!" % auth.username()})
    
@app.route("/lang", methods = ['GET'])
@auth.login_required
def returnAll():
    return jsonify({"language": languages})

@app.route("/lang/<string:name>", methods = ['GET'])
@auth.login_required
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({"languages": langs[0]})
    
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)