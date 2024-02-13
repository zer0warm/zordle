import random

def red(s: str) -> str:
    return ''.join(('\033[31m', s, '\033[m'))

def green(s: str) -> str:
    return ''.join(('\033[32m', s, '\033[m'))

def yellow(s: str) -> str:
    return ''.join(('\033[33m', s, '\033[m'))

def colorize(word: str, guess: str) -> str:
    res = ''
    for i in range(len(guess)):
        c = guess[i]
        if c in word and word[i] == c:
            res += green(c)
        elif c in word:
            res += yellow(c)
        else:
            res += red(c)
    return res

def pick(file: str) -> str:
    with open(file) as f:
        wordlist = f.read().splitlines()
    return random.choice(wordlist)

if __name__ == '__main__':
    print('Wordle: Hello!')
    print('Wordle: Word is picked. Turn is yours.')

    word = pick('five.txt').upper()
    turn = 1

    while turn <= 6:
        guess = input('> ').upper()
        if len(guess) != len(word):
            print('Wordle: Must be exactly', len(word), 'characters!')
            continue
        print('==>', colorize(word, guess))
        if guess == word:
            print('Wordle: You won. Congratulations!')
            break
        turn += 1
    else:
        print('Wordle: Word is', word)
        print('Wordle: You lost. There will always be next time!')
