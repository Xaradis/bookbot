def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_count = get_count(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sorted_dict(chars_dict)

# print statements
    print(f"--- Begin report of {book_path}---")
    print(f"{num_count} words found in the document")
    print()
# iterating on dict
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
# file contents read
def get_book_text(path):
    with open(path) as f:
        return f.read()
# Count content words
def get_count(text):
    words = text.split()
    return len(words)
# char dictionary for unique
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
# sort dictionary of chars
def sorted_dict(dict):
    return dict["num"]

def get_sorted_dict(num_charsd):
    sorted_list = []
    for ch in num_charsd:
        sorted_list.append({"char": ch, "num": num_charsd[ch]})
    sorted_list.sort(reverse=True, key=sorted_dict)
    return sorted_list
main()


