import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Render ke environment variables se URI uthayega
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.iSkipPro

@app.route('/check_device', methods=['POST'])
def check_device():
    data = request.json
    serial = data.get('serial', '').strip().upper()
    
    device = db.registered_devices.find_one({"serial": serial})
    
    if device:
        return jsonify({
            "status": "registered", 
            "message": "A12+ With Signal Supported"
        })
    else:
        return jsonify({
            "status": "not_registered", 
            "message": "Serial not registered. Contact Admin or Reseller."
        })

if __name__ == "__main__":
    app.run()
