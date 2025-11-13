from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from PyQt5.QtGui import QIcon, QGuiApplication
import pygame
from MenuWindowUI import UI_MenuWindow as MenuWindowUI
pygame.mixer.init()

click_sound4 = pygame.mixer.Sound('backsound.wav')
click_sound7 = pygame.mixer.Sound('intro.wav')
click_sound = pygame.mixer.Sound('theend.wav')
click_sound3 = pygame.mixer.Sound('start.wav')

class Ui_MainWindow:
    def __init__(self, sound_enabled=True):
        self.sound_enabled = sound_enabled

    def setupUi(self, MainWindow):
        MenuWindowUI.stop_sound7(MenuWindowUI)
        if self.sound_enabled:
            click_sound7.stop()
            click_sound4.play()
            click_sound4.set_volume(0.03) # Set the volume to 50%
            click_sound4.play(-1)
        else:
            click_sound4.stop()
        # установить минимальную ширину и высоту MainWindow на 30% и 55% от доступного разрешения экрана.
        screen_res = QGuiApplication.primaryScreen().availableGeometry() # вызов из класса QGuiApplication метода primaryScreen и availableGeometry
        width, height = screen_res.width() * 0.3, screen_res.height() * 0.55
        MainWindow.setMinimumSize(width, height)

        # установить максимальную ширину и высоту MainWindow в соответствии с разрешением экрана.
        widthm, heightm = screen_res.width(), screen_res.height()
        MainWindow.setMaximumSize(widthm, heightm)

        pixmap = QtGui.QPixmap("gg.png")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        MainWindow.setPalette(palette)

        icon = QtGui.QIcon("grass.png")
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # создание объекта QGridLayout (сетку) и установка его в центральный виджет с кем мы можем организовать виджеты
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.level_number = QtWidgets.QSpinBox(self.centralwidget)
        self.level_number.setMinimum(1)
        self.level_number.setMaximum(10)
        self.level_number.setFont(QtGui.QFont('Comic Sans MS', 12))
        # установка выравнивания счетчика номера уровня по центру
        self.level_number.setAlignment(QtCore.Qt.AlignCenter)
        self.level_number.setMinimumSize(100, 42)
        self.level_number.setPrefix("Level: ")
        # виджет добавляется в строку 12 и столбец 6 макета и занимает 1 строку и 4 столбца.
        self.gridLayout.addWidget(self.level_number, 12, 6, 1, 4)
        self.level_number.setStyleSheet(
            "QSpinBox { padding: 5px; border-radius: 5px; background-color: #F0F8FF; border: 1px solid #000000;}")

        self.new_game_Button = QtWidgets.QPushButton(self.centralwidget)
        self.new_game_Button.setIcon(QtGui.QIcon("restart.png"))
        self.new_game_Button.setToolTip("Reset")
        self.new_game_Button.setFont(QtGui.QFont('Comic Sans MS', 11, QtGui.QFont.Bold))
        self.new_game_Button.setMinimumSize(70, 42)
        self.new_game_Button.clicked.connect(self.on_restart_clicked)
        self.gridLayout.addWidget(self.new_game_Button, 12, 1, 1, 3)
        self.new_game_Button.setStyleSheet("""
            QPushButton {background-color: #F0F8FF;border-style: solid;border-width: 1px;border-radius: 7px;border-color: black;}
            QPushButton:hover {background-color: #FFFFFF;}
            """)

        self.new_random_Button = QtWidgets.QPushButton(self.centralwidget)
        self.new_random_Button.setMinimumSize(30, 42)
        self.new_random_Button.setIcon(QtGui.QIcon("random.png"))
        self.new_random_Button.setToolTip("Randomize")
        self.new_random_Button.setFont(QtGui.QFont('Comic Sans MS', 11, QtGui.QFont.Bold))
        self.new_random_Button.clicked.connect(self.on_random_clicked)
        self.gridLayout.addWidget(self.new_random_Button, 12, 4, 1, 2)
        self.new_random_Button.setStyleSheet("""
            QPushButton {background-color: #F0F8FF;border-style: solid;border-width: 1px;border-radius: 7px;border-color: black;}
            QPushButton:hover {background-color: #FFFFFF;}
             """)
        # создание объекта QTableView и установка его в центральный виджет
        self.game_field = QtWidgets.QTableView(self.centralwidget)
        # скрытие горизонтального заголовка табличного представления игрового поля
        self.game_field.horizontalHeader().setVisible(False)
        # скрытие вертикального заголовка табличного представления игрового поля
        self.game_field.verticalHeader().setVisible(False)
        # измените размер заголовка (поля), чтобы заполнить все доступное пространство виджета игрового поля по вертикали.
        self.game_field.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # измените размер заголовка (поля), чтобы заполнить все доступное пространство по горизонтали.
        self.game_field.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.gridLayout.addWidget(self.game_field, 1, 1, 1, 9)

        self.exit_button2 = QtWidgets.QPushButton(self.Menucentralwidget)
        self.exit_button2.setText("Выход")
        self.exit_button2.setFixedSize(80, 28)
        self.exit_button2.clicked.connect(self.confirm_exit2)
        self.gridLayout.addWidget(self.exit_button2, 0, 9, 1, 1)
        self.exit_button2.setStyleSheet("""
                                  QPushButton {background-color: #797BAF; color: white;border-style: solid; padding: 12px 1px; text-align: center; font-size: 17px; margin: -7px 1px; font-family: Comic Sans MS, sans-serif;}
                                  QPushButton:hover {background-color: #A21C1A;}
                                  """)

        self.return_button2 = QtWidgets.QPushButton(self.Menucentralwidget)
        self.return_button2.setText("Меню")
        self.return_button2.setFixedSize(80, 28)
        self.return_button2.clicked.connect(self.return_menu)
        self.gridLayout.addWidget(self.return_button2, 0, 1, 1, 1)
        self.return_button2.setStyleSheet("""
                                    QPushButton {background-color: #AFAC69; color: white;border-style: solid; padding: 12px 1px; text-align: center; font-size: 17px; margin: -7px 1px; font-family: Comic Sans MS, sans-serif;}
                                    QPushButton:hover {background-color: #FCB11A;}
                                     """)
        self.textUi(MainWindow)

    def textUi(self, MainWindow):
        MainWindow.setWindowTitle("Цифровой кузнечик")
        self.new_game_Button.setText("Restart")

    # изменить цвет фона кнопки на зеленый
    def on_restart_clicked(self):
        self.new_game_Button.setStyleSheet("border-style: solid; border-width: 1px; border-radius: 7px; border-color: black;background-color: #7FFF00;")
        QtCore.QTimer.singleShot(250, self.reset_button_color) # установить таймер для изменения цвета фона кнопки обратно на белый через 250 мс (0,25 с)

    # снова изменить на белый
    def reset_button_color(self):
        self.new_game_Button.setStyleSheet("""
            QPushButton {background-color: #FFFFFF;border-style: solid;border-width: 1px;border-radius: 7px;border-color: black;}
            QPushButton:hover {background-color: #E8E8E8;}
            """)

    # изменить на коричневый
    def on_random_clicked(self):
        self.new_random_Button.setStyleSheet("border-style: solid; border-width: 1px; border-radius: 7px; border-color: black;background-color: #FF7256;")
        QtCore.QTimer.singleShot(250, self.reset_random_color)

    # снова изменить на белый
    def reset_random_color(self):
        self.new_random_Button.setStyleSheet("""
            QPushButton {background-color: #FFFFFF;border-style: solid;border-width: 1px;border-radius: 7px;border-color: black;}
            QPushButton:hover {background-color: #E8E8E8;}
            """)

    def confirm_exit2(self):

        if self.sound_enabled:
            click_sound4.stop()
            click_sound.play()
            click_sound.set_volume(0.07)  # Set the volume to 50%
            click_sound.play(-1)  # Play the sound in a loop until stop()


        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Выход")
        icon = QIcon("grass.png")
        msgBox.setWindowIcon(icon)
        msgBox.setInformativeText("        Выйти ... ?"
                                  "\n.")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("Да")
        msgBox.setFont(QtGui.QFont('Comic Sans MS', 11, QtGui.QFont.Bold))
        msgBox.button(QMessageBox.No).setText("Нет")
        style_sheet = """
            QMessageBox {background-image: url(bye.png);background-color: #FF4038;color: white;font-size: 20px;text-align: right;min-height: 40px; min-width: 150px;}
            QMessageBox QPushButton {background-color: #F0F8FF;color: black;border: none;padding: 5px 10px;min-height: 20px; min-width: 30px;margin: 1px;font-size: 19px;}
            QMessageBox QPushButton:hover {background-color: #FFFFFF;}
        """
        msgBox.setStyleSheet(style_sheet)
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            QGuiApplication.instance().quit()
            click_sound.stop()

        if self.sound_enabled:
            click_sound.stop()
            click_sound3.play()
            click_sound3.set_volume(0.04)
            click_sound4.play()
            click_sound4.set_volume(0.03)
            click_sound4.play(-1)
        else:
            click_sound.stop()
            click_sound3.play()
            click_sound3.set_volume(0.07)

    def return_menu(self):
        if self.sound_enabled:
            self.MenuUi(self)
            self.play_sound_checkbox.setChecked(self.sound_enabled) # Update the UI.
            self.label2.setStyleSheet(
                """QLabel {background-color: #31FF64; color: black;border-style: solid;border-width: 2px; border-radius: 10px;border-color: white;  text-align: center; font-size: 17px; font-family: Comic Sans MS, sans-serif;}""")
            click_sound4.stop()
        else:
            self.MenuUi(self)
            self.play_sound_checkbox.setChecked(self.sound_enabled) # Update the UI.
            self.label2.setStyleSheet(
                """QLabel {background-color: #FF2528; color: white;border-style: solid;border-width: 2px; border-radius: 10px;border-color: white;  text-align: center; font-size: 17px; font-family: Comic Sans MS, sans-serif;}""")
            MenuWindowUI.stop_sound7(MenuWindowUI)






