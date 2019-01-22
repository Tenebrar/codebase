from urllib.parse import urlencode

from requests import get

from hacker.settings import USERNAME, PASSWORD

answer = urlencode({'answer': 'http://whitehouse.gov'})
url = f'http://www.hacker.org/challenge/chal.php?{answer}&id=38&go=Submit'

response = get(url, params={'name': USERNAME, 'password': PASSWORD}, headers={'referer': 'http://whitehouse.gov'})

print(response.text)
