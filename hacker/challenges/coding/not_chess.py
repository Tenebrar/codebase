from base64 import b64decode
from urllib.parse import unquote

input = 'cXVlZW4lMjdzJTIwZ2FtYml0'  # Found in source of page

print(unquote(b64decode(input).decode('utf-8')))
