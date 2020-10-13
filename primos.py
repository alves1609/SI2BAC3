import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    limite = 100

    c = 1
    p = 1
    n = 3

    primos = "2,"

    while p < limite:
        saoprimo = 1
        for i in range(2, n):
            if n % i == 0:
                saoprimo = 0
                break
        if (saoprimo):
            primos = primos + str(n) + ","
            p += 1
            if(p % 10 == 0):
                primos = primos + "<br>"
        n+=1

    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)