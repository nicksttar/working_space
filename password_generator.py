import random
import time
from string import ascii_uppercase, ascii_lowercase, digits


def valid_answer(a):
    if a == "Y" or a == "N":
        return True
    return False


def valid_number(a):
    if a.isdigit() is True:
        return True
    return False


digits = digits
lower_letters = ascii_lowercase
upper_letters = ascii_uppercase
symbols = "#!$%&*+-=?@^_"
print("----------Приветствую вас в генераторе паролей----------")
print()


def script():
    while True:
        amount = input("Введите количество паролей для генерации: ")
        if valid_number(amount) is True:
            break
        else:
            print("Введите число...")
            continue
    while True:
        long = input("Введите длину одного пароля: ")
        if valid_number(long) is True:
            break
        else:
            print("Введите число...")
            continue
    while True:
        numbers = input("Включать ли цифры (Y - Yes, N - No): ")
        if valid_answer(numbers) is True:
            break
        else:
            print("Введите только Y или N")
            continue
    while True:
        letters_u = input("Включать ли прописные буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ (Y - Yes, N - No): ")
        if valid_answer(letters_u) is True:
            break
        else:
            print("Введите только Y или N")
            continue
    while True:
        letters_l = input("Включать ли строчные буквы: abcdefghijklmnopqrstuvwxyz (Y - Yes, N - No): ")
        if valid_answer(letters_l) is True:
            break
        else:
            print("Введите только Y или N")
            continue
    while True:
        symbols_1 = input("Включать ли символы: !#$%&*+-=?@^_?: (Y - Yes, N - No): ")
        if valid_answer(symbols_1) is True:
            break
        else:
            print("Введите только Y или N")
            continue
    while True:
        symbols_2 = input("Исключать ли неоднозначные символы il1Lo0O:O (Y - Yes, N - No): ")
        if valid_answer(symbols_2) is True:
            break
        else:
            print("Введите только Y или N")
            continue
    print("----------Ваши пароли готовы----------")
    time.sleep(1)
    for i in range(int(amount)):
        counter = 0
        chars = []
        while counter != int(long):
            if numbers == "Y" and counter != int(long):
                list(digits)
                chars.append(random.choice(digits))
                counter += 1
            if letters_l == "Y" and counter != int(long):
                list(lower_letters)
                chars.append(random.choice(lower_letters))
                counter += 1
            if letters_u == "Y" and counter != int(long):
                list(upper_letters)
                chars.append(random.choice(upper_letters))
                counter += 1
            if symbols_1 == "Y" and counter != int(long):
                list(symbols)
                chars.append(random.choice(symbols))
                counter += 1
            if symbols_2 == "Y":
                for j in chars:
                    if j in "il1Lo0O:O":
                        counter2 = chars.count(j)
                        counter -= counter2
                        chars.remove(j)
        random.shuffle(chars)
        print("Пароль: ", *chars, sep="")


script()

while True:
    print()
    end_answer = input("Сгенерировать еще паролей: ")
    if valid_answer(end_answer) is True:
        if end_answer == "Y":
            time.sleep(1)
            script()
        if end_answer == "N":
            print("See you next time...")
            time.sleep(1)
            break
    else:
        print("Введите Y или N")
        continue
# try to sell it on Google authenticator hd
# that's all, nothing to fix and update
# upload string mb faster IDK
