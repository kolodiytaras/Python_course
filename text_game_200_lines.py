import random
import time

input_var = input("Будь ласка введіть Ваше імя: ")

def million():
    print("Привіт" + " " + input_var)
    input_start = input("Чи готові Ви почати гру? Введіть 1 для так або 2 для ні: ")
    if int(input_start) == 1:
        time.sleep(0.25)
        print("Вам буде поставлено 15 питань і на кожне з них буде запропоновано по 4 варіанта відповіді. ")
        print("Один із варіантів є правильним, три інші - ні. Кожна правильна відповідь буде наближати Вас до перемоги.")
        print("На роздуми кожного питання у Вас буде 10 секунд. У Вас не буде пізказок та допомоги друга.")

        print("")
        print("За декілька секунд Вам буде задано перше питання")
        print("Loading...")
        time.sleep(9)
        print("№1. Твердження, яке доводять: a) аксіома b) гіпотенуза c) теорема d) правило")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")

        if input_asw == "c":
            print("Ваша відповідь вірна. Ви виграли 50 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли")

        print("Наступне питання...")
        time.sleep(3)

        print("№2.  Одиницею часу є: a) 1 км/год b) 1 доба c) 1 см d) 1 а")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "b":
            print("Ваша відповідь вірна. Ви виграли 100 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№3. Яке з даних чисел є простим?: a) 10 b) 7 c) 12 d) 4")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "b":
            print("Ваша відповідь вірна. Ви виграли 150 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№4. Тупокутний трикутник має: a) один тупий кут b) два тупих кута c) три тупих кута d) жодного")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "a":
            print("Ваша відповідь вірна. Ви виграли 150 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№5. Процентом називається: a) половина b) одна десята c) третина d) одна сота частина")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "d":
            print("Ваша відповідь вірна. Ви виграли 250 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№6. Периметр квадрата обчислюється за формулою: a) P = 2a b) P = a c) P = 3a d) P = 4a")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "d":
            print("Ваша відповідь вірна. Ви виграли 1000 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№7. На 5 і 3 ділиться число: a) 71725 b) 55553 c) 33115 d) 24135")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "d":
            print("Ваша відповідь вірна. Ви виграли 2000 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№8. Косинусом гострого кута прямокутного трикутника називається відношення:/"
              " a) прилеглого катета до протилежного b) прилеглого катета до гіпотенузи/"
              " c) протилежного катета до гіпотенузи d) протилежного катета до прилеглого")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "b":
            print("Ваша відповідь вірна. Ви виграли 4000 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№9. Яке число вважалося раніше щасливим?: a) 1 b) 3 c) 7 d) 10")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "c":
            print("Ваша відповідь вірна. Ви виграли 8000 гривень")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

        print("№10. Яка маса горобця?: a) 10 г b) 60 г c) 200 г d) 550 г")

        timer_10()

        input_asw = input("Виберіть відповідь. Введіть тільки одну літеру: ")
        if input_asw == "b":
            print("Ваша відповідь вірна. Ви виграли 16000 гривень")
            print("Нажаль у нас більше не має грошей. На цього наша гра повинна завершитись.")
            print("Надіємось у нас появиться більше грошей, коли ми пересадим всіх корупціонерів!")
        else:
            print("Ваша відповідь не вірна. Ви програли.")

        print("Наступне питання...")
        time.sleep(3)

    else:
        print("Допобачення")
        exit(0)

def timer_10():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("")

if input_var.isalpha():
    print("Loading...")
    time.sleep(3)

    million()

else:
    print("Імя повинно містити тільки літери. Вам не дозволено вводити числа, пробіли та спеціальні символи")

    input_var = input("Будь ласка введіть Ваше імя: ")
    if input_var.isalpha():
        print("Loading...")
        time.sleep(3)
        million()
    else:
        print("Ви маєте останню спробу для вводу коректного імені")

        input_var = input("Please enter your name: ")
        if input_var.isalpha():
            print("Loading...")
            time.sleep(3)
            million()
        else:
            print("Вибачте. Ви ввели не коректне імя")
            exit(0)