from requests import get
from hacker.settings import USERNAME, PASSWORD

url = 'http://www.hacker.org/challenge/chal.php?answer=spaghetti&id=25&go=Submit'

response = get(url, params={'name': USERNAME, 'password': PASSWORD})

print(response.text)
