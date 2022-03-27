import json

jfile = open("library.json", "r")

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

jfile = open("D:\\Programming\\LibrProject\\library.json", "w")

newdict = json.dumps(updated, indent=4)

jfile.write(newdict)

jfile.close()