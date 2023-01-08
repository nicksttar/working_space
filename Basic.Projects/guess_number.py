import random
import time

print("Добро пожаловать в числовую угадайку")


def random_generator(b):  # generator of random number
    num = random.randint(1, b)
    return num


def is_valid3(a):  # number check
    if a.isdigit() and int(a) > 1:
        return True
    return False


def is_valid2(a):  # check answer in the end of code
    if a == "д" or a == "н":
        return True
    return False


def script():  # main script
    while True:
        def is_valid(a):  # number check
            if a.isdigit() is True and int(a) <= long:
                return True
            return False

        long = input("В каком диапазоне будем играть? От 1 до...")
        is_valid3(long)
        if is_valid3(long) is True:
            long = int(long)
            random_generator(long)
            break
        else:
            print("Введи число от 2 до ....")
            continue
    secret_number = random_generator(long)
    answer = secret_number - 1
    counter = 0
    while answer != secret_number:
        answer = input("Введите число: ")
        if is_valid(answer) is True:
            counter += 1
            answer = int(answer)
            if answer > secret_number:
                print("Слишком много, попробуйте еще")
            if answer < secret_number:
                print("Слишком мало, попробуйте еще раз")
            if answer == secret_number:
                print("Спасибо, что играли в числовую угадайку.")
                print(f"Количество попыток: {counter}")
                print()
                print("Сиграем еще раз? д- да, н - нет")
                while True:
                    print("Введи только 'д' или 'н'")
                    answer2 = input()
                    if is_valid2(answer2) is True:
                        if answer2 == "д":
                            script()
                        if answer2 == "н":
                            print()
                            print("Удачи)")
                            time.sleep(1)
                            break
        else:
            print(f"А может быть все-таки введем целое число от 1 до {long}?")
        continue


script()
# that's all, nothing to fix and update
