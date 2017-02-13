import random

list_card = ['6П', '7П', '8П', '9П', '10П', 'ВП', 'ДП', 'КП', 'ТП', '6Б', '7Б', '8Б', '9Б', '10Б', 'ВБ', 'ДБ', 'КБ', 'ТБ', '6Х', '7Х', '8Х', '9Х', '10Х', 'ВХ', 'ДХ', 'КХ', 'ТХ', '6Ч', '7Ч', '8Ч', '9Ч', '10Ч', 'ВЧ', 'ДЧ', 'КЧ', 'ТЧ']
list_card2 = ['6П', '7П', '8П', '9П', '10П', 'ВП', 'ДП', 'КП', 'ТП', '6Б', '7Б', '8Б', '9Б', '10Б', 'ВБ', 'ДБ', 'КБ', 'ТБ', '6Х', '7Х', '8Х', '9Х', '10Х', 'ВХ', 'ДХ', 'КХ', 'ТХ', '6Ч', '7Ч', '8Ч', '9Ч', '10Ч', 'ВЧ', 'ДЧ', 'КЧ', 'ТЧ']


random.shuffle(list_card)

first_player = []
second_player = []

for i in list_card:
    if len(first_player) < 6:
        p = list_card.pop()
        first_player.append(p)

for k in list_card:
    if len(second_player) < 6:
        p = list_card.pop()
        second_player.append(p)

cozur = random.choice(list_card)
print(cozur, 'cozur')
list_card.remove(cozur)
print(len(list_card), "len_of_main_list")


print(first_player, "first_player")
print(second_player, "second_player")


pp = random.choice(first_player)

print(pp, "pershuy pishov")


print(pp[-1], type(pp[-1]))
#if any(p[-1] in s for s in second_player):

matching = [s for s in second_player if pp[-1] in s]
matching2 = [s for s in second_player if cozur[-1] in s]
matching3 = matching + matching2
matching3 = set(matching3)
matching3 = list(matching3)
#if (p[-1] in t) and (list_card2.index(p) < list_card2.index(t)):
ind1 = list_card2.index(pp)

def first_move():
    for j in matching3:
        if (ind1 < list_card2.index(j)) or (any(cozur[-1] in string for string in matching3)):
            print(pp, first_player)
            first_player.remove(pp)
            second_player.remove(j)
            break
    else:
        print(pp, first_player)
        first_player.remove(pp)
        second_player.append(pp)

first_move()

print(first_player, "1")
print(second_player, "2")

def adding_cards():
    if len(first_player) < 6:
        first_player.append(list_card[-1])
    if len(second_player) < 6:
        second_player.append(list_card[-1])

adding_cards()

print(first_player, '1')
print(second_player, '2')