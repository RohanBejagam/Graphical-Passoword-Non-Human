import hashlib

password = input()

h = hashlib.new('sha512_256')
h.update(password.encode())
password = h.hexdigest()

print(password)