from flask import Flask, render_template, url_for, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello():
    if(request.method == "POST"):
        response = request.get_json()
        p = response['p']
        print(p)
        res = {}
        for i in os.listdir(p):
            res[i] = [f"{p}{i}/{x}" for x in os.listdir(f'{p}{i}')]
        return res
    else:
        return render_template('index.html')

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response



if( __name__ == "__main__"):
        app.run(debug=True);
