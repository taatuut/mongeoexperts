def gridder():
# function gridder creates grid point data in geojson format
    pointid = 1
    lonmin, lonmax, latmin, latmax = -180, 180, -90, 90
    orglatmin = latmin
    stepsize = 10
    while lonmin < lonmax:
        gj = {
          "type": "Feature",
          "geometry": {
              "type": "Point",
              "coordinates": [float(lonmin), float(latmin)]
          },
          "properties": {
              "name": "Point" + str(pointid)
          }
        }
        yield(gj)
        latmin += stepsize
        pointid += 1
        if latmin == latmax:
            latmin = orglatmin
            lonmin += stepsize

# print the output in a json array
i = 0
print("[")
for g in gridder():
    if i > 0:
      print(",")
    print(str(g))
    i += 1
print("]")
