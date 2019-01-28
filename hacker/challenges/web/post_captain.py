from requests import post
from hacker.settings import USERNAME, PASSWORD

url = 'http://www.hacker.org/challenge/chal.php?answer=marmelade&id=27&go=Submit'

response = post(url, params={'name': USERNAME, 'password': PASSWORD})

print(response.text)
