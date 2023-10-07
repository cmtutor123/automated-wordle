
def best_letter_count(words):

    letter_counts = [[0 for i in range(5)] for j in range(26)]

    word_values = [0 for word in words]

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            count = sum(1 for j in range(i) if word[j] == letter)
            letter_counts[ord(letter) - ord('a')][count] += 1

    for k in range(len(words)):
        for i in range(len(words[k])):
            letter = words[k][i]
            count = sum(1 for j in range(i) if words[k][j] == letter)
            word_values[k] += letter_counts[ord(letter) - ord('a')][count]

    max_value = 0
    best_words = []
    for i in range(len(word_values)):
        if word_values[i] > max_value:
            max_value = word_values[i]
            best_words = [words[i]]
        elif word_values[i] == max_value:
            best_words.append(words[i])

    return best_words


def best_weighted_letter_count(words):
    letter_counts = [[0 for i in range(5)] for j in range(26)]

    word_values = [0 for word in words]

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            count = sum(1 for j in range(i) if word[j] == letter)
            letter_counts[ord(letter) - ord('a')][count] += 1

    for k in range(len(words)):
        for i in range(len(words[k])):
            letter = words[k][i]
            count = sum(1 for j in range(i) if words[k][j] == letter)
            word_values[k] += letter_counts[ord(letter) - ord('a')][count] * (5 - count)

    max_value = 0
    best_words = []
    for i in range(len(word_values)):
        if word_values[i] > max_value:
            max_value = word_values[i]
            best_words = [words[i]]
        elif word_values[i] == max_value:
            best_words.append(words[i])

    return best_words


def best_letter_position_count(words):
    letter_counts = [[0 for i in range(5)] for j in range(26)]

    word_values = [0 for word in words]

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            letter_counts[ord(letter) - ord('a')][i] += 1

    for k in range(len(words)):
        for i in range(len(words[k])):
            letter = words[k][i]
            word_values[k] += letter_counts[ord(letter) - ord('a')][i]

    max_value = 0
    best_words = []
    for i in range(len(word_values)):
        if word_values[i] > max_value:
            max_value = word_values[i]
            best_words = [words[i]]
        elif word_values[i] == max_value:
            best_words.append(words[i])

    return best_words


def best_mixed_letter_position_count(words):
    letter_counts = [[0 for i in range(5)] for j in range(26)]
    position_counts = [[0 for i in range(5)] for j in range(26)]

    word_values = [0 for word in words]

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            count = sum(1 for j in range(i) if word[j] == letter)
            letter_counts[ord(letter) - ord('a')][count] += 1
            position_counts[ord(letter) - ord('a')][i] += 1

    for k in range(len(words)):
        for i in range(len(words[k])):
            letter = words[k][i]
            count = sum(1 for j in range(i) if words[k][j] == letter)
            word_values[k] += letter_counts[ord(letter) - ord('a')][count]
            word_values[k] += position_counts[ord(letter) - ord('a')][i]

    max_value = 0
    best_words = []
    for i in range(len(word_values)):
        if word_values[i] > max_value:
            max_value = word_values[i]
            best_words = [words[i]]
        elif word_values[i] == max_value:
            best_words.append(words[i])

    return best_words

            
def best_half_letter_count(words):

    letter_counts = [[0 for i in range(5)] for j in range(26)]

    word_values = [0 for word in words]

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            count = sum(1 for j in range(i) if word[j] == letter)
            letter_counts[ord(letter) - ord('a')][count] += 1

    half = len(words) / 2

    for i in range(26):
        for j in range(5):
            letter_counts[i][j] = half - abs(half - letter_counts[i][j])

    for k in range(len(words)):
        for i in range(len(words[k])):
            letter = words[k][i]
            count = sum(1 for j in range(i) if words[k][j] == letter)
            word_values[k] += letter_counts[ord(letter) - ord('a')][count]

    max_value = 0
    best_words = []
    for i in range(len(word_values)):
        if word_values[i] > max_value:
            max_value = word_values[i]
            best_words = [words[i]]
        elif word_values[i] == max_value:
            best_words.append(words[i])

    return best_words


def best_squared_half_letter_count(words):

    letter_counts = [[0 for i in range(5)] for j in range(26)]

    word_values = [0 for word in words]

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            count = sum(1 for j in range(i) if word[j] == letter)
            letter_counts[ord(letter) - ord('a')][count] += 1

    half = len(words) / 2

    for i in range(26):
        for j in range(5):
            letter_counts[i][j] = half - abs(half - letter_counts[i][j])
            letter_counts[i][j] *= letter_counts[i][j]

    for k in range(len(words)):
        for i in range(len(words[k])):
            letter = words[k][i]
            count = sum(1 for j in range(i) if words[k][j] == letter)
            word_values[k] += letter_counts[ord(letter) - ord('a')][count]

    max_value = 0
    best_words = []
    for i in range(len(word_values)):
        if word_values[i] > max_value:
            max_value = word_values[i]
            best_words = [words[i]]
        elif word_values[i] == max_value:
            best_words.append(words[i])

    return best_words


def best_exponential_half_letter_count(words):

    letter_counts = [[0 for i in range(5)] for j in range(26)]

    word_values = [0 for word in words]

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            count = sum(1 for j in range(i) if word[j] == letter)
            letter_counts[ord(letter) - ord('a')][count] += 1

    half = len(words) / 2

    for i in range(26):
        for j in range(5):
            letter_counts[i][j] = half - abs(half - letter_counts[i][j])
            letter_counts[i][j] *= pow(letter_counts[i][j], 5)

    for k in range(len(words)):
        for i in range(len(words[k])):
            letter = words[k][i]
            count = sum(1 for j in range(i) if words[k][j] == letter)
            word_values[k] += letter_counts[ord(letter) - ord('a')][count]

    max_value = 0
    best_words = []
    for i in range(len(word_values)):
        if word_values[i] > max_value:
            max_value = word_values[i]
            best_words = [words[i]]
        elif word_values[i] == max_value:
            best_words.append(words[i])

    return best_words

def best_random(words):
    return words
