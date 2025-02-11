def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    alphabet = get_sorted_alpha(characters)
    book_report(book_path, text, words, alphabet)

def get_sorted_alpha(characters):
    alpha = {}
    for character in characters:
        if character.isalpha():
            alpha[character] = characters[character]
    sorted_alpha = dict(sorted(alpha.items(),reverse=True, key=lambda key_val: key_val[1]))
    return sorted_alpha
    



    
    

def word_count(text):
    
    words = text.split()
    count = 0
    for word in words:
        count += 1

    #print(f"Frankenstein has {x} words!")
    return count

def character_count(text):
    #unique = set()
    #for char in text.lower():
    #    if char not in unique:
    #        unique.add(char)

    character_dictionary = {}
    for char in text.lower():
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1

    #print(character_dictionary)
    return character_dictionary

def book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def book_report(book_path, text, words, alphabet):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for each in alphabet:
        print(f"The '{each}' character was found {alphabet[each]} times")
    print("--- End report ---")

main()