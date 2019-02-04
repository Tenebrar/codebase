from hacker.bytestreams import substrings

value = '00230211913108430050286091123267001446589042407200380634902253880050113189282402'

sum_lat = 0
sum_lon = 0
for s in substrings(value, 16):
    lat = int(s[:8]) / 1e6
    lon = int(s[8:]) / 1e6
    print(lat, lon)

    sum_lat += lat
    sum_lon += lon

print()
print(sum_lat / 5, sum_lon / 5)

# http://www.copypastemap.com/
# 0.230211	-91.310843	cross5	red	1	Point1
# 0.50286	-91.123267	cross5	red	2	Point2
# 0.144658	-90.424072	cross5	red	3	Point3
# 0.380634	-90.225388	cross5	red	4	Point4
# 0.501131	-89.282402	cross5	red	5	Point5

# DMS to DD conversion (seems to have little effect)
# 0.4419444	91.75083333333333
# 1.6277778	92.1075
# 1.5272222	91.83111111111111
# 0.8094444	91.86333333333333
# 1.1475  90.13388888888889
