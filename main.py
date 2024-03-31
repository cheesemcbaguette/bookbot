def main():
    book_path = "books/frankenstein.txt"
    # Get text from filepath
    text = get_book_text(book_path)
    # Get number of words
    num_words = get_num_words(text)
    # Get dictionary of characters
    chars_dict = get_chars_dict(text)
    # Get a sorted list of characters from a characters dictionary
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    # Loop throught every characters
    for item in chars_sorted_list:
        # Ignore non alphanumeric characters
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

# A function that reads text from a filepath
def get_book_text(path):
    with open(path) as f:
        return f.read()

# A function that splits the text into a list of words and returns the length of that list
def get_num_words(text):
    words = text.split()
    return len(words)

# A function that splits the text into a list of words and returns the length of that list
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# A function that creates a dictionary that counts the number of characters
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]


main()




