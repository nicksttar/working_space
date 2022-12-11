import random
import sys


print("------Hi guys it's new code names: guess the word------")
print("Description: Imagine that you are pirate and you go to gallows you can alive if you guess the word lets go...")
words_easy = ["Амеба", "Апельсин", "Автобус", "Абобус", "Банан", "Букашка", "Булка", "Вулкан", "Вор", "Великан", "Гнездо", "Гуев-легенда", "Гадалка", "Днепр", "Декабрь", "Двадцать"]
words_medium = ["Железо", "Женева", "Желплощадь", "Индия", "Интерес", "Интерн", "Какрнавал", "Калыван", "Курага", "Ланшфт", "Лимбо", "Листва"]
secret_word = words_easy[11]


words_hard = ['Династия', 'Истомить', 'Клык', 'Латник', 'Очерствелый', 'Разобидеться', 'Агропромышленный', 'Каракули',
         'Попечение', 'Провал', 'Прямизна', 'Пуховик', 'Сдержанный', 'Сухомятка', 'Тотальный', 'Эсер', 'Заторможенный',
         'Исполнительный', 'Клохтать', 'Отменный', 'Прекратиться', 'Размежевать', 'Сварганить', 'Серповидный', 'Хны',
         'Чеканка', 'Всяк', 'Зайчатина', 'Законсервировать', 'Кланяться', 'Продналог', 'Силлабический', 'Стасовать',
         'Столешница', 'Уровень', 'Чернотал']


def get_word():  # Рандомное слово
    return random.choice(words_hard)


def display_human(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def another_game(n):
   if n == "Y":
      play_script()
   elif n == "N":
      sys.exit
   else:
      print("Введите Y - yes, N - no")
      play = input("Играем еще? ")
      another_game(play)



def play_script():
   print("Выберите уровень сложности 1-3 (1-простой, 3-самый сложный")
   uswer_words = []
   tries = 6
   new_word = get_word()
   new_word2 = new_word.lower()
   shipher_word = list(len(new_word) * "_")
   print(*shipher_word)
   while tries != 0:
      answer = input("Введите букву: ")
      if answer.lower() not in new_word2:
         tries -= 1
         print(display_human(tries))
         print("Веревка все ближе...")
         print("Осталось попыток: ", tries)
      if answer in uswer_words or shipher_word.count("_") == 0:
         print("Эта буква ужи была...")
      if answer == new_word:
         print("Победа")
         play = input("Играем еще? ")
         another_game(play)
      else:
         for i in range(len(new_word)):
            if new_word[i] == answer.lower():
               shipher_word[i] = str(answer.lower())
               uswer_words.append(answer)
            if new_word[i] == answer.upper():
               shipher_word[i] = str(answer.upper())
               uswer_words.append(answer)
         print(*shipher_word)
   play = input("Играем еще? ")
   another_game(play)


play_script()

# add dificult>
# add stupid detector<
# add category>а