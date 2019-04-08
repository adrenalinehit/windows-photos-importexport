import hashlib
from base64 import b64decode, b64encode

hashermd5 = hashlib.md5()

with open('c:\\users\\nick\\Pictures\\jaguarxf91.jpg', 'rb') as afile:
    buf = afile.read()
    hashermd5.update(buf)
print(hashermd5.hexdigest())
print(b64encode(hashermd5.digest()).decode('utf-8'))


#PeJKCvpHyN+hdiX4duQffQ==   <-- "pixel" hash from photos db
#vBZYU0drGYSxf7BgPGVSpQ==   <-- md5 hashbfrom python lib.