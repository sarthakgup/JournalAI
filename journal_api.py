#run with python -m uvicorn journal_api:app --reload (to launch)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SnippetRequest(BaseModel):
    snippets: List[str]

@app.post("/summarize")
async def summarize_day(request: SnippetRequest):
    snippets = request.snippets

    if not snippets:
        return {"summary": "No snippets provided."}

    prompt = f"""These are some quick notes from my day:
{chr(10).join(f"- {s}" for s in snippets)}

Please write a short, warm, reflective journal entry about this day.
"""

    try:
        process = subprocess.Popen(
            ["ollama", "run", "llama3"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"
        )
        output, _ = process.communicate(input=prompt)
        summary = output.strip()
    except Exception as e:
        return {"error": str(e)}

    return {"summary": summary}
