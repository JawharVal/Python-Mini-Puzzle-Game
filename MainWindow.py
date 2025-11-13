import os
import random
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg  # Модуль QtSvg для работы с масштабируемой векторной графикой (SVG).
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem # создание основных окон приложения, настройка отображения элементов и редактирование в виде, предоставление вариантов стилей для элементов в виде.
from PyQt5.QtGui import QMouseEvent, QPainter, QStandardItemModel # для обработки событий мыши и элементов рисования
from PyQt5.QtCore import QModelIndex, QRectF, Qt # для работы с моделями и геометрическими фигурами
from MainWindowUI import Ui_MainWindow as MainWindowUI
from MenuWindowUI import UI_MenuWindow as MenuWindowUI
from Game import Game

pygame.mixer.init()
click_sound = pygame.mixer.Sound('restart.wav')
click_sound3 = pygame.mixer.Sound('start.wav')

class MainWindow(QMainWindow, MainWindowUI, MenuWindowUI):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.MenuUi(self)# устанавливает MenuiUI окна меню из MenuWindowUI
        self.prev_num = None  # Инициализировать числовую переменную как None, чтобы использовать ее для случайного уровня

    def start_game(self):
        self.setupUi(self) # устанавливает setupUI окна меню из MenuWindowUI (self twali 3andha access le les methodes ta3 classes eli mawjoudin fel mainwindow)

        images_dir = os.path.join(os.path.dirname(__file__), 'resources/images') # получить путь к папке с изображением

        # перебираем каждый файл в каталоге images_dir и создаем пару ключ-значение для каждого файла,
        # где ключ — это имя файла без расширения, а значение — объект средства визуализации SVG, созданный из файла SVG.
        # Результирующий словарь присваивается атрибуту _images объекта self. (использовать только название части изображения)
        self._images = {
            os.path.splitext(f)[0]:  # Использовать имя файла без расширения в качестве ключа
                QtSvg.QSvgRenderer(os.path.join(images_dir, f)) # Создать объект рендерера SVG из файла SVG
            for f in os.listdir(images_dir)  # Перебираем каждый файл в каталоге
        }

        i = random.randint(1,10)
        self.level_number.setValue(i)  # установка начального значения для счетчика level_number
        self.game = Game(i)  # начать новую игру со случайным уровнем
        self.grid_display(self.game) # отображать игровое поле сетки sna3na el grid fere8 bel method heki

        # делегат отвечает за рендеринг и редактирование элементов в представлении (отрисовка) (tedhen el ar9am  fi el grid) (nested class)
        class MyDelegate(QItemDelegate):
            def __init__(self, parent=None):
                super().__init__(parent)

            # Аргумент painter - это объект QPainter, который используется для рисования элемента,
            # Аргумент option - содержит различные параметры стиля, которые можно использовать для настройки рисунка.
            # Аргумент idx - это индекс модели окрашиваемого элемента.
            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                self.parent().on_item_paint(idx, painter, option)  # вызывает on_item_paint из класса MainWindow

        delegate = MyDelegate(self)
        self.game_field.setItemDelegate(delegate)  # устанавливает делегат элемента для игрового поля (применяет рисование)
        self.new_game_Button.clicked.connect(self.new_game)  # соединяет функцию new_game с событием нажатия кнопки new_game_Button для запуска/перезапуска уровня
        self.new_random_Button.clicked.connect(self.random_game)  # соединяет функцию new_game с событием нажатия кнопки new_random_Button для случайного уровня
        click_sound3.play() # воспроизводит стартовый звук
        click_sound3.set_volume(0.03)

        # Этот метод вызывается при нажатии мыши на игровое поле
        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.game_field.indexAt(e.pos())  # определить индекс элемента в позиции мыши
            self.on_item_clicked(idx, e)  # вызывает функцию on_item_clicked с индексом и событием

        self.game_field.mousePressEvent = new_mouse_press_event  # устанавливает функцию mousePressEvent для игрового поля QtableView

    # Этот метод отображает модель сетки в game_field QTableView # tesna3 el grid fere8
    def grid_display(self, game: Game) -> None:
        model = QStandardItemModel(game.row_count, game.col_count) # создает новую модель сетки с указанным количеством строк и столбцов
        self.game_field.setModel(model)  # устанавливает модель игрового поля для отображения данных в виджете game_field
        self.update_view()  # обновляет вид

    # Этот метод запускает/перезапускает новую игру с указанным номером уровня
    def new_game(self):
        self.game = Game(self.level_number.value())  # creates a new Game object with specified level number
        self.update_view()  # updates view
        click_sound.play()
        click_sound.set_volume(0.05)

    # Этот метод запускает новую игру со случайным номером уровня
    def random_game(self):
        i = random.randint(1, 10)  # Создать новое случайное число от 1 до 10
        while i == self.prev_num:  # Продолжайте генерировать новые числа, пока они не будут отличаться от предыдущего числа
            i = random.randint(1, 10)
        self.prev_num = i  # Установить предыдущий номер как текущий новый номер
        self.level_number.setValue(i)
        self.game = Game(i) # создает новый объект Game с указанным номером уровня
        self.update_view() # обновляет вид
        click_sound.play()
        click_sound.set_volume(0.05)

    # Этот метод обновляет/перерисовывает вид игрового поля
    def update_view(self):
        self.game_field.viewport().update()

    # Этот метод вызывается, когда элемент в игровом поле нужно покрасить(paint)
    def on_item_paint(self, e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem) -> None:
        cell = self.game.field[e.row()][e.column()]  # получает ячейку по указанному индексу
        img = self._images['default']  # устанавливает изображение по умолчанию для GameCell
        if cell.block:
            # Если ячейка представляет собой блок
            name = ""
            if cell.is_active:
                name = name + "active "  # добавляет "active" к имени изображения, если блок активен
            if cell.is_locked:
                name = name + "locked "  # добавляет "locked" к имени изображения, если блок заблокирован

            if cell.number == 1:
                name = name + "1"  # добавляет номер к имени изображения, если у блока есть номер
            if cell.number == 2:
                name = name + "2"
            if cell.number == 3:
                name = name + "3"
            if cell.number == 4:
                name = name + "4"
            img = self._images[name]  # устанавливает изображение для блока
        if cell.step:
            img = self._images['step']  # устанавливает изображение для шага

        img.render(painter, QRectF(option.rect))  # визуализирует изображение в указанном прямоугольнике, который указывает область рисовальщика, которая будет отрисовываться с изображением

    # Этот метод вызывается при щелчке элемента в игровом поле
    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton or me.button() == Qt.RightButton: # Если была нажата левая или правая кнопка мыши
            self.game.on_button_click(e.row(), e.column())  # вызывает функцию on_button_click Game объекта
        self.update_view()  # updates view

