from flask import Flask, request
from number_parser import parse, parse_number

app = Flask(__name__)

@app.route("/number", methods=["POST"])
def parseNumber():
    data = request.form['data']
    ret = str(parse(data))
    ret = ret.replace(" ","")
    return ret

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
