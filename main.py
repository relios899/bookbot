def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = character_counts(book_text)
    list_of_character_counts = convert_to_list_of_dicts(char_count)
    print(list_of_character_counts)
    print_results(book_path, word_count, list_of_character_counts)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_counts(text):
    character_tracker = {}
    for character in text:
        lowercase_character = character.lower()
        if lowercase_character not in character_tracker:
            character_tracker[lowercase_character] = 0
        character_tracker[lowercase_character] += 1
    return character_tracker

def sort_on(character_count):
    return character_count["count"]

def convert_to_list_of_dicts(char_count):
    list_of_character_counts = []
    for key in char_count:
        if key.isalpha():
            list_of_character_counts.append({"character": key, "count": char_count[key]})
    list_of_character_counts.sort(reverse=True, key=sort_on)
    return list_of_character_counts


def print_results(book_path, word_count, character_count_list):
    print(f"---begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for character_count in character_count_list:
        character = character_count["character"]
        count = character_count["count"]
        print(f"The '{character}' character was found {count} times")
    print("--- end of report ---")





main()
