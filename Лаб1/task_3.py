list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle= len(list_players) // 2 #Находим середину,чтобы поделить участников

first_team = list_players[:middle]
second_team = list_players[middle:]

print(first_team)
print(second_team)
