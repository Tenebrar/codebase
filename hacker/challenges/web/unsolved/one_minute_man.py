from datetime import datetime
from requests import get
from time import sleep

url = 'http://www.hacker.org/challenge/misc/minuteman.php'

while True:
    response = get(url)

    if response.text == '<html><body>\nback later':
        print(f'No received at {datetime.now()}')
    else:
        print(f'Response received at {datetime.now()}')
        print(response.text)
        break
    sleep(30)  # We poll twice a minute to make sure we don't miss the correct minute


# Response received at 2019-07-27 05:52:15.744809
# <html><body>
# i declare the answer is gugglemuggle
