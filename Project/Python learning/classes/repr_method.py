class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):  #usage of __repr__ allows to convert str back to class obj.
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"

if __name__ == "__main__":
    r = Robot('Maks', 1993)

    r_str = str(r)
    print(r_str)
    print("Type of r_str: ", type(r_str))
    new = eval(r_str)
    print(new)
    print("Type of new: ", type(new))