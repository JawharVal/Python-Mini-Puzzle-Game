import copy # Мы будем использовать для копирования и заполнения игровое поле (GameField) пустыми ячейками из GameCell
import pygame # для импорта mixer для звуковых эффектов
from enum import Enum # создать константу для состояния игры
from PyQt5.QtWidgets import QMessageBox # сообщение об окончании игры
from PyQt5.QtGui import QIcon

pygame.mixer.init() # инициализирует модуль mixer, который используется для обработки звука в Pygame.

class GameCell: # используется для создания пустой ячейки.
    def __init__(self, block: bool = False, number: int = 0, step: bool = False, is_locked=False, is_active=False):
        self._block = block  # узнать blocked ячейка или нет
        self._number = number  # число в ячейке
        self._step = step  # был ли сделан шаг в этой ячейке или нет
        self._is_locked = is_locked  # узнать locked ячейка или нет
        self._is_active = is_active  # узнать active ячейка или нет

    # Декоратор, позволяет превращать атрибуты класса в свойства или управляемые атрибуты.
    # @property — это декоратор в Python, который позволяет превратить метод в атрибут, доступный только для чтения.
    # Это питонический способ использования геттеров и сеттеров в объектно-ориентированном программировании .
    # Это означает, что мы можем получить доступ к методу как к атрибуту, не вызывая его как функцию.
    # Например, мы можем получить доступ к атрибуту блока объекта GameCell, вызвав my_game_cell.block вместо my_game_cell.block().
    # атрибут хранит данные, пока функция (или метод) выполняет действие.


    @property
    def block(self) -> bool:
        return self._block

    @property
    def number(self) -> int:
        return self._number

    @property
    def step(self) -> bool:
        return self._step

    @property
    def is_locked(self) -> bool:
        return self._is_locked

    @property
    def is_active(self) -> bool:
        return self._is_active

# читаем многомерный массив целых чисел из файла
def read_int_multy_array_form_file(level_number: int):
    path = "resources/levels/level " + str(level_number) # задаем путь к файлу по номеру уровня
    with open(path) as file: # открывает файл по указанному пути
        lst = file.readlines() # читает все строки из файла в список
    return [[int(n) for n in x.split()] for x in lst] # возвращает список списков, где каждый внутренний список представляет строку целых чисел из файла


class GameState(Enum): # enum — это набор именованных значений, представляющих набор констант.
    PLAYING = 1
    WIN = 2


class Game:
    def __init__(self, start_level: int):
        self._state = None  # текущее состояние игры
        self._row_count = 0  # количество строк в игровом поле (game field)
        self._col_count = 0  # количество столбцов в игровом поле
        self._field = []  # игровое поле, представленное в виде списка списков
        self._current_level = start_level  # текущий уровень игры
        self.new_game()  # запускает новую игру
        self._current_cell = None  # текущая выбранная ячейка
        self._current_cell_row = None  # индекс строки текущей выбранной ячейки
        self._current_cell_col = None  # индекс столбца текущей выбранной ячейки
        self._steps = []  # список шагов, пройденных в этой игре

    def new_game(self) -> None:
        self.init_game_field() # инициализирует новое игровое поле на основе данных текущего уровня
        self._state = GameState.PLAYING # устанавливает состояние PLAYING

    @property
    def row_count(self) -> int:
        return self._row_count

    @property
    def col_count(self) -> int:
        return self._col_count

    @property
    def field(self) -> list:
        return self._field

    @property
    def state(self) -> GameState:
        return self._state

    # инициализируем новое игровое поле на основе данных текущего уровня
    def init_game_field(self):
        level = read_int_multy_array_form_file(self._current_level)  # считывает данные уровня из файла
        self._col_count = len(level[0])  # Устанавливает количество столбцов на основе данных уровня. Получив длину этой первой строки, мы можем определить, сколько столбцов есть в 2D-массиве или матрице, представленной уровнем.
        self._row_count = len(level)  # устанавливает количество строк на основе данных уровня

        # Создаем двумерный список. Каждый элемент списка инициализируется как глубокая deep копия списка, содержащего объекты GameCell().
        self._field = [copy.deepcopy([GameCell() for c in range(self.col_count)]) for r in range(self.row_count) ]

        for row in range(len(level)):
            for column in range(len(level[0])):
                cell = level[row][column]  # получить значение ячейки из данных уровня
                if cell == 1:
                    self._field[row][column] = GameCell(block=True, number=1)  # создает заблокированную ячейку с номером 1
                if cell == 2:
                    self._field[row][column] = GameCell(block=True, number=2)  # создает заблокированную ячейку с номером 2
                if cell == 3:
                    self._field[row][column] = GameCell(block=True, number=3)  # создает заблокированную ячейку с номером 3
                if cell == 4:
                    self._field[row][column] = GameCell(block=True, number=4)  # создает заблокированную ячейку с номером 4

    # находим все возможные шаги из текущей ячейки
    def find_steps(self, row, column):
        if self._current_cell is None or not self._current_cell.block or self._current_cell.step:
            return None
        else:
            step = self._current_cell.number  # получает количество шагов, которые можно сделать из текущей ячейки
            self.check_neighbor(row - step, column)  # проверяет, можно ли сделать шаг на север
            self.check_neighbor(row + step, column)  # проверяет, можно ли сделать шаг на юг
            self.check_neighbor(row, column - step)  # проверяет, можно ли сделать шаг на запад
            self.check_neighbor(row, column + step)  # проверяет, можно ли сделать шаг на восток
            self.check_neighbor(row - step,column + step)  # проверяет, можно ли сделать шаг по диагонали на северо-восток
            self.check_neighbor(row + step, column + step)  # проверяет, можно ли сделать диагональный шаг на юго-восток
            self.check_neighbor(row - step,column - step)  # проверяет, можно ли сделать шаг по диагонали на северо-запад
            self.check_neighbor(row + step, column - step)  # проверяет, можно ли сделать шаг по диагонали на юго-запад

    # проверяем, можно ли сделать шаг в указанную ячейку
    def check_neighbor(self, row, column):
        # возвращает, если указанная ячейка выходит за пределы
        if row < 0 or row >= len(self._field) or column < 0 or column >= len(self.field[row]):
            return None
        # исключения, не за границы, ни блок, ни уже сделанный шаг, то возможный шаг
        elif not self._field[row][column].block and not self._field[row][column].step:
            self._field[row][column]._step = True
            self._steps.append([row, column]) # добавляет указанную ячейку в список шагов

    # меняем текущую ячейку на указанную ячейку
    def swap_cells(self, row, col):
        self._field[row][col] = self._current_cell  # перемещает текущую ячейку в указанное место
        self._field[row][col]._is_locked = True  # lock текущую ячейку
        self._field[row][col]._is_active = False  # деактивирует текущую ячейку
        self._field[self._current_cell_row][self._current_cell_col] = GameCell()  # заменяет старое местоположение текущей ячейки пустой ячейкой

        # на указанную ячейку уже наступали, поэтому метод удаляем ее из списка шагов с помощью метода remove()
        for cell in self._steps:
            if cell[0] == row and cell[1] == col:
                self._steps.remove(cell)

        # проверяем, все ли "block" были перемещены
        all_pieces_moved = True
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.field[row][col].block and not self.field[row][col].is_locked:
                    all_pieces_moved = False # устанавливает для all_pieces_moved значение False, если найден "block", который не заблокирован

        # Если все блоки были перемещены, показать сообщение
        if all_pieces_moved:
            self._state = GameState.WIN  # устанавливает состояние игры в WIN
            click_sound4 = pygame.mixer.Sound('cong.wav')
            click_sound4.play()
            click_sound4.set_volume(0.07)
            msg_box = QMessageBox()
            msg_box.setWindowTitle("END GAME")
            msg_box.setText("Поздравляю!!\n\n Уровень пройден.""Пробуйте другие уровни.")
            icon = QIcon("grass.png")
            msg_box.setWindowIcon(icon)
            style_sheet = """
                QMessageBox {background-image: url(win.png);background-color: #05D800;background-size: cover;font-size: 20px; font-family: Comic Sans MS, sans-serif;}
                QMessageBox QLabel { padding: 1px 0px;color: white;}
                QMessageBox QPushButton {background-color: #71C671;color: white;border: none;padding: 15px 20px;margin: 5px;font-size: 20px;}
                QMessageBox QPushButton:hover {background-color: #7CCD7C;}
                """
            msg_box.setStyleSheet(style_sheet)
            msg_box.exec_()

    # очищаем все шаги с игрового поля
    def clear_steps(self):
        for cell in self._steps:
            self._field[cell[0]][cell[1]] = GameCell()  # заменяет каждый шаг пустой ячейкой
        self._steps.clear()  # эффективно очищает историю шагов, предпринятых в игре.

    # этот метод вызывается при клике по блоку на игровом поле
    def on_button_click(self, row: int, col: int):
        click_sound = pygame.mixer.Sound('click.wav') # загружает звуковой файл для щелчка по блоку
        click_sound2 = pygame.mixer.Sound('click2.wav')  # загружает звуковой файл для клика по шагу

        if self.state != GameState.PLAYING:
            return # возвращает None, если состояние игры не PLAYING

        # Если щелкнуть не locked блок
        if self._field[row][col].block and not self._field[row][col].is_locked:
            if self._current_cell is not None:
                self._current_cell._is_active = False  # деактивирует последнюю текущую ячейку, по которой щелкнули
            self._current_cell = self._field[row][col] # устанавливает текущую ячейку в блок, на который нажали
            self._current_cell._is_active = True  # активирует текущую ячейку
            self.clear_steps()  # удалить шаги последнего текущего блока после нажатия на другой блок
            self._current_cell_row = row
            self._current_cell_col = col
            self.find_steps(row, col)  # находит все возможные шаги из текущей ячейки
            click_sound.play() # воспроизводит звук щелчка по блоку
            click_sound.set_volume(0.07)

        # Проверяем, нажат ли шаг
        if self._field[row][col].step: #True
            # Если шаг нажат
            self.swap_cells(row, col)  # меняет местами текущую ячейку с указанной ячейкой
            self.clear_steps()  # очищает все шаги с игрового поля после совершения хода
            click_sound2.play() # воспроизводит звук клика по шагу
            click_sound2.set_volume(0.07)