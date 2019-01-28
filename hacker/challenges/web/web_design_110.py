from lxml.etree import HTML
from requests import get
from typing import Dict

# What would Netscape call:
value = '#6B8E23'


def color_definitions() -> Dict[str, str]:
    # Official Netscape color table
    response = get('https://www.ou.edu/research/electron/internet/bgcolors.shtml')

    html = HTML(response.text)
    rows = html.xpath('/html/body/center/table/tr')

    result = {}
    for row in rows:
        cells = row.xpath('td/font')
        if cells:
            result[f'#{cells[1].text}{cells[2].text}{cells[3].text}'] = cells[0].text

    return result


print(color_definitions()[value])  # olivedrab
