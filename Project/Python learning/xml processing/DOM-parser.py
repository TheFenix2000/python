from xml.dom.minidom import parse
import xml.dom.minidom
import os

filename = "movies.xml"
path = os.path.join("../files/" + filename)


#otwieranie dokumentu XML przy użyciu minidom parser
DOMTree = xml.dom.minidom.parse(path)
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: %s" % collection.getAttribute("shelf"))

# Weź wszystkie filmy w "collection"
movies = collection.getElementsByTagName("movie")

#Wypisz szczegóły każdego z filmów
for movie in movies:
    print("\n*****Movie*****")
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))
    type = movie.getElementsByTagName("type")[0]
    print("Type: %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print("Format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)