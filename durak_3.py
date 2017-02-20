
import random


list_card = ['6П', '7П', '8П', '9П', '10П', 'ВП', 'ДП', 'КП', 'ТП', '6Б', '7Б', '8Б', '9Б', '10Б', 'ВБ', 'ДБ', 'КБ', 'ТБ', '6Х', '7Х', '8Х', '9Х', '10Х', 'ВХ', 'ДХ', 'КХ', 'ТХ', '6Ч', '7Ч', '8Ч', '9Ч', '10Ч', 'ВЧ', 'ДЧ', 'КЧ', 'ТЧ']
list_card2 = ['6П', '7П', '8П', '9П', '10П', 'ВП', 'ДП', 'КП', 'ТП', '6Б', '7Б', '8Б', '9Б', '10Б', 'ВБ', 'ДБ', 'КБ', 'ТБ', '6Х', '7Х', '8Х', '9Х', '10Х', 'ВХ', 'ДХ', 'КХ', 'ТХ', '6Ч', '7Ч', '8Ч', '9Ч', '10Ч', 'ВЧ', 'ДЧ', 'КЧ', 'ТЧ']


random.shuffle(list_card)

name_1 = input("Гравець 1 будь ласка введіть Ваше імя: ")
name_2 = "Компютер"


list_names = []
list_names.append(name_1)
list_names.append(name_2)
random_player = random.choice(list_names)

print("Першим робить хід гравець " + random_player)

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
print('Козир - ', cozur)

list_card.remove(cozur)
list_card = [cozur] + list_card

def first_move(random_player):
    if random_player == name_1:
        print(first_player)
        pp = input("Виберіть одну карту з колоди: ")
        #print(pp)
        return pp
    else:
        kk = random.choice(second_player)
        print("компютер походив: " + kk)
        return kk

result_of_funct = first_move(random_player)


def main_program():
    global result_of_funct
    if result_of_funct in first_player:
        all_cards_player = [s for s in second_player if result_of_funct[-1] in s]
        all_cozur_player = [s for s in second_player if cozur[-1] in s]

        all_cards_player = [x for (x, y) in sorted(zip(all_cards_player, list_card2))]
        all_cozur_player = [x for (x, y) in sorted(zip(all_cozur_player, list_card2))]

        all_cards_second_player = all_cards_player + all_cozur_player


        one_card_index = list_card2.index(result_of_funct)



        for j in all_cards_second_player:
            if ((one_card_index < all_cards_player.index(j)) or (any(cozur[-1] in string for string in all_cards_second_player))):
                first_player.remove(result_of_funct)

                if (result_of_funct[-1] == j[-1]) and (one_card_index < list_card2.index(j)):
                    second_player.remove(j)
                else:
                    for p in all_cozur_player:
                        if list_card2.index(p) > list_card2.index(j):
                            second_player.remove([p])
                            if (len(list_card) > 0) and (len(first_player) < 7):
                                first_player.append(list_card[-1])
                            if (len(list_card) > 0) and (len(second_player) < 7):
                                second_player.append(list_card[-1])
                        else:
                            second_player.append(j)
                            print("Карта не була успішно побита " + name_2)
                            print("Знов ходить гравець " + name_1)
                            result_of_funct = first_move(name_1)

                print("Карта успішно побита копютером")

                if (len(list_card) > 0) and (len(first_player) < 7):
                    first_player.append(list_card[-1])
                if (len(list_card) > 0) and (len(second_player) < 7):
                    second_player.append(list_card[-1])
                    break

                #break
        else:
            first_player.remove(result_of_funct)
            second_player.append(result_of_funct)

            if len(list_card) > 0:
                first_player.append(list_card[-1])
            else:
                first_player.append(cozur)

            first_move(name_1)

        #result_of_funct = first_move(name_2)

        result_of_funct = first_move(name_2) #!!!!!!!!! from 101

    elif result_of_funct in second_player:

        # print('У Вас на руках такі карти ')
        # print(first_player)
        # print("")
        # one_card_input = input("Виберіть одну з карт щоб побити карту противника. Якщо у Вас немає чим побити карту,"
        #                        " то ви повинні взяти її: ")
        #
        #
        # first_player.remove(one_card_input)



        all_cards_player = [s for s in first_player if result_of_funct[-1] in s]
        all_cozur_player = [s for s in first_player if cozur[-1] in s]

        all_cards_player = [x for (x, y) in sorted(zip(all_cards_player, list_card2))]
        all_cozur_player = [x for (x, y) in sorted(zip(all_cozur_player, list_card2))]
        all_cards_first_player = all_cards_player + all_cozur_player

        all_cards_first_player = set(all_cards_first_player)

        one_card_index = list_card2.index(result_of_funct)

        for j in all_cards_first_player:
            # if (one_card_index < list_card2.index(j)) or (any(cozur[-1] in string for string in all_cards_first_player)):
            #     second_player.remove(result_of_funct)
             if ((result_of_funct[-1] == j[-1]) and (one_card_index < list_card2.index(j))) or (any(cozur[-1] in string for string in all_cards_first_player)):
                second_player.remove(result_of_funct)
                print('У Вас на руках такі карти ')
                print(first_player)
                print("")
                one_card_input = input(
                    "Виберіть одну з карт щоб побити карту противника. Якщо у Вас немає чим побити карту,"
                    " то ви повинні взяти її ")
                first_player.remove(one_card_input)

            else:
                for p in all_cozur_player:
                    if list_card2.index(p) > list_card2.index(j):
                        print('У Вас на руках такі карти ')
                        print(first_player)
                        print("")
                        one_card_input = input(
                            "Виберіть одну з карт щоб побити карту противника. Якщо у Вас немає чим побити карту,"
                            " то ви повинні взяти її ")

                        first_player.remove(one_card_input)

                        if (len(list_card) > 0) and (len(first_player) < 7):
                            first_player.append(list_card[-1])
                        elif (len(list_card) > 0) and (len(second_player) < 7):
                            second_player.append(list_card[-1])
                    else:
                        first_player.append(j)
                        print("Карта не була успішно побита " + name_2)
                        print("Знов ходить гравець " + name_1)
                        result_of_funct = first_move(name_1)

            print("Карта успішно побита " + name_1)

            if len(list_card) > 0:
                first_player.append(list_card[-1])
                second_player.append(list_card[-1])
                break
            else:
                if len(first_player) > len(second_player):
                    first_player.append(cozur)
                else:
                    second_player.append(cozur)

        else:
            first_player.remove(result_of_funct)
            second_player.append(result_of_funct)

            if len(list_card) > 0:
                first_player.append(list_card[-1])
            else:
                first_player.append(cozur)

            result_of_funct = first_move(name_2)

        result_of_funct = first_move(name_1)

while (len(first_player) != 0) or (len(second_player) != 0):
    main_program()
