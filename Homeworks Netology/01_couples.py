boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma']

couples = zip(sorted(boys), sorted(girls))

if len(boys) == len(girls):
    print("Идеальные пары:")
    for i in couples:
        print(f"{i[0]} и {i[1]}")
else:
    print("Кажется, кто-то может остаться без пары!")