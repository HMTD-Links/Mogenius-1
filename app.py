import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Links: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@github.com/HMTD-Links/UK-Auto-Filter-Bot $REPO ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
