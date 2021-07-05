import hashlib
text = "cyber security"
#MD5
print(hashlib.md5(text.encode()).hexdigest())
#SHA1
print(hashlib.sha1(text.encode()).hexdigest())
#SHA224
print(hashlib.sha224(text.encode()).hexdigest())