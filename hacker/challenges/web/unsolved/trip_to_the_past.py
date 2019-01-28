from requests import get
from hacker.settings import USERNAME, PASSWORD

url = 'http://www.hacker.org/challenge/misc/past.php'

response = get(url, params={'name': USERNAME, 'password': PASSWORD})

print(response.text)
