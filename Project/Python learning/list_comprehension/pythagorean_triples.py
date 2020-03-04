def pithagorean_triple(input_range):
    result = [ (x, y, z) for x in range(1, input_range) for y in range(x, input_range) for z in range(y, input_range) if x**2 + y**2 == z**2 ]
    return print(result)
pithagorean_triple(30)