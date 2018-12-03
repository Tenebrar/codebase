value = '5499fa991ee7d8da5df0b78b1cb0c18c10f09fc54bb7fdae7fcb95ace494fbae8f5d90a3c766fdd7b7399eccbf4af592f35c9dc2272be2a45e788697520febd8468c808c2e550ac92b4d28b74c16678933df0bec67a967780ffa0ce344cd2a9a2dc208dc35c26a9d658b0fd70d00648246c90cf828d72a794ea94be51bbc6995478505d37b1a6b8daf7408dbef7d7f9f76471cc6ef1076b46c911aa7e75a7ed389630c8df32b7fcb697c1e89091c30be736a4cbfe27339bb9a2a52a280'  # noqa

"""
This sequence has been encrypted with a cipher that works as follows:

k = {unknown 4-byte value}
x = {unknown 4-byte value}
for (i = 0; i < len(txt); i += 4)
  c = (txt[i] -> txt[i + 3]) ^ k
  print c
  k = (c + x) % 0x100000000
"""
