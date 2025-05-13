import random
import string

print (''.join(random.choices(string.ascii_letters+string.digits,k=8)))