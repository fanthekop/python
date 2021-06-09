from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import mysql.connector
import testfile

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/v1/dataAll')
@cross_origin(supports_credentials=True)
def dataAll():
    print("request dateInput : "+request.args.get("dateInput"))
    return jsonify({'success': 'ok'})

@app.route('/api/v1/test')
@cross_origin(supports_credentials=True)
def test():
    print("test")
    return jsonify({'success': 'ok'})

@app.route('/api/v1/data/<dateInput>')
@cross_origin(supports_credentials=True)
def api_all(dateInput):
    print("dateInput : "+dateInput)
    testfile.my_function()
    return jsonify({'success': 'ok'})

@app.route('/test_run')
@cross_origin(supports_credentials=True)
def test_run():
    return render_template('view.html',name="hiran")

@app.route('/view_history')
@cross_origin(supports_credentials=True)
def view_history():
    return render_template('view_history.html',)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

app.run(port=8000, host='0.0.0.0')