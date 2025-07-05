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

## 📺 Demo
Watch the video: [Demo Walkthrough](https://drive.google.com/drive/folders/1GMvQAh-TPPHMRVadPHzWWz2Y_2dcRZjY?usp=sharing)

## 🌐 Live Testing
Run:
```bash
py -3.10 app.py
./ngrok.exe http 5000
