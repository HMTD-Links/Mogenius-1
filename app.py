import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Links: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@github.com/HMTD-Links/UK-Auto-Filter-Bot $REPO ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
