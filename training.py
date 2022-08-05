list = ['2018-01-01', 'yandex', 'cpc', 100]
dict = {}

def recursive()

for i in range(len(list)):
    a = list[i]
    b = list[i+1:]
    dict[a] = b

print(dict)