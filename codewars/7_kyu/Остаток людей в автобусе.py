def number(bus_stops):
    c = 0
    for i in range(len(bus_stops)):
        c = c + bus_stops[i][0] - bus_stops[i][1]
    return c
print(number([[1,0],[3,1],[7,3]]))

#def number(bus_stops):
#    return sum([stop[0] - stop[1] for stop in bus_stops])