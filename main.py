def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        #Commented out, someone else will have to approve re-adding the entire text of frankenstein
        #print(file_contents)

        wordcount = word_counter(file_contents)
        print(f"Wordcount: {wordcount}")

        character_dictionary = character_counter(file_contents)
        character_printer(character_dictionary)


    return

#counts the number of words in the book
def word_counter(book_to_count):
    book_word_by_word = book_to_count.split()

    wordcount = 0
    for words in book_word_by_word:
        wordcount += 1

    return (wordcount)


#counts the characters, then returns them in a sorted dictionary
def character_counter(book_to_count):
    book_lowercase_letters = list(book_to_count.lower())
    character_dictionary = {}

    for character in book_lowercase_letters:
        if character in character_dictionary:
            character_dictionary[character] +=1
        
        else:
            character_dictionary[character] = 1

    sorted_dict_keys = sorted(character_dictionary.keys())
    character_dictionary_sorted = {}
    for key in sorted_dict_keys:
        character_dictionary_sorted[key] = character_dictionary[key]

    return character_dictionary_sorted

#function that prints the characters and their counts
def character_printer(lettercount_dict):
    for character in lettercount_dict:
        print(f"{character}: {lettercount_dict[character]}")
    return

    

main()