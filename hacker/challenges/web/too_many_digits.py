from requests import get

url = 'http://www.hacker.org/challenge/misc/toomany/infinite_number.txt'
# Can't use 1e52, because then the 'sexdecillion - 1' doesn't work
sexdecillion = 1000000000000000000000000000000000000000000000000000

response = get(url, headers={'Range': f'bytes={sexdecillion - 1}-{sexdecillion + 98}'})

print(response.text)
# 6307248905694960523281201519065112560315109266120946334276511258112647455670688177420019237462570351

