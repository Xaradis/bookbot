def edit_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
edit_text()


