queries = [
       'смотреть сериалы онлайн',
       'новости спорта',
       'афиша кино',
       'курс доллара',
       'сериалы этим летом',
       'курс по питону',
       'сериалы про спорт'
]

words = [len(i.split()) for i in queries]

for i in set(words):
       print(f"Поисковых запросов из {i} слов: {int(words.count(i)/len(words)*100)}%")