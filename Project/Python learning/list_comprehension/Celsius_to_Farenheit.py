def celsius_to_farenheit(*temperatures):
    Farenheit = [ ((float(9)/5)*x + 32) for x in temperatures ]
    return print(Farenheit)

celsius_to_farenheit(36.6)