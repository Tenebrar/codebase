from hacker.ciphers import rot
from hacker.decoder import decode

value = 'Guvf zrffntr vf rapelcgrq va ebg 13. Lbhe nafjre vf svfupnxr.'

result = decode(value, lambda x: rot(x, 13))
print(result)
