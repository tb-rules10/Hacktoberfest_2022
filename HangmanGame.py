import random
 
def selected_a_word():
    words = ['working', 'hard', 'makes', 'things', 'easier', 'congrats', 'programming', 'hero']
    word = words[random.randint(0, len(words)-1)]
    return word
 
def get_blank_word(word):
    blank_word = word[0]
    for i in range(1, len(word)):
            blank_word += '_'
    return blank_word
 
def word_hangman(word, so_far, letter, try_left):
    bad_try = True
    for i in range(0, len(word)):
            if word[i] == letter:
                    so_far = so_far[:i]+letter+so_far[i+1:]
                    bad_try = False
    if bad_try is True:
            try_left -= 1
            print('Wrong Try Left: ', try_left)
    print('so far you got: ', so_far)
    if word == so_far:
            print('YAY!!! You Win')
    elif try_left == 0:
            print('Opps!!! You Lost')
    else:
     next_letter = input ('Enter your next letter: ')
     word_hangman(word, so_far, next_letter, try_left)
 
# play the game
word = selected_a_word()
clue_word = get_blank_word(word)
word_hangman(word, clue_word, word[0], 5)
