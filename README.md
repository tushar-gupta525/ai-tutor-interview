# AI Tutor Interview – Voice Based AI Interview System

An AI-powered voice interview platform that simulates a real tutoring interview.
The system asks questions using AI, listens to spoken answers, and evaluates the candidate automatically.

This project demonstrates AI + Speech Recognition + Full-Stack Deployment using modern web technologies.

### 🚀 Live Demo
#### Frontend

https://ai-tutor-interview.vercel.app

#### Backend API

https://ai-tutor-interview.onrender.com

### ✨ Features
AI interviewer that dynamically asks questions
Voice-based interaction using browser speech recognition
AI speech synthesis for interviewer voice
10-second thinking timer before answering
Real-time conversational UI
Automatic answer evaluation
Score visualization with progress bars
Fully deployed full-stack system

### 🧠 Tech Stack

Frontend

HTML

CSS

Vanilla JavaScript

Web Speech API (SpeechRecognition + SpeechSynthesis)

Backend

Python

FastAPI

Uvicorn

AI Model

Groq LLM API

Deployment

Vercel (Frontend)

Render (Backend)


### 🏗 System Architecture

User Browser

     │
     │ Voice Input
     ▼

Speech Recognition (Web Speech API)
  
     │
     ▼
Frontend (Vercel)
     
     │
     │ HTTP Request
     ▼
FastAPI Backend (Render)
     
     │
     │ Prompt + User Answer
     ▼
Groq LLM
   
     │
     ▼
AI Question / Evaluation
     
     │
     ▼

Frontend UI + Voice Output


### 📁 Project Structure

ai-tutor-interview

│

├── frontend

│   └── index.html
│

├── backend

│   ├── app

│   │   └── main.py

│   ├── requirements.txt
│

└── README.md

### ⚙️ How It Works

User clicks Start Interview

AI asks the first question

User gets 10 seconds to think

Microphone activates automatically

User speaks their answer

Answer is sent to backend

AI generates the next question

After several questions, AI generates evaluation scores

### 📊 Evaluation Metrics

The AI evaluates answers based on:

Clarity
Warmth
Patience
Simplicity
Fluency
Recommendation

### 📝 Example Evaluation

Clarity:        6 / 10

Warmth:         4 / 10

Patience:       7 / 10

Simplicity:     5 / 10

Fluency:        6 / 10

Recommendation: Proceed to next round


### 🛠 Backend Setup

Clone Repository

git clone https://github.com/yourusername/ai-tutor-interview.git

cd ai-tutor-interview

Install Dependencies

pip install -r requirements.txt

Run Backend

uvicorn app.main:app --reload

Backend will run at:

http://127.0.0.1:8000
🔑 Environment Variables

The backend requires a Groq API key.

Create environment variable:

GROQ_API_KEY=your_api_key_here

⚠️ Never expose API keys in frontend code.

### 🌍 Deployment
Backend Deployment (Render)

Build command

pip install -r requirements.txt

Start command

uvicorn app.main:app --host 0.0.0.0 --port 10000

Add environment variable:

GROQ_API_KEY

Frontend Deployment (Vercel)

Push frontend to GitHub

Import project into Vercel

Deploy as static site

Update API URL in index.html

https://ai-tutor-interview.onrender.com


### 🌐 Browser Requirements

#### Best supported browsers:

Google Chrome

Microsoft Edge

Brave may require enabling microphone permissions manually.

### 🔮 Future Improvements

#### Possible enhancements:

Adaptive interview difficulty
Emotion detection from voice
Candidate performance dashboard
Export interview report (PDF)
Multi-role interview support (Math, Science, Coding)
