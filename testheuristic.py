import io
import random
from bestwords import *

with open('words.txt', 'r') as f:
    words = [i.strip('\n').strip('"') for i in f.read().split(',')]

with open('selectwords.txt', 'r') as f:
    select_words = [i.strip('\n').strip('"') for i in f.read().split(',')]

results = [' ']

test_count = 0

def generate_hint(guess, answer):
    hints = []
    colors = []
    answerList = list(answer)
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            colors.append('green')
            answerList[i] = None
        else:
            colors.append(None)
    for i in range(len(guess)):
        if colors[i] is None and guess[i] in answerList:
            colors[i] = 'yellow'
            answerList[answerList.index(guess[i])] = None
        elif colors[i] is None:
            colors[i] = 'gray'
    for i in range(len(guess)):
        if colors[i] == 'green':
            hints.append([guess[i], 'correct'])
        elif colors[i] == 'yellow':
            hints.append([guess[i], 'present'])
        else:
            if guess[i] in answer:
                hints.append([guess[i], 'overused'])
            else:
                hints.append([guess[i], 'absent'])
    return hints

def prune(words, guess_hints):
    valid_words = [i for i in words]
    keep_correct = lambda word: all([word[i] == guess_hints[i][0] for i in range(len(word)) if guess_hints[i][1] == 'correct'])
    exclude_absent = lambda word: all(i[0] not in word for i in guess_hints if i[1] == 'absent')
    exclude_overused = lambda word: all(guess_hints[i][1] != 'overused' or word[i] != guess_hints[i][0] for i in range(len(guess_hints)))
    letter_count = lambda word: all((hint[1] != 'overused' or word.count(hint[0]) == sum(1 for h in guess_hints if h[1] in ['correct', 'present'] and h[0] == hint[0])) for hint in guess_hints)
    move_present = lambda word: all([word[i] != guess_hints[i][0] and guess_hints[i][0] in word for i in range(len(guess_hints)) if guess_hints[i][1] == 'present'])
    is_valid = lambda word: keep_correct(word) and exclude_absent(word) and exclude_overused(word) and move_present(word) and letter_count(word)
    valid_words = list(filter(is_valid, valid_words))
    return valid_words

def start_test(heuristic, name, repetitions):
    global test_count
    test_count += 1
    print("Testing Heuristic: " + name)
    add_result("Tested: " + name)
    run_heuristic_test(heuristic, repetitions)
    add_result(' ')
    
def run_heuristic_test(heuristic, repetitions):
    testCount = 0
    succeedCount = 0
    failCount = 0
    tryCount = 0
    allTests = repetitions * len(select_words)
    for answer in select_words:
        for x in range(repetitions):
            guesses = []
            hints = []
            plausible = [word for word in select_words]
            best = []
            while (len(guesses) == 0 or not guesses[-1] == answer) and len(guesses) < 6:
                best = heuristic(plausible)
                random.shuffle(best)
                guesses.append(best[0])
                hints.append(generate_hint(guesses[-1], answer))
                plausible = prune(plausible, hints[-1])
            testCount += 1
            if guesses[-1] == answer:
                succeedCount += 1
                tryCount += len(guesses)
            else:
                failCount += 1
    if testCount != 0:
        successRate = succeedCount / testCount
    else:
        successRate = 0
    if succeedCount != 0:
        averageGuesses = tryCount / succeedCount
    else:
        averageGuesses = 0
    add_result("Succeeded: " + str(succeedCount) + "/" + str(testCount))
    add_result("Failed: " + str(failCount) + "/" + str(testCount))
    add_result("Success Rate: " + str(successRate))
    add_result("Average Guesses: " + str(averageGuesses))

def add_result(result):
    results.append(result)

def display_results():
    for result in results:
        print(result)

test_repetitions = 10

start_test(best_letter_count,  "best_letter_count", test_repetitions)
start_test(best_weighted_letter_count, "best_weighted_letter_count", test_repetitions)
start_test(best_letter_position_count, "best_letter_position_count", test_repetitions)
start_test(best_mixed_letter_position_count, "best_mixed_letter_position_count", test_repetitions)
start_test(best_half_letter_count, "best_half_letter_count", test_repetitions)
start_test(best_squared_half_letter_count, "best_squared_half_letter_count", test_repetitions)
start_test(best_exponential_half_letter_count, "best_exponential_half_letter_count", test_repetitions)
start_test(best_random, "best_random", test_repetitions)

display_results()
