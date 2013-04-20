words = [
    'abacus',
    'deltoid',
    'gaff',
    'giraffe',
    'microphone',
    'reef',
    'qar'
]

letters = [
    'a',
    'e',
    'f',
    'f',
    'g',
    'i',
    'r',
    'q',
]



def find_longest_word(words, letters):
    # Maintain a global map of letter counts to check against
    table = {}
    for letter in letters:
        table[letter] = table.get(letter, 0) + 1

    longest = ''
    for word in words:
        # Construct a letter map for this word and short circuit if the word is not valid
        wordtable = {}
        valid = True
        for letter in word:
            wordtable[letter] = wordtable.get(letter, 0) + 1
            if wordtable[letter] > table.get(letter, 0):
                valid = False
                break

        if valid and len(word) > len(longest):
            longest = word

    return longest



print find_longest_word(words, letters)

