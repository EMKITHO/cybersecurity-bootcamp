import hashlib
text = "cyber security"
print(hashlib.md5(text.encode()).hexdigest())

