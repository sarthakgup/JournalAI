import subprocess

def summarize_with_ollama(snippets):
    if not snippets:
        return "No snippets for today."

    prompt = f"""Here are some quick notes from my day:
{chr(10).join(f"- {s}" for s in snippets)}

Please write a short reflective journal entry for the day. Keep it concise but warm and thoughtful.
"""

    process = subprocess.Popen(
        ["ollama", "run", "llama3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    out, err = process.communicate(input=prompt)
    return out.strip()
