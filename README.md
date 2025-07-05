# GitHub Webhook Listener 🚀

A Flask app that listens to GitHub Webhooks for push and pull request events and stores them in MongoDB Atlas.

## 🔧 Technologies Used
- Python 3.10
- Flask
- MongoDB Atlas
- GitHub Webhooks
- Ngrok

## 📦 How It Works
1. GitHub Webhook sends events to `/webhook`
2. Events are stored in MongoDB
3. `/events` route displays JSON data
4. Frontend fetches and shows events live

## 📌 Important Notes
      - This project demonstrates a Flask-based webhook listener for GitHub events.

      - It uses MongoDB Atlas to store push and pull request data in real time.

      - Ngrok is used to expose the local Flask server to the internet for GitHub webhook testing.

      - GitHub sends events to the /webhook route, which are processed and stored with timestamps.

      - Frontend (index.html + script.js) fetches events via /events and displays them live.

      - Tested with Python 3.10, Flask, and PyMongo.

      - MongoDB URI and credentials are securely managed using a .env file.

## 📦 Deployment Checklist
       1. Flask app connects to MongoDB Atlas

       2.Webhook receives push and pull_request events

       3.Events are stored and fetched successfully

       4.Ngrok exposes the server publicly

       5.UI shows latest GitHub activity

## 📺 Demo
Watch the video: [Demo Walkthrough](https://drive.google.com/drive/folders/1GMvQAh-TPPHMRVadPHzWWz2Y_2dcRZjY?usp=sharing)

## 🌐 Live Testing
Run:
```bash
py -3.10 app.py
./ngrok.exe http 5000
