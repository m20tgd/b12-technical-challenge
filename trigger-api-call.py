import json
import os


print("Hello, World!")

ACTION_RUN_URL = os.getenv("ACTION_RUN_URL").strip()
TEST = os.getenv("TEST")
print(TEST == "This is a test")

body = {
    "name": "Tom Digby",
    "email": "m20tgd@hotmail.co.uk",
    "resume_link": "https://www.linkedin.com/in/tom-digby-71a819184/",
    "repository_link": "https://github.com/m20tgd/b12-technical-challenge",
    "action_run_link": ACTION_RUN_URL,
}

payload = json.dumps(body, sort_keys=True,
                     separators=(",", ":")).encode("utf-8")

print(payload)
