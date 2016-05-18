def get_solutions(dictionary, must_have, can_have):
    solutions = []
    for word in dictionary:
        if is_valid_word(word, must_have, can_have):
            solutions.append(word)
    return solutions

def is_valid_word(word, must_have, can_have):
    must_have_letters = list(must_have)
    can_have_letters = list(can_have)

    for letter in word:
        if letter not in (can_have_letters + must_have_letters):
            return False
        if letter in must_have_letters:
            must_have_letters.remove(letter)
        elif letter in can_have_letters:
            can_have_letters.remove(letter)

    #return true if we got to this point and all neccesary letters were used
    return len(must_have_letters) == 0

def load_words_from_file():
    words = []
    with open('words.txt') as dictionary:
        for word in dictionary:
            words.append(word.replace('\n',''))
    return words

def main():
    english_language = load_words_from_file()

    must_have_letters = raw_input('Letters that the word would ideally have: ')
    can_have_letters = raw_input('Other letters on the board that could be used: ')

    solutions = get_solutions(english_language, must_have_letters, can_have_letters)
    
    for solution in solutions:
        print solution

if __name__ == "__main__":
    main()