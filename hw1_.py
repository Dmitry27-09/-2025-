import string
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    10 самых длинных и уник слов.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()

    word_scores = {}
    for word in words:
        word_score = len(set(word)) / len(word)
        word_scores[word] = word_score

    sorted_by_length_and_uniqueness = sorted(
        word_scores.items(),
        key=lambda item: (-len(item[0]), -item[1]),
        reverse=False
    )

    return [word for word, _ in sorted_by_length_and_uniqueness][:10]


def get_rarest_char(file_path: str) -> str:
    """
    редкий символ
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    char_counter = Counter(content)
    min_count = float('inf')
    rarest_char = ''

    for char, count in char_counter.items():
        if count < min_count:
            min_count = count
            rarest_char = char

    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    """
    считаем кол-во знаков в документе
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    punctuation_chars = set(string.punctuation)
    counter = 0

    for char in content:
        if char in punctuation_chars:
            counter += 1

    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """
    количество небуквенно-цифровых символов в документе
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    counter = 0

    for char in content:
        if ord(char) > 127:
            counter += 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    самый частый небуквенно-цифровой символ в документе
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    non_ascii_chars = []

    for char in content:
        if ord(char) > 127:
            non_ascii_chars.append(char)

    if non_ascii_chars:
        return Counter(non_ascii_chars).most_common(1)[0][0]
    else:
        return ""
# Использование файла data.txt
file_path = 'data.txt'
# Сохранение результата вызова функции в переменную
longest_diverse_words = get_longest_diverse_words(file_path)
rarest_char = get_rarest_char(file_path)
punctuation_count = count_punctuation_chars(file_path)
non_ascii_count = count_non_ascii_chars(file_path)
most_common_non_ascii = get_most_common_non_ascii_char(file_path)

print("Десять самых длинных и разнообразных слов:", longest_diverse_words)
print("Самый редкий символ:", rarest_char)
print("Количество знаков пунктуации:", punctuation_count)
print("Количество небуквенно-цифровых символов:", non_ascii_count)
print("Самый частый небуквенно-цифровой символ:", most_common_non_ascii)