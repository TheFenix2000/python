class Robot:
    def __init__(self, name):
        print(name + " has been created!")

    def __del__(self):
        print("Robot has been destroyed!")

if __name__ == "__main__":
    x = Robot('Great-bot')
    y = Robot('Nice-bot')

    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y