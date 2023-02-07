def searcher():
    import time
    book = "THis harry and codewithharry and harry like good"
    # funtion which consume time
    time.sleep(4)

    while True:
        text = (yield)

        if text in book:
            print("Your text is in the book")

        if text not in book:
            print("Your text is not in book")


search = searcher()
print("Your search is started")
next(search)
print("Next method run")
search.send("harry")
input("Press any key")
search.send("ap")

search.close()

# search.send("ar")