"""
1. В консоли запусти: python -c “import this”
2. Текст с результатом просто скопируй в переменную в скрипте, например <text>
(не нужно никаких захватов stdout и rot кодеков)
3. Выведи на экран длину текста
4. Выведи на экран количество всех гласных в тексте
5. Выведи на экран каждый (внимательно!) 18ый символ текста в измененном регистре (А если а, и наоборот),
при печати добавь к символу позицию этого символа в тексте, например:
18,
36E
54
Избегай скобок при печати, как, например (18, ,)
6. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в алфавитном
порядке.
7. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в порядке частоты
встречаемости символов.
"""
# 1-2. python -c “import this”
text = """Beautiful is bettEr than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 3. Выведи на экран длину текста
len_text = len(text)
print(f"Длина текста: {len_text} символа")

# 4. Выведи на экран количество всех гласных в тексте
def count_vowels1(text, vowels = "AeEeIiOoUu"):
    all_vowels = ""
    for vowel in text:
        if vowel in vowels:
            all_vowels += vowel
    print("Всего гласных: " + str(len(all_vowels)))

count_vowels1(text)

def count_vowels2(text, vowels = "AeEeIiOoUu"):
    all_vowels = [vowel for vowel in text if vowel in vowels]
    print("Всего гласных: " + str(len(all_vowels)))

count_vowels2(text)

# 5. Выведи на экран каждый (внимательно!) 18ый символ текста в измененном регистре (А если а, и наоборот),
# при печати добавь к символу позицию этого символа в тексте, например:
# 18,
# 36,
# 54
# Избегай скобок при печати, как, например (18, ,)
def every_18th_symbol(text):
    dict = {}
    index = 17
    while index < len(text):
        dict[index+1] = text[index]
        index += 18
    for key, value in dict.items():
        if value.isupper():
            print(f"{value.lower()} {key}")
        else:
            print(f"{value.upper()} {key}")

every_18th_symbol(text)

# 6. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в алфавитном
# порядке.
def symbol_index(text):
    set_of_text = set(text)
    # How to do this automatically??
    sorted_set_of_text = ['\n', ' ', '!', "'", '*', ',', '-', '.', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f',
    'g', 'h', 'I', 'i', 'k', 'l', 'm', 'N', 'n', 'o', 'p', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'v', 'w', 'x', 'y']
    list = []
    for i in range(len(text)):
        list.append([text[i], i + 1])
    for sym in sorted_set_of_text:
        for i in list:
            if i[0] == sym:
                if str(i[0]).isupper():
                    print(str(i[0].lower()) + " " + str(i[1]))
                else:
                    print(str(i[0].upper()) + " " + str(i[1]))

symbol_index(text)

# 7. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в порядке частоты
# встречаемости символов.

from collections import Counter
def popular_symbol(text):
    dict = {}
    index = 0
    while index < len(text):
        dict[index + 1] = text[index]
        index += 1
    sorted_values = sorted(dict.items(),  key=lambda x: x[1]) # -> List of sorted pairs as the tuples
    data = []
    for item in sorted_values:
        data.append({item[1]:item[0]})
    counts = Counter([list(d.keys())[0] for d in data])
    data_sorted = sorted(data,
        key=lambda item: counts[list(item.keys())[0]],  # function to lookup freq from counts
        reverse=True)
    for i in data_sorted:
        for kv in i.items():
            print(f"{kv[0]} {kv[1]}")

popular_symbol(text)


    # Another solution without Counter
def popular_symbol_2(text):
    # Create a list of lists with letters and their indexes
    data = []
    index = 0
    while index < len(text):
        data.append([index, text[index]])
        index += 1

    # Create a dict of letters frequency
    all_freq = {}
    for i in text:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    # Add frequency as the third value of each sub-list
    list_tripple = []
    for key, value in all_freq.items():
        for i in range(len(data)):
            if data[i][1] == key:
                list_tripple.append([value, data[i][0], data[i][1]])

    # Sort data(sub-lists) by frequency
    s_data = sorted(list_tripple, key=lambda e: e[0], reverse=True)

    # Print each letter by frequency with their unique index value in the changed register
    for lis in s_data:
        if lis[2].isupper():
            print(f"{lis[2].lower()} {lis[1]}")
        else:
            print(f"{lis[2].upper()} {lis[1]}")

popular_symbol_2(text)
