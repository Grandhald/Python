# Задача FOOTBALL необязательная

# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех команд.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Пример входа:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Выход будет:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


def add_res_match(dict_res, res_match):
    res = (3, 1, 0)
    list_res = res_match.split(";")
    
    if int(list_res[1]) < int(list_res[3]):
        dict_res[list_res[2]] = dict_res.get(list_res[2], []) + [res[0]]
        dict_res[list_res[0]] = dict_res.get(list_res[0], []) + [res[-1]]
    elif int(list_res[1]) > int(list_res[3]): 
        dict_res[list_res[0]] = dict_res.get(list_res[0], []) + [res[0]]
        dict_res[list_res[2]] = dict_res.get(list_res[2], []) + [res[-1]]
    else:
        dict_res[list_res[0]] = dict_res.get(list_res[0], []) + [res[1]]
        dict_res[list_res[2]] = dict_res.get(list_res[2], []) + [res[1]]

        
def count_results(res_teams):
    res = (3, 1, 0)
    count_points = []
    for key in res_teams:
        amount_game = len(res_teams[key])
        count_win = res_teams[key].count(3)
        count_loss = res_teams[key].count(1)
        count_dead_heat = res_teams[key].count(0)
        sum_points = sum(res_teams[key])
        count_points.append(f"{key}: {amount_game} {count_win} {count_loss} {count_dead_heat} {sum_points}")
    return count_points 


n  = int(input("Введите кол-во матчей: "))

dict_matchs = {}

for _ in range(n):
    add_res_match(dict_matchs, input("Введите результат матча: "))

print()
print("Сводная таблица результатов матчей: ")   
print(*count_results(dict_matchs), sep = "\n")