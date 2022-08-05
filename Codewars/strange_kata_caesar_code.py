s1 = "I should have known that you would have a perfect answer for me!!!"
s = "J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"
shift = 1
shift1 = 1
#"J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def moving_shift(s, shift):
    list_index = [] #здесь будут лежать новые индексы для новой фразы
    new_phrase = [] #здесь будет лежать новая фраза в виде списка
    index_plus_one = shift

    for letter in s:
        if letter.isalpha():
            list_index.append(letters.index(letter.lower()))
        else:
            list_index.append(letter)

    for i in list_index:
        if index_plus_one == 26:
            index_plus_one = 0
        if i in numbers:
            new_phrase.append(letters[i+index_plus_one])
        else:
            new_phrase.append(i)
        index_plus_one += 1

    for letter in range(len(s)):
        if s[letter].isupper():
            new_phrase[letter]= new_phrase[letter].upper()

    new_phrase = ''.join(new_phrase)
    main_part = len(new_phrase)//4

    code_phrase = list(new_phrase[0+i:main_part+i] for i in range(0, len(new_phrase), main_part))

    print(code_phrase)


def demoving_shift(s, shift):
    list_index = [] #здесь будут лежать новые индексы для новой фразы
    new_phrase = [] #здесь будет лежать новая фраза в виде списка
    index_plus_one = shift

    for letter in s:
        if letter.isalpha():
            list_index.append(letters.index(letter.lower()))
        else:
            list_index.append(letter)

    for i in list_index:
        if index_plus_one == 0:
            index_plus_one = 26
        if i in numbers:
            new_phrase.append(letters[i])
        else:
            new_phrase.append(i)
        index_plus_one -= 1

    for letter in range(len(s)):
        if s[letter].isupper():
            new_phrase[letter]= new_phrase[letter].upper()

    new_phrase=''.join(new_phrase)
    print(new_phrase)



moving_shift(s,1)
demoving_shift(s1, shift1)