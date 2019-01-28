from datetime import datetime
from requests import get
from time import sleep

url = 'http://www.hacker.org/challenge/misc/minuteman.php'

response = get(url)

# TODO let run until answer received
while True:
    if response.text == '<html><body>\nback later':
        print('No')
    else:
        print(f'Response received at {datetime.now()}')
        print(response.text)
        break
    sleep(30)  # We poll twice a minute to make sure we don't miss the correct minute
