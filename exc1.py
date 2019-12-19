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
# item 1-2
text = """
Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!
"""

# item 3
