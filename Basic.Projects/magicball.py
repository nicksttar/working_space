import random
import sys
import time

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется '
                                                                                                         '- да',
           'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно', 'Попробуй снова',
           'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
           'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
           'Весьма сомнительно']


def is_valid_words(a):
    if a.isalpha() is True:
        return True
    return False


def is_valid_question(a):
    if a.isdigit() is True:
        return False
    return True


def is_valid_answer(a):
    if a == "д" or a == "н":
        return True
    return False


print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
while True:
    name = input("Как тебя зовут? ")
    if is_valid_words(name) is True:
        print(f"{name}, я знал что тебя так зовут...")
        break
    else:
        print("Введите имя...")
        continue


def script():
    while True:
        while True:
            question = input("Задай мне свой вопрос: ")
            answer = answers[random.randint(0, len(answers) - 1)]
            if is_valid_question(question) is True:
                time.sleep(0.5)
                print("Дай подумать...")
                time.sleep(0.5)
                print("Налаживаю связь с космосом...")
                time.sleep(0.5)
                print("Почти готово...")
                time.sleep(0.5)
                print(f"Ответ на твой вопрос: {answer}")
                while True:
                    question2 = input("Задать еще вопрос? (д - да, н - нет): ")
                    if is_valid_answer(question2) is True:
                        if question2 == "д":
                            script()
                        if question2 == "н":
                            print("See you next time...")
                            time.sleep(1)
                            sys.exit()
                    else:
                        print("Введите д или н")
                        continue
            else:
                print("Введите вопрос без знаков и цифр...")
                continue


script()
# that's all, nothing to fix and update
# fixed len 
#sfsd 
print("LOL")