"""
Вопросы:
1. Задание 5:   - зачем условие "index != 0" ?
                - зачем 'continue'?
2. Задание 6:   - text = 'ahbcdefg ABAB ahbcdefg1' - выводит только до "b"?
3. Сортировка:
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])} - ??
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}


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
def count_vowels1(text, vowels="AeEeIiOoUu"):
    number_of_vowels = 0
    for vowel in text:
        if vowel in vowels:
            number_of_vowels += 1
    print("Всего гласных: " + str(number_of_vowels))
count_vowels1(text)

def count_vowels2(text, vowels="AeEeIiOoUu"):
    all_vowels = [vowel for vowel in text if vowel in vowels]
    print("Всего гласных: " + str(len(all_vowels)))
count_vowels2(text)


# 5. Выведи на экран каждый (внимательно!) 18ый символ текста в измененном регистре (А если а, и наоборот),
# при печати добавь к символу позицию этого символа в тексте, например:
# 18,
# 36,
# 54
# Избегай скобок при печати, как, например (18, ,)
print("5. Каждый 18-й")
def every_18th_symbol(text):
    for index, letter in enumerate(text, 1):
        if index != 0 and index % 18 != 0:
            continue
        print(f"{letter.swapcase()} {index}")
every_18th_symbol(text)

def every_18th_symbol1(text):
    for index, letter in enumerate(text, 1):
        if index % 18 == 0:
            print(f"{letter.swapcase()} {index}")
every_18th_symbol1(text)


# 6. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в алфавитном
# порядке.
print("6. Сортировка по символам в алфавитном порядке. Список")
def symbol_index(text):
    # Получить сортировку сета с учетом заглавных букв (что б он были не в конце, как по дефолту в sorted)
    sorted_set_of_text = sorted(set(text), key=lambda v: (v.lower(), v.islower()))
    # Создане списка с учетом позиции буквы в тексте
    list = []
    for index, letter in enumerate(text, 1):
        list.append([letter.swapcase(), index])
   # Вывод на печать с учетом сортировки по символам в алфавитном порядке
    for sym in sorted_set_of_text:
        for letter in list:
            if letter[0] == sym:
                print(str(letter[0]) + " " + str(letter[1]))
symbol_index(text)

print("6. Сортировка по символам в алфавитном порядке. Словарь")
def symbol_index(text):
    # Создане словаря с учетом позиции буквы в тексте
    dict = {}
    for index, letter in enumerate(text, 1):
        dict[index] = letter.swapcase()
    # Сортировка словаря по значениям
    sorted_list_of_tuples = sorted(dict.items(), key=lambda x: x[1])
    # Вывод на печать
    for element in sorted_list_of_tuples:
        print(str(element[1]) + " " + str(element[0]))
symbol_index(text)


# 7. Отпечатай на экран ту-же информацию о каждом символе в тексте, только отсортированной по символам в порядке частоты
# встречаемости символов.
print("7. Сортировка по символам в в порядке частоты встречаемости символов.")
from collections import Counter

def popular_symbol(text):
    dict = {}
    for index, letter in enumerate(text, 1):
        dict[index] = letter.swapcase()
    sorted_values = sorted(dict.items(), key=lambda x: x[1])  # -> List of sorted pairs as the tuples
    data = []
    for item in sorted_values:
        data.append({item[1]: item[0]})
    counts = Counter([list(d.keys())[0] for d in data])
    data_sorted = sorted(data,
                         key=lambda item: counts[list(item.keys())[0]],  # function to lookup freq from counts
                         reverse=True)
    for i in data_sorted:
        for kv in i.items():
            print(f"{kv[0]} {kv[1]}")
popular_symbol(text)


# Another solution without Counter
print("7. Сортировка по символам в в порядке частоты встречаемости символов. Без Counter")
def popular_symbol_2(text):
    # Create a list of lists with letters and their indexes
    list_of_letters = []
    for index, letter in enumerate(text, 1):
        list_of_letters.append([index, letter])

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
        for i in range(len(list_of_letters)):
            if list_of_letters[i][1] == key:
                list_tripple.append([value, list_of_letters[i][0], list_of_letters[i][1]])

    # Sort sub-lists by frequency
    sorted_list = sorted(list_tripple, key=lambda e: e[0], reverse=True)

    # Print each letter by frequency with their unique index value in the changed register
    for lis in sorted_list:
        print(f"{lis[2].swapcase()} {lis[1]}")

popular_symbol_2(text)

