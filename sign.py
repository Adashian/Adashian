import hashlib
from config import SECRET_KEY


def generate_sign(data: dict):
    keys_sorted = dict(sorted(data.items(), key=lambda item: str(item[0])))
    values = [str(value) for value in keys_sorted.values()]
    str_sign = ':'.join(values) + SECRET_KEY
    data['sign'] = hashlib.sha256(str_sign.encode('utf-8')).hexdigest()
    return data
