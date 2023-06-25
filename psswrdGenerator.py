import random
import string

for_pass = string.ascii_letters + string.digits + "@!$#%&?"
size_pass = 10

password = ''.join(random.choice(for_pass) for _ in range(size_pass))

print("Password:", password)