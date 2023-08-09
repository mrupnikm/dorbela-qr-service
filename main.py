import os
import random
import string
import pyqrcode
from flask import Flask
import pyzbar

app = Flask(__name__)
url= "http://localhost:5000/dorbella/"

# Generate a random string of length 80
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

random_string = generate_random_string(80)
qr_code = pyqrcode.create(url+random_string)
qr_code.png("qr_code.png", scale=6)

@app.route('/dorbella/ping')
def ping():
    return "Pong!"


@app.route('/dorbella/<string:random_string>')
def dorbella(random_string):
    # Check if the provided string matches the generated random string
    if random_string != random_string:
        return "No home configured under this name.", 400

    # Send a notification to Slack
    print("Ding Dong!")

    return "Please wait for response", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
