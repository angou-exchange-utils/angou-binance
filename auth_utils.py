import hmac
import hashlib


def generate_signature(secret, query, body):
    if isinstance(body, (bytes, bytearray)):
        body = body.decode('utf8')
    message = query + body
    signature = hmac.new(
        bytes(secret, 'utf8'),
        bytes(message, 'utf8'),
        digestmod=hashlib.sha256)
    return signature.hexdigest()
