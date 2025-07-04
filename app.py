from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

print("🔥 Flask server starting...")

load_dotenv()

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["github_events"]
collection = db["events"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event = request.headers.get('X-GitHub-Event')
    timestamp = datetime.utcnow()

    if event == "push":
        author = data['pusher']['name']
        branch = data['ref'].split("/")[-1]
        message = f'{author} pushed to {branch} on {timestamp.strftime("%d %B %Y - %I:%M %p UTC")}'
    elif event == "pull_request":
        author = data['pull_request']['user']['login']
        from_branch = data['pull_request']['head']['ref']
        to_branch = data['pull_request']['base']['ref']
        message = f'{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp.strftime("%d %B %Y - %I:%M %p UTC")}'
    else:
        return '', 204

    collection.insert_one({"message": message, "timestamp": timestamp})
    return jsonify({"status": "success"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    docs = collection.find().sort("timestamp", -1).limit(10)
    return jsonify([{"message": doc["message"]} for doc in docs])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
