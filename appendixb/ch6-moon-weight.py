weight = 30
for year in range(1, 16):
    weight = weight + 0.25
    moon_weight = weight * 0.165
    print('Year %s is %s' % (year, moon_weight))