from datetime import datetime
import json
import os
import hmac
import hashlib
import requests

# Get current timestamp in ISO 8601 format with milliseconds and 'Z' suffix
timestamp = datetime.now().isoformat(timespec="milliseconds") + 'Z'

# Get action run URL from environment variable
ACTION_RUN_URL = os.getenv("ACTION_RUN_URL")
if ACTION_RUN_URL:
    ACTION_RUN_URL = ACTION_RUN_URL.strip()

# Create JSON payload
body = {
    "timestamp": timestamp,
    "name": "Tom Digby",
    "email": "m20tgd@hotmail.co.uk",
    "resume_link": "https://www.linkedin.com/in/tom-digby-71a819184/",
    "repository_link": "https://github.com/m20tgd/b12-technical-challenge",
    "action_run_link": ACTION_RUN_URL,
}
payload = json.dumps(body, sort_keys=True,
                     separators=(",", ":")).encode("utf-8")

# Get hex of payload and add to headers
SIGNING_SECRET = os.getenv("SIGNING_SECRET")
hex_digest = hmac.new(SIGNING_SECRET.encode(),
                      payload, hashlib.sha256).hexdigest()
headers = {
    "Content-Type": "application/json",
    " X-Signature-256": f"sha256={hex_digest}",
}

# Send request
response = requests.post(
    "https://b12.io/apply/submission", headers=headers, data=payload)
print(f"Response status code: {response.status_code}")
print(f"Response body: {response.text}")
