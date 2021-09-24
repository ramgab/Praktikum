board = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]
stop = 0 #Если стоп будет равна 1, то кто-то выиграл, в противном случае объявится ничья
for i in board: #Вывод поля на экран
   print(" ".join(map(str, i))) 
#Приступаем к ходу и проверяем, выиграл ли кто-то или заполнено ли поле
while stop == 0 or (board[0][0] == '.' and board[0][1] == '.' and board[0][2] == '.' and board[1][0] == '.' and board[1][1] == '.' 
                    and board[1][2] == '.' and board[2][0] == '.' and board[2][1] == '.' and board[2][2] == '.'):
        if stop != 1 and (board[0][0] == '.' or board[0][1] == '.' or board[0][2] == '.' or board[1][0] == '.' or board[1][1] == '.' 
                          or board[1][2] == '.' or board[2][0] == '.' or board[2][1] == '.' or board[2][2] == '.'):
            print("ход крестиков ")
            line = int(input("Введите номер линии: "))
            column = int(input("Введите номер столбца: "))
            while line > 3 or line < 1 or column > 3 or column < 1: #Если выбранная позиция не существует
                print("Введите координаты заново, выбранная позиция не существует")
                line = int(input("Введите номер линии: "))
                column = int(input("Введите номер столбца: "))
            while board[line-1][column-1] != '.': #Если выбранная позиция уже занята, то просим игрока заново ввести координаты
                print("Введите координаты заново, выбранная позиция занята")
                line = int(input("Введите номер линии: "))
                column = int(input("Введите номер столбца: "))
            board[line-1][column-1] = 'x'
            for i in board: #Выводим обновленное поле на экран
                print(" ".join(map(str, i))) 
        else:
            stop = 2 #Чтобы остановить цикл при ничье
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x': #Проверка строк
            print("победили крестики!")
            stop = 1
        elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
            print("победили крестики!") 
            stop = 1
        elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
            print("победили крестики!") 
            stop = 1
        if board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x': #Проверка столбцов
            print("победили крестики!")
            stop = 1
        elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
            print("победили крестики!")
            stop = 1
        elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
            print("победили крестики!")
            stop = 1
        if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x': #Проверка диагоналей
            print("победили крестики!")
            stop = 1
        elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            print("победили крестики!")
            stop = 1
        
        
        if stop != 1 and (board[0][0] == '.' or board[0][1] == '.' or board[0][2] == '.' or board[1][0] == '.' or board[1][1] == '.' 
                          or board[1][2] == '.' or board[2][0] == '.' or board[2][1] == '.' or board[2][2] == '.'): #Для того, чтобы после победы крестиков не просили ходить нолики
            print("ход ноликов ")
            line = int(input("Введите номер линии: "))
            column = int(input("Введите номер столбца: "))
            while line > 3 or line < 1 or column > 3 or column < 1: #Если выбранная позиция не существует
                print("Введите координаты заново, выбранная позиция не существует")
                line = int(input("Введите номер линии: "))
                column = int(input("Введите номер столбца: "))
            while board[line-1][column-1] != '.': #Если выбранная позиция уже занята, то просим игрока заново ввести координаты; либо если на поле нет больше мест
                print("Введите координаты заново, выбранная позиция занята")
                line = int(input("Введите номер линии: "))
                column = int(input("Введите номер столбца: "))
            board[line-1][column-1] = 'o'
            for i in board: #Выводим обновленное поле на экран
                print(" ".join(map(str, i))) 
        else:
            if stop != 1: #Для того, чтобы если уже после победы не было ничьи
                stop = 2 #Чтобы остановить цикл при ничье
        if board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o': #Проверка строк
            print("победили нолики!")
            stop = 1
        elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
            print("победили нолики!")
            stop = 1
        elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
            print("победили нолики!")
            stop = 1
        if board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o': #Проверка столбцов
            print("победили нолики!")
            stop = 1
        elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
            print("победили нолики!")
            stop = 1
        elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
            print("победили нолики!")
            stop = 1
        if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o': #Проверка диагоналей
            print("победили нолики!")
            stop = 1
        elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
            print("победили нолики!")
            stop = 1


if stop == 2:
    print("Ничья")