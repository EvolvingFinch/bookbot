import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    construct_report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(input_text):
    all_words = input_text.split()
    return len(all_words)

def character_counter(input_text):
    my_text = input_text.lower()

    out_dic = {}

    for char in my_text:
        if char not in out_dic.keys():
            out_dic[char] = 1
        else:
            out_dic[char] += 1

    return out_dic

def construct_report(book_path, text):
    word_count = count_words(text)
    char_count = character_counter(text)

    filtered_dic = {key: char_count[key] for key in list(string.ascii_lowercase)}
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    print()
    print()
    
    for i in filtered_dic.keys():
        print(f"the '{i}' character was found {filtered_dic[i]} times")

main()