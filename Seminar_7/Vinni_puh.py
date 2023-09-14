# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def count_vowels(array):
    vowels_in_ACII = "аиыеуюяёо"
    count = 0
    for word in array:
        for letters in word:
            if letters in vowels_in_ACII:
                count += 1
    return count
        

def find_rhythm(message):
    list_phrase = message.lower().split()
    list_syllable = [item.split("-") for item in list_phrase]
    cou_vow_phrase = count_vowels(list_syllable[0])
    for phrase in list_syllable:
        if count_vowels(phrase) != cou_vow_phrase:
            return "Пам парам"
    return "Парам пам-пам"




poem = input("Введите стих для Винни-Пуха: ")

print(find_rhythm(poem))