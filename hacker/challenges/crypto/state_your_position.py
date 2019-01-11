from hacker.decoder import decode
from hacker.bytestreams import substrings

value = 'TNAIDDNHBWVEWIAAZECAGINCNMDNJJWIESCCNHDGAGGADTNBNCFCACOKAOKAAKECTHCAHWYGNHDDCKOKAVACWVEWIBMSCDCICAASCHLAANCLDCKNYFNDCMNCWVGMIG'  # noqa

# Source: http://www.stateabbreviations.us/
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    # Districts, territories and possessions
    'American Samoa': 'AS',
    'District of Columbia': 'DC',
    'Federated States of Micronesia': 'FM',
    'Guam': 'GU',
    'Marshall Islands': 'MH',
    'Northern Mariana Islands': 'MP',
    'Palau': 'PW',
    'Puerto Rico': 'PR',
    'Virgin Islands': 'VI',
}
states = {value: key for key, value in states.items()}


def decode_substring(s):
    """
    Decode a substring of length 3
    The first 2 characters indicate a state, the third which letter in the state name to return
    """
    return states.get(s[:2])[ord(s[2]) - ord('a')]

result = decode(substrings(value, 3), decode_substring)
print(result)
