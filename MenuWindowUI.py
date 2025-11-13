from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QLabel
from PyQt5.QtGui import QGuiApplication, QIcon
import pygame
pygame.mixer.init()
click_sound7 = pygame.mixer.Sound('intro.wav')
class UI_MenuWindow:
    def __init__(self, sound_enabled = True):
        # Инициализация класса с параметром sound_enabled
        self.sound_enabled = sound_enabled

    def MenuUi(self, MenuWindow):
        # Установка фиксированного размера окна меню
        MenuWindow.setFixedSize(470, 350)
        # Загрузка изображения для фона окна меню
        pixmap = QtGui.QPixmap("rr.png")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        MenuWindow.setPalette(palette)

        # Установка иконки окна меню
        icon = QIcon("grass.png")
        MenuWindow.setWindowIcon(icon)

        # Создание центрального виджета для окна меню
        self.Menucentralwidget = QtWidgets.QWidget()
        MenuWindow.setCentralWidget(self.Menucentralwidget)

        # Создание метки с текстом "Добро пожаловать в 'Цифровой кузнечик'"
        self.label = QtWidgets.QLabel(self.Menucentralwidget)
        self.label.setText("Добро пожаловать в 'Цифровой кузнечик' ")
        self.label.move(10, 15)
        self.label.setFixedSize(470, 40)
        # Установка стиля для метки
        self.label.setStyleSheet("""
                    QLabel {color: white;font-size: 22px;font-family: Comic Sans MS;}
                    """)

        # Создание второй метки с текстом "Музыка"
        self.label2 = QtWidgets.QLabel(self.Menucentralwidget)
        self.label2.move(15,307)
        self.label2.setFixedSize(98, 30)
        # Установка стиля для второй метки
        self.label2.setStyleSheet("""QLabel {background-color: #31FF64; color: white;border-style: solid;border-width: 2px; border-radius: 10px;border-color: white;  text-align: center; font-size: 17px; font-family: Comic Sans MS, sans-serif;}
                                """)

        # Создание кнопки "play_button"
        self.play_button = QtWidgets.QPushButton(self.Menucentralwidget)
        self.play_button.setFixedSize(30, 32)
        # Установка подсказки для кнопки
        self.play_button.setToolTip("Start!")
        # Установка шрифта для кнопки
        self.play_button.setFont(QtGui.QFont('Comic Sans MS', 11, QtGui.QFont.Bold))
        # Подключение функции start_game к событию нажатия на кнопку
        self.play_button.clicked.connect(self.start_game)
        self.play_button.move(120,70)
        # Установка стиля для кнопки
        self.play_button.setStyleSheet("""
                    QPushButton {background-color: #54DDFF; color: white; padding: 20px 42px; text-align: center; font-size: 27px; margin: 4px 2px; min-height: 40px; min-width: 150px; font-family: Comic Sans MS, sans-serif;}
                    QPushButton:hover {background-color: #9FECFE;}
                    """)

        # Создание кнопки "rule_button"
        self.rule_button = QtWidgets.QPushButton(self.Menucentralwidget)
        self.rule_button.setFixedSize(30, 32)
        # Установка подсказки для кнопки
        self.rule_button.setToolTip("Rules")
        # Установка шрифта для кнопки
        self.rule_button.setFont(QtGui.QFont('Comic Sans MS', 11, QtGui.QFont.Bold))
        # Подключение функции show_instructions к событию нажатия на кнопку
        self.rule_button.clicked.connect(self.show_instructions)
        self.rule_button.move(120,190)
        # Установка стиля для кнопки
        self.rule_button.setStyleSheet("""
                    QPushButton {background-color: #54DDFF; color: white; padding: 20px 42px; text-align: center; font-size: 27px; margin: 4px 2px; min-height: 40px; min-width: 150px; font-family: Comic Sans MS, sans-serif;}
                    QPushButton:hover {background-color: #9FECFE;}
                    """)

        # Создание кнопки "exit_button"
        self.exit_button = QtWidgets.QPushButton(self.Menucentralwidget)
        self.exit_button.setFixedSize(91, 30)
        # Подключение функции confirm_exit к событию нажатия на кнопку
        self.exit_button.clicked.connect(self.confirm_exit)
        self.exit_button.move(360,306)
        # Установка стиля для кнопки
        self.exit_button.setStyleSheet("""
                          QPushButton {background-color: transparent; color: white;;border-style: solid;border-width: 2px; border-radius: 10px;border-color: white;   text-align: center; font-size: 17px; font-family: Comic Sans MS, sans-serif;}
                          QPushButton:hover {background-color: #A21C1A;}
                          """)

        # Создание флажка "play_sound_checkbox"
        self.play_sound_checkbox = QtWidgets.QCheckBox(self.Menucentralwidget)
        # Установка начального состояния флажка в соответствии с параметром sound_enabled
        self.play_sound_checkbox.setChecked(self.sound_enabled)
        self.play_sound_checkbox.move(89,314)
        # Подключение функции on_checkbox_state_changed к событию изменения состояния флажка
        self.play_sound_checkbox.stateChanged.connect(self.on_checkbox_state_changed)
        # Подключение функции toggle_sound к событию нажатия на флажок
        self.play_sound_checkbox.clicked.connect(self.toggle_sound)

        # Вызов функции MenutextUI
        self.MenutextUI(MenuWindow)

        # Загрузка и воспроизведение звукового файла
        click_sound3 = pygame.mixer.Sound('start.wav')
        click_sound3.play()
        # Установка громкости звука
        click_sound3.set_volume(0.07)
        click_sound7.play()
        click_sound7.set_volume(0.07)
        click_sound7.play(-1)

    def MenutextUI(self, MenuWindow):
        MenuWindow.setWindowTitle("Меню")
        self.play_button.setText("Играть!")
        self.rule_button.setText("Правила")
        self.exit_button.setText("Выход")
        self.label2.setText("Музыка")

    def toggle_sound(self):
        # Эта функция включает и выключает звук.
        sound_enabled = self.sound_enabled
        # Переключить состояние звука.
        self.sound_enabled = not sound_enabled
        # Обновите интерфейс.
        self.play_sound_checkbox.setChecked(self.sound_enabled)

    def on_checkbox_state_changed(self, state):
        # Функция вызывается при изменении состояния флажка "play_sound_checkbox"
        if state == QtCore.Qt.Checked:
            # Если флажок установлен, установить стиль для метки "label2"
            self.label2.setStyleSheet(
                """QLabel {background-color: #31FF64; color: black;border-style: solid;border-width: 2px; border-radius: 10px;border-color: white;
                  text-align: center; font-size: 17px; font-family: Comic Sans MS, sans-serif;}""")
            click_sound7.play()
            click_sound7.set_volume(0.07)
            click_sound7.play(-1)
        else:
            # Если флажок снят, установить другой стиль для метки "label2"
            self.label2.setStyleSheet(
                """QLabel {background-color: #FF2528; color: white;border-style: solid;border-width: 2px; border-radius: 10px;border-color: white;  text-align: center; font-size: 17px; font-family: Comic Sans MS, sans-serif;}""")
            click_sound7.stop()

    def confirm_exit(self):
        # Загрузка и воспроизведение звуковых файлов
        click_sound = pygame.mixer.Sound('theend.wav')
        click_sound3 = pygame.mixer.Sound('start.wav')

        # Установка громкости звука
        if self.sound_enabled:
            click_sound7.stop()
            click_sound.play()
            click_sound.set_volume(0.07)  # Set the volume to 50%
            click_sound.play(-1)  # Play the sound in a loop until stop()


        # Создание окна сообщения
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Выход")
        icon = QIcon("grass.png")
        msgBox.setWindowIcon(icon)
        msgBox.setInformativeText("        Выйти ... ?"
                                  "\n.")
        # Установка кнопок "Да" и "Нет"
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("Да")
        msgBox.setFont(QtGui.QFont('Comic Sans MS', 11, QtGui.QFont.Bold))
        msgBox.button(QMessageBox.No).setText("Нет")
        # Установка стиля для окна сообщения
        style_sheet = """
            QMessageBox {background-image: url(bye.png);background-color: #FF4038;color: white;font-size: 20px;text-align: right;min-height: 40px; min-width: 150px;}
            QMessageBox QPushButton {background-color: #F0F8FF;color: black;border: none;padding: 5px 10px;min-height: 20px; min-width: 30px;margin: 1px;font-size: 19px;}
            QMessageBox QPushButton:hover {background-color: #FFFFFF;}
        """
        msgBox.setStyleSheet(style_sheet)
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            # Если пользователь нажал "Да", приложение выйдет из цикла обработки событий и завершится
            

            QGuiApplication.instance().quit()
            click_sound.stop()

        if self.sound_enabled:
            click_sound.stop()
            click_sound3.play()
            click_sound3.set_volume(0.07)
            click_sound7.play()
            click_sound7.set_volume(0.07)
            click_sound7.play(-1)
        else:
            click_sound.stop()
            click_sound3.play()
            click_sound3.set_volume(0.07)
            click_sound7.stop()



    def show_instructions(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Инструкции")
        icon = QIcon("grass.png")
        msgBox.setWindowIcon(icon)
        msgBox.setInformativeText(
            "\nЗадача: сделать по одному ходу каждым блоком. Длинна шага - число на блоке."
            "\n\nКак играть в Цифровой кузнечик : Управление: Как играть в Digital Grasshopper: Управление: нажмите на блок и увидите места,"
            " где можно сделать ход, они отмечены крестиком, если для этого блока есть доступные ходы."
            " Начать/перезапустить уровень заново - restart. Рандомизировать уровень - randomize."
            "\n\nПредставляем вам логическую игру 'Цифровой кузнечик'. Задача игры Цифровой кузнечик - Сделать по одному ходу каждой фишкой, длинна хода указана на фишке. Вы можете сделать в нашей онлайн игре только по одному ходу. поэтому необходимо заранее продумывать всю стратегию игры до конца, так как мест очень мало и нужных мест для прыжка может не оказаться. Если вы зашли в тупик, то можете начать уровень сначала, кликнув restart на игровом поле.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        style_sheet = """
            QMessageBox {background-image: url(rules.png);background-size: cover;color: white;font-size: 20px;}
            QMessageBox QLabel { padding: 6px 0px;color: white;}
            QMessageBox QPushButton {background-color: #1E90FF;color: white;border: none;padding: 15px 20px;margin: 5px;font-size: 20px;}
            QMessageBox QPushButton:hover {background-color: #0066CC;}
            """
        label = QLabel()
        label.setText('<br><br><a href="https://vk.com/id689753463">Автор: Маатук Джавхер</a>')

        label.setOpenExternalLinks(True)
        label.move(78,235)
        msgBox.layout().addWidget(label)
        msgBox.setStyleSheet(style_sheet)
        msgBox.exec_()

    def stop_sound7(self):
        click_sound7.stop()


# Когда приложение PyQt5 запущено, оно входит в цикл событий, где оно ожидает и обрабатывает события,
# такие как пользовательский ввод. Когда пользователь нажимает кнопку выхода и подтверждает,
# что хочет выйти из приложения, вызывается метод QGuiApplication.instance().quit(),
# который заставляет приложение выйти из цикла обработки событий. Это означает,
# что приложение перестанет обрабатывать события и завершится, фактически закрыв приложение.n
