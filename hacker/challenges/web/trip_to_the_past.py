from requests import get

from hacker.settings import USERNAME, PASSWORD

url = 'http://www.hacker.org/challenge/misc/past.php'

# IDEA try passing a very old browser in the headers

user_agent = 'NCSA_Mosaic/2.0'
response = get(url, params={'name': USERNAME, 'password': PASSWORD}, headers={'User-Agent': user_agent})

print(response.text)  # <h3>Hello Mosaic user</h3><p>Welcome to the past. Your answer is: Remember Eric Bina
