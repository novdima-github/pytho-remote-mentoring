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
text = """Beautiful is better than ugly.
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
        dict[index+1] = text[index].upper()
        index += 18
    for key, value in dict.items():
        print(f"{value} {key}")

every_18th_symbol(text)

# 6. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в алфавитном
# порядке.
def symbol_index(text):
    dict = {}
    index = 0
    while index < len(text):
        dict[index + 1] = text[index].upper()
        index += 1
    sorted_values = sorted(dict.items(),  key=lambda x: x[1]) #got a list of tuples with alphabetically sorted items
    for item in sorted_values:
        print(f"{item[1]} {item[0]}")

symbol_index(text)

# 7. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в порядке частоты
# встречаемости символов.

from collections import Counter
def popular_symbol(text):
    dict = {}
    index = 0
    while index < len(text):
        dict[index + 1] = text[index].upper()
        index += 1
    sorted_values = sorted(dict.items(),  key=lambda x: x[1])
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

