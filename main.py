from flask import Flask, request, jsonify
import hmac
import json
import hashlib
import base64

app = Flask(__name__)
secret_key = None

# read the secret key from file
with open("util/secret_key.txt", "rb") as f:    
    secret_key = b""
    byte = f.read(1)
    while byte != b"":
        secret_key += byte
        byte = f.read(1)

@app.route('/generate-token', methods=["POST"])
def generateToken():
    try:
        req = request.get_json()
        # turn json object to string
        data = json.dumps(req)
    except:
        return "Invalid JSON", 400
    
    try:
        # base64 encode string
        datab64 = base64.b64encode(data.encode('utf-8'))
        # generate hmac token
        h = hmac.new(secret_key, datab64, hashlib.sha256)
        res = req
        res["signature"] = h.hexdigest()
        return res, 200
    except:
        return "something went wrong generating hmac token", 400

if __name__ == '__main__':
    # verify that secret key is initialized
    if secret_key != None and secret_key != "":
        app.run(debug=False, host='0.0.0.0', port=8081)
