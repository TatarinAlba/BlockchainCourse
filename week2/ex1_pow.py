#!/usr/bin/env python
# example of proof of work algorithm

import hashlib
import time
import json

from flask import Flask, request
import requests

max_nonce = 2 ** 32 # 4 billion

def proof_of_work(header, difficulty_bits):
    target = 2 ** (256 - difficulty_bits)
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256((str(header)+str(nonce)).encode()).hexdigest()
        if int(hash_result, 16) < target:
            print(f"Success with nonce {nonce}")
            print(f"Hash is {hash_result}")
            return (hash_result, nonce)
    print(f"Failed after {nonce} (max_nonce) tries")
    return None, nonce

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_index():
    return "<h1>Go to /pow_calculate directory with the query string including difficulty_bit parameter. Good luck!</h1>"

@app.route("/pow_calculate", methods=["GET"])
def give_proof_of_work():
    hash_result = ''
    new_block = 'test block with transactions' + hash_result
    difficulty_bit = request.args.get("difficulty_bit")
    if difficulty_bit is not None and difficulty_bit.isdigit():
        hash_result, nonce = proof_of_work(new_block, int(difficulty_bit))
    else:
        return json.dumps({"message": "400", "description": "You provided invalid difficulty_bit parameter"})
    if hash_result is None:
        return json.dumps({"message": "400", "description": f"Failed after {nonce} (max_nonce) tries"})
    return json.dumps({"hash_result": hash_result, "nonce": nonce})

app.run(debug=True, port=5000)