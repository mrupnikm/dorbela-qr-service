import os
import random
import string
import pyqrcode
from flask import Flask, send_file
import pyzbar
from pathlib import Path

app = Flask(__name__)
url= "http://localhost:5000/dorbella/"
random_string=""

# Generate a random string of length 80
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

if not (Path("qr_code.png").exists()):
    random_string = generate_random_string(80)
    text_file = open("string.txt", "w")
    n = text_file.write(random_string)
    text_file.close()
    qr_code = pyqrcode.create(url+random_string)
    qr_code.png("qr_code.png", scale=6)
    #print("Does not exist!"+ random_string)

else: 
    random_string = open("string.txt").read()
    #print("Exists!"+ random_string)

@app.route('/home')
def home():
    return send_file(Path("qr_code.png"))

@app.route('/dorbella/ping')
def ping():
    print("in ping route")
    return "Pong!"

@app.route('/dorbella/<string:x>')
def dorbella(x):
    if x != random_string:
        return "No home configured under this name.", 400

    # Send a notification to whatever channel
    print("Ding Dong!")
    return "Please wait for response", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
