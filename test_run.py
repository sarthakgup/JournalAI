#Add Fake Entries for Testing

import json
from datetime import date

today = str(date.today())

sample_snippets = [
    "Had a walk in the park this morning.",
    "Worked on the journaling AI project.",
    "Made pasta and listened to music at night."
]

with open("snippets.json", "r") as f:
    data = json.load(f)

data[today] = sample_snippets

with open("snippets.json", "w") as f:
    json.dump(data, f, indent=2)

print("Snippets for today saved.")
