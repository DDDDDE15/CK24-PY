# TODO Найдите количество книг, которое можно разместить на дискете
Vinf=1.44 * 1024 * 1024 #Объем дискеты в байтах
pages = 100 # кол-во страниц в книге
str_ = 50 # кол-во строк на  странице
chars = 25 # кол-во символов в строке
Vsmb = 4 # вес 1 символа в байтах
Books= int(Vinf // (pages * str_ * chars * Vsmb))
print("Количество книг, помещающихся на дискету:",Books)
