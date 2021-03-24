import decimal

def gridder():
    pos = 1
    lonmin = -180
    lonmax = 180
    latmin = -90
    latmax = 90
    stepsize = 10
    while lonmin < lonmax:
        gj = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [float(lonmin), float(latmin)]
        },
        "properties": {
            "name": "Point" + str(pos)
        }
        }
        yield(gj)
        latmin += decimal.Decimal(stepsize)
        pos += 1
        if latmin == 90:
            latmin = -90
            lonmin += decimal.Decimal(stepsize)


i = 0
print("[")
for g in gridder():
    if i > 0:
      print(",")
    print(str(g).replace("'","\""))
    i += 1
print("]")
