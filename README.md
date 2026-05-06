# AI Voice Receptionist

An AI-powered voice receptionist system designed for salon and service appointment bookings.  
The application enables users to interact using voice commands, receive AI-generated responses, and automatically schedule appointments through Google Calendar integration.

---

## Features

- Voice-based interaction using browser SpeechRecognition APIs
- AI-generated conversational responses using local Ollama LLM
- Appointment booking intent detection
- Automatic date and time extraction from conversations
- Google Calendar integration for scheduling events
- Real-time voice response using speech synthesis
- FastAPI backend with modular architecture
- Optional Next.js frontend support

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Web Speech API
- Next.js (optional frontend)

### Backend
- FastAPI
- Python
- Ollama LLM
- Google Calendar API
- Uvicorn

---

# Project Structure

```bash
AI-Voice-Receptionist/
│
├── back/
│   ├── main.py
│   ├── agent.py
│   ├── ollama_client.py
│   ├── tools.py
│   ├── database.py
│   ├── business_info.txt
│   ├── credentials.json
│   └── token.json
│
├── front/
│   └── index.html
│
├── next-app/
│
└── README.md
```

---

# Architecture Overview

## Backend (`back/`)

### `main.py`
FastAPI server exposing the `/chat` API endpoint.

### `agent.py`
Handles:
- Conversation flow
- Intent detection
- Booking extraction
- AI response generation

### `ollama_client.py`
Communicates with the local Ollama API for LLM-based responses.

### `tools.py`
Contains Google Calendar integration utilities.

### `database.py`
Temporary in-memory appointment storage.

### `business_info.txt`
Business-specific details used for AI prompting.

---

## Frontend (`front/`)

### `index.html`
Voice-enabled browser interface that:
- Captures user speech
- Sends text to backend APIs
- Speaks AI-generated responses

---

## Next.js Frontend (`next-app/`)

An optional modern frontend scaffold built with Next.js.

---

# Requirements

## Software

- Python 3.11+
- Node.js
- Ollama installed locally

## Python Dependencies

Install required packages:

```bash
pip install fastapi uvicorn pydantic requests google-auth-oauthlib google-api-python-client
```

---

# Ollama Setup

1. Install Ollama from the official website.
2. Pull a supported model:

```bash
ollama pull qwen2.5:3b
```

3. Ensure Ollama is running locally:

```bash
ollama serve
```

Default API endpoint:

```bash
http://localhost:11434
```

---

# Backend Setup

## 1. Navigate to Backend

```bash
cd back
```

## 2. Start FastAPI Server

```bash
uvicorn main:app --reload --port 8000
```

Backend API will run at:

```bash
http://127.0.0.1:8000/chat
```

---

# Google Calendar Integration Setup

## 1. Create Google Cloud Project

- Enable Google Calendar API
- Create OAuth 2.0 credentials

## 2. Download Credentials

Download:

```bash
credentials.json
```

Place it inside:

```bash
back/
```

## 3. Authorize Access

On the first booking request:
- Browser authorization window opens
- Access token gets stored as `token.json`

---

# Running Frontend

## Plain HTML Frontend

1. Open:

```bash
front/index.html
```

2. Allow microphone permissions
3. Click:

```bash
Start Conversation
```

---

## Next.js Frontend

### Install Dependencies

```bash
cd next-app
npm install
```

### Start Development Server

```bash
npm run dev
```

---

# Example Workflow

1. User speaks:
   > "Book an appointment tomorrow at 5 PM"

2. Speech is converted to text

3. Backend:
- Detects booking intent
- Extracts date and time
- Generates AI response

4. Appointment is created in Google Calendar

5. AI confirms the booking using voice output

---

# Future Improvements

- Database integration (MongoDB/PostgreSQL)
- Multi-user authentication
- WhatsApp integration
- SMS/Email confirmations
- Admin dashboard
- Multi-language support
- Deployment support

---

# Notes

- Current appointment storage is temporary (in-memory).
- Browser SpeechRecognition works best on Chrome/Edge.
- Google OAuth credentials are required for Calendar functionality.

---

# Author

Developed as an AI-powered voice automation project using FastAPI, Ollama, and browser speech technologies.
