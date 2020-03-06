class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," +  str(self.build_year) +  ")"

    def __str__(self):
        return "Name: " + self.name + ", Build year: " + str(self.build_year)

if __name__ == "__main__":
    r = Robot('George', 1890)

    r_repr = repr(r)
    print(r_repr)
    print("Type of r: ", type(r_repr))
    new = eval(r_repr)  #przyjazne printowanie - czyli wykonywanie naszej funkcji '__str__'
    print(new)
    print("Type of new: ", type(new))