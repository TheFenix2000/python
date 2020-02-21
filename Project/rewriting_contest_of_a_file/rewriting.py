with open("read_from.txt","r") as f:
    with open("write_into.txt","w") as f1:
        for line in f:
            f1.write(line)
