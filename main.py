def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path);
    book_words = get_book_words(book_text)
    book_letters = get_book_letters(book_words)
    book_letters_list = generate_letter_list(book_letters)
    print_book_report(book_path, book_words, book_letters_list)

def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def get_book_words(text):
    return text.split()

def get_book_letters(words):
    letter_dict = {}
    for w, word in enumerate(words):
        for c, character in enumerate(word):
            new_char = character.lower()
            
            if new_char in letter_dict.keys():
                letter_dict[new_char] += 1
            else:
                letter_dict[new_char] = 1
    
    return letter_dict

def generate_letter_list(letters):
    letters_list = []
    for key, val in letters.items():
        if str.isalpha(key):
            letters_list.append((key, val))

    letters_list.sort(key=lambda i:i[1], reverse=True)
    return letters_list

def print_book_report(book, words, letters):
    print(f'--- Begin report of {book} ---')
    print(f'{len(words)} words found in the document.')
    print()

    for item in letters:
        print(f'The \'{item[0]}\' character was found {item[1]} times')
    
    print(f'--- End report ---')

main()