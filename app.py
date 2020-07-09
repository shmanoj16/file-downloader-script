from flask import Flask, jsonify,request,send_file
import sys
import json
app = Flask(__name__)
import os

@app.route('/', methods=['GET','POST'])
def main():
    return 'Success'
    
@app.route('/download')
def download():
    location = r"C:\Users\Manoj Srimurugan\Documents\iris.csv" # File Name / Path 
    print(location)
    return send_file(location, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4545,debug=True)