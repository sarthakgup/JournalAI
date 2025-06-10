import json
import subprocess
from datetime import date

def load_snippets():
    today = str(date.today())
    with open("snippets.json", "r") as f:
        data = json.load(f)
    return data.get(today, [])

def summarize_with_ollama(snippets):
    if not snippets:
        return "No snippets for today."

    prompt = f"""These are some quick notes from my day:
{chr(10).join(f"- {s}" for s in snippets)}

Please write a short, warm, reflective journal entry about this day.
"""

    process = subprocess.Popen(
        ["ollama", "run", "llama3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"  # ✅ Fix for UnicodeDecodeError and special character issues
    )

    output, _ = process.communicate(input=prompt)
    return output.strip()

def main():
    snippets = load_snippets()
    summary = summarize_with_ollama(snippets)
    print("\n📝 Journal Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
