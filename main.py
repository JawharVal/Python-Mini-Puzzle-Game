import sys # для взаимодействия с системой
from MainWindow import MainWindow # для создания главного окна
from PyQt5.QtWidgets import QApplication # для создания приложения

# Определение главной функции
def main():
    # Создание нового объекта QApplication, QApplication is a subclass of QGuiApplication, which in turn is a subclass of QCoreApplication
    app = QApplication(sys.argv)
    # Создание нового объекта MainWindow
    mw = MainWindow()
    # запустить и показ mw
    mw.show()
    # Запуск цикла обработки событий приложения, приложение завершит работу чисто
    sys.exit(app.exec_())

# Запуск главной функции
if __name__ == '__main__':
    main()














# import sys импортирует модуль sys, который обеспечивает доступ к некоторым переменным, используемым или поддерживаемым интерпретатором, а также к функциям, тесно взаимодействующим с интерпретатором.
# import traceback импортирует модуль traceback, который предоставляет стандартный интерфейс для извлечения, форматирования и печати трассировки стека программ Python.
# from MainWindow import MainWindow импортирует класс MainWindow из модуля MainWindow.
# from PyQt5.QtWidgets import QApplication, QMessageBox импортирует классы QApplication и QMessageBox из модуля PyQt5.QtWidgets.
# import sys importiruyet modul' sys, kotoryy obespechivayet dostup k nekotorym

# import sys imports the sys module which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
# import traceback imports the traceback module which provides a standard interface to extract, format and print stack traces of Python programs.
# from MainWindow import MainWindow imports the MainWindow class from the MainWindow module.
# from PyQt5.QtWidgets import QApplication, QMessageBox imports the QApplication and QMessageBox classes from the PyQt5.QtWidgets module.

# Оператор if __name__ == '__main__': обычно используется в скриптах Python, чтобы гарантировать, что определенный..
# ..код выполняется только при непосредственном запуске скрипта, а не когда он импортируется как модуль в другой скрипт.

# The if __name__ == '__main__': statement is commonly used in Python scripts to ensure that certain code is only executed when the script is run directly, and not when it is imported as a module into another script.
