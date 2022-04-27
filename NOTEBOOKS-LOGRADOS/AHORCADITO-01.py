#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'celular',
    'cuarentena',
    'virus',
    'smartphone',
    'zapatillas',
    'frazadas',
    'verdura',
    'murcielago',
    'antibiotico',
    'paranormal',
    'paralelogramo',
    'triangulo',
    'paralelepipedo',
    'orangutan',
    'rinoceronte',
    'purmamarca',
    'humahuaca',
    'panificadora',
    'estereotipo',
    'continente',
    'parapsicologo',
    'diatomeas',
    'euglenidos',
    'poaceas',
    'oceanografia'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- * --- * ---')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))
        print ('Desaciertos: ', tries)

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word,tries)
                print('')
                print(f'¡Perdiste! La palabra correcta era: {word}')
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print(f'¡Felicidades! Ganaste. La palabra es: {word}')
            break

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()

