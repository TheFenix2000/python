import os

def convert(dirname):
    new_extension = ".docx"
    files = os.listdir(dirname)
    for filename in files:
        if not filename.endswith(".xml"):
            continue

        prefix, extensions = os.path.splitext(filename)
        newly_created_file = os.path.join("./", prefix + new_extension)
        seleected_file = os.path.join(dirname, filename)
        with open(seleected_file, "r") as source:
            with open(newly_created_file, "w+") as converted:
                converted.write(source.read())