numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
mis_num= 4 #Индекс пропущенного элемента
numbers[mis_num]=(sum(numbers[:mis_num])+sum(numbers[mis_num+1:]))/(len(numbers))
print("Измененный список:", numbers)
