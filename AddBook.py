import json
import os 

<<<<<<< HEAD
dir_path = os.path.dirname(os.path.realpath(__file__))

jfile = open(dir_path+"\\library.json", "r")
=======
jfile = open("/library.json", "r")
>>>>>>> 2df766c38e3adc583e3bd5aee71f78cbc5d9d638

dict = json.load(jfile)

books = dict.get("books")

count = 1

for i in books:
    title = i.get("title")
    print(count, title)
    count += 1

print("Add new book: ")

title = input("title: ")

author = input("author: ")

publisher = input("publisher: ")

pages = int(input("pages: "))

description = input("description: ")


books.append({"title":title, "author":author, "publisher":publisher, "pages":pages, "description":description})

updated = {"books":books}

print(updated)

jfile.close()

<<<<<<< HEAD
jfile = open(dir_path+"\\library.json", "w")
=======
jfile = open("/library.json", "w")
>>>>>>> 2df766c38e3adc583e3bd5aee71f78cbc5d9d638

newdict = json.dumps(updated, indent=4)

jfile.write(newdict)

jfile.close()
