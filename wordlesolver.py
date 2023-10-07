from playwright.sync_api import sync_playwright
import time, random
from etext import send_mms_via_email
from emoji import emojize
import io
from datetime import date
from bestwords import *
from credentials import *

def avoid_rules(page):
    #page.query_selector('.purr-blocker-card__button').click()
    page.get_by_test_id('Play').click()
    page.get_by_test_id('icon-close').click()

def press_letter(page, key):
    page.locator(f'[data-key={key}]').click()

def guess_word(page, word):
    for letter in word:
        press_letter(page, letter)
    press_letter(page, '↵')

def get_hints(page, guess_num):
    rows = []
    for i in range(1, 7):
        rows.append(page.get_by_label(f'Row {i}'))
    tiles = rows[guess_num-1].get_by_test_id('tile').all()
    
    #get_letter = lambda tile: tile.get_attribute('aria-label').split(' ')[0]
    #get_evaluation = lambda tile: tile.get_attribute('data-state')

    get_letter = lambda tile: tile.get_attribute('aria-label').split(',')[1][1].lower()
    get_evaluation = lambda tile: tile.get_attribute('aria-label').split(',')[2].split(' ')[1]
    
    hints = [(get_letter(tile), get_evaluation(tile)) for tile in tiles]

    letters = {i[0]: set() for i in hints}
    for hint in hints:
        letters[hint[0]].add(hint[1])

    
    should_replace_absent = lambda letter: len(letters[letter] - set(['absent'])) >= 1
    replace_absent = lambda hint: (hint[0], 'overused') if should_replace_absent(hint[0]) and hint[1] == 'absent' else hint

    modified_hints = list(map(replace_absent, hints))
    #print(modified_hints)
    return modified_hints

def all_correct(page, hints):
    if len(hints) == 0:
        return False
    return all([i[1] == 'correct' for i in hints[-1]])

def generate_hint(word, answer):
    pass

def prune(words, all_hints):
    valid_words = [i for i in words]
    for guess_hints in all_hints:
        keep_correct = lambda word: all([word[i] == guess_hints[i][0] for i in range(len(word)) if guess_hints[i][1] == 'correct'])

        exclude_absent = lambda word: all(i[0] not in word for i in guess_hints if i[1] == 'absent')

        exclude_overused = lambda word: all(guess_hints[i][1] != 'overused' or word[i] != guess_hints[i][0] for i in range(len(guess_hints)))

        letter_count = lambda word: all((hint[1] != 'overused' or word.count(hint[0]) == sum(1 for h in guess_hints if h[1] in ['correct', 'present'] and h[0] == hint[0])) for hint in guess_hints)

        move_present = lambda word: all([word[i] != guess_hints[i][0] and guess_hints[i][0] in word for i in range(len(guess_hints)) if guess_hints[i][1] == 'present'])

        is_valid = lambda word: keep_correct(word) and exclude_absent(word) and exclude_overused(word) and move_present(word) and letter_count(word)

        valid_words = list(filter(is_valid, valid_words))
    
    return valid_words

def select_best(words):
    return best_exponential_half_letter_count(words)

words = []

def load_words():
    global words
    with open('selectwords.txt', 'r') as f:
        words = [i.strip('\n').strip('"') for i in f.read().split(',')]

if __name__ == '__main__':
    load_words()

    today = date.today()
    start = date(2021, 6, 19)
    day = today - start

    with sync_playwright() as p:
        browser = p.chromium.launch(channel = 'msedge', headless = False)
        page = browser.new_page()
        page.goto('https://www.nytimes.com/games/wordle/index.html')
        avoid_rules(page)

        guesses = []
        hints = []
        plausible = [word for word in words]
        best = []

        while not all_correct(page, hints) and len(guesses) < 6:
            best = select_best(plausible)
            random.shuffle(best)
            guesses.append(best[0])
            guess_word(page, guesses[-1])
            time.sleep(2.1)
            hints.append(get_hints(page, len(guesses)))
            plausible = prune(words, hints)

        #print(guesses[-1])
        #print(hints)

        message = ''

        message += f'Wordle {day.days} '
        if all_correct(page, hints):
            message += f'{len(guesses)}/6*\n\n'
        else:
            message += 'X/6\n\n'

        for hint in hints:
            for x in hint:
                if x[1] == 'absent' or x[1] == 'overused':
                    message += emojize(':white_large_square:')
                elif x[1] == 'present':
                    message += emojize(':yellow_square:')
                elif x[1] == 'correct':
                    message += emojize(':green_square:')
                else:
                    message += '_'
            message += '\n'

        sender_credentials = (sender_email, sender_access_token)

        #print(message)

        file_path = 'message.txt'

        mime_maintype = 'text'
        mime_subtype = 'plain'
        
        with open(file_path, 'w', encoding='utf-8') as text_file:
            for guess in guesses:
                text_file.write(guess)
                text_file.write('\n')
            text_file.close()

        send_mms_via_email(phone_number, message, file_path, mime_maintype, mime_subtype, provider, sender_credentials, subject='Wordle')
        
