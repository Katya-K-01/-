def get_all_diagonals(matrix):  # функция взята у deepseek, находит все диагонали
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])

    # Главные диагонали (сверху-слева направо-вниз)
    diagonals = []

    # Диагонали, начинающиеся в первом столбце
    for i in range(rows):
        diagonal = []
        j = 0
        while i < rows and j < cols:
            diagonal.append(matrix[i][j])
            i += 1
            j += 1
        diagonals.append(diagonal)

    # Диагонали, начинающиеся в первой строке (кроме уже учтенной [0][0])
    for j in range(1, cols):
        diagonal = []
        i = 0
        while i < rows and j < cols:
            diagonal.append(matrix[i][j])
            i += 1
            j += 1
        diagonals.append(diagonal)

    # Побочные диагонали (сверху-справа налево-вниз)
    # Диагонали, начинающиеся в последнем столбце
    for i in range(rows):
        diagonal = []
        j = cols - 1
        while i < rows and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        diagonals.append(diagonal)

    # Диагонали, начинающиеся в первой строке (кроме уже учтенной [0][cols-1])
    for j in range(cols - 2, -1, -1):
        diagonal = []
        i = 0
        while i < rows and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        diagonals.append(diagonal)

    return diagonals


class Fourinarow():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.playfield = [[0 for _ in range(width)] for _ in range(height)]

    def printdesk(self):
        for i in self.playfield:
            print(i)

    def check(self):
        x = 1 #счетчик 1 игрока
        y = 1 # счетчик 2 игрока
        for i in range(self.height): # горизонтальная проверка
            for j in range(self.width-1):
                if self.playfield[i][j] == 1 and self.playfield[i][j+1] == 1:
                    x += 1
                else:
                    if x >= 4:
                        return 1
                    x = 1
                if self.playfield[i][j] == 2 and self.playfield[i][j+1] == 2:
                    y += 1
                else:
                    if y >= 4:
                        return 2
                    y = 1
        if x >= 4:
            return 1
        elif y >= 4:
            return 2
        x = 1
        y = 1
        for i in range(self.width): # Вертикальная проверка
            for j in range(self.height-1):
                print(j, i)
                if self.playfield[j][i] == 1 and self.playfield[j+1][i] == 1:
                    x += 1
                else:
                    if x >= 4:
                        return 1
                    x = 1
                if self.playfield[j][i] == 2 and self.playfield[j+1][i] == 2:
                    y += 1

                else:
                    if y >= 4:
                        return 2
                    y = 1
        if x >= 4:
            return 1
        elif y >= 4:
            return 2
        zero = 0 # наличие ходов
        for i in self.playfield:
            zero += i.count(0)
        if zero == 0:
            return 3
        diag = get_all_diagonals(self.playfield) # проверка дигоналей
        for i in diag:
            if len(i) >= 4 and set(i) == {1}:
                return 1
            if len(i) >= 4 and set(i) == {2}:
                return 2
        return 0

    def motion(self, player, number): #player - номер игрока, number - номер столбца
        if number-1 >= self.width:
            return 0
        for i in range(self.height-1, -1, -1):
            if self.playfield[i][number-1] == 0:
                self.playfield[i][number-1] = player
                return 1
        return 0


a = int(input('Введите ширину (больше 3)'))
b = int(input('Введите высоту (больше 3)'))
while a < 4:
    a = int(input('Введите ширину (больше 3)'))
while b < 4:
    b = int(input('Введите ширину (больше 3)'))

desk = Fourinarow(a, b)
desk.printdesk()
desk.turn(1, 1)
end = 1
player_m = 1
while end:
    if desk.motion(player_m, int(input(f'Игрок {player_m}, введите номер столбца (от 1 до {desk.width})\n'))):
        if desk.check() == 3:
            print('Ничья')
            end = 0
        elif desk.check() != 0:
            print(f'Игра завершена. Победил игрок {desk.check()}')
            end = 0
        if player_m == 2:
            player_m = 1
        else:
            player_m = 2
        desk.printdesk()

