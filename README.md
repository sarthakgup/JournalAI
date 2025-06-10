# JournalAI
AI journaling assistant that turns daily snippets into a full entry. Implements text summarization and optional selfie uploads.



1. Backend (FastAPI + Ollama)
Language: Python
Tech Stack: FastAPI for the REST API, Ollama to run a local LLM like llama3 for summarization.
Functionality: Accepts an array of text snippets via /summarize endpoint and returns a coherent daily summary.

Run with:
python -m uvicorn journal_api:app --reload

2. Frontend (React + TailwindCSS)
Created With: create-react-app
Styling: TailwindCSS for modern utility-first styling

Functionality:
Textarea to input daily snippet
List of submitted snippets
Button to call backend API and generate a summary
Dynamically displays returned summary

Integrated via: Fetch request to http://127.0.0.1:8000/summarize

Run with:
npm start [powershell]

🗂️ File Structure Highlights
JournalAI/
├── journal_api.py (your FastAPI backend)
├── ollama_utils.py (runs Ollama with subprocess)
├── journal-frontend/ (your React frontend)
│   ├── src/
│   │   ├── App.js (UI + fetch logic)
│   │   ├── index.js
│   │   ├── index.css (@tailwind directives)
│   ├── postcss.config.js
│   ├── tailwind.config.js

🧠 What's in Front of You Now
A working local full-stack app that:
Accepts journal snippets from a UI
Sends them to a backend running a local LLM (no API key or cloud charges)
Receives and displays a generated story/summary
Clean, responsive UI with modern styling
Fully modular — ready for:
Hosting (Vercel + Render)
User auth
Persistent storage (e.g., SQLite, Supabase)
Native mobile integration (e.g., React Native or Expo)

