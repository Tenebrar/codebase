from requests import get

url = 'http://www.hacker.org/challenge/misc/one.php'

response = get(url)

# The answer is in the headers of the redirect
print(response.history[0].headers['X-hacker-answer'])  # madreup
