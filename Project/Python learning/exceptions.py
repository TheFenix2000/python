import os
#to zadziała
def Open(filename):
    path = os.path.join("files/" + filename)
    """try:
        file = open(path, "w")
        file.write("This is working")
    except IOError:
        print("Can't find or write into file")
    else:
        print("Successfully writtedn content in the file")
        file.close()"""
    #a to nie bo nie mamy prawa do zapisu
    """
    try:
        fh = open(path, "r")
        fh.write("This is my test file for exception handling!!")
    except IOError:
        print ("Error: can\'t find file or read data")
    else:
        print ("Written content in the file successfully")
    """
    #elegant way z finally(zawsze się wykonuje)
    try:
        fh = open(path, "w") #zmienić w na r i zobaczyć różnicę
        try:
            fh.write("This is my test file for exception handling!!")
        finally:
            print("Going to close the file")
            fh.close()
    except IOError:
        print("Error: can\'t find file or read data")
Open("test.txt")


