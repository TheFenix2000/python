class Robot:
    def __init__(self, name, build_year, lk, lp):
        self.name = name
        self.build_year = build_year
        self.__potential_phisical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_phisical + self.__potential_psychic
        if s <= -1:
            return 'I feel miserable!'
        elif s <= 0:
            return 'I feel bad!'
        elif s <= 0.5:
            return 'Could be worse!'
        elif s <= 1:
            return 'Seem to be okay!'
        else:
            return  'Great'

if __name__ == "__main__":
    x = Robot('Boris', 1990, 0.2, 0.4)
    y = Robot('Marvin', 1899, -0.4, 0.3)
    z = Robot('Vlad', 2000, 0.8, 0.8)
    z2 = Robot('Kamil', 2020, -0.9, -0.2)
    z3 = Robot('Gabriel', 2019, 0.3, 0.2)
    print(x.condition)
    print(y.condition)
    print(z.condition)
    print(z2.condition)
    print(z3.condition)