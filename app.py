import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QTimer
from design import Ui_MainWindow

import classes

class Program(QMainWindow):
    """"""

    hide = False

    def __init__(self):
        """"""

        super(Program, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.status_bar.setValue(0)
        self.ui.btn_start.clicked.connect(self.start_program)

        self.ui.btn_hide_password.clicked.connect(lambda f: self.hide_password(self.hide))

        self.ui.btn_copy.clicked.connect(self.copy_password)

    
    def start_program(self) -> None:
        """"""

        text_1 = "Длина пароля: <len>\nКоличество очков: <score>\nВывод: "
        text_2 = "Количество очков: <score>\nВывод:"
        text_3 = "Энтропия пароля: <score_entropy> бит\nВывод:"

        text_full = "Подробный отчет\nОбщее количество очков: <score>\nЭнтропия пароля: <score_entropy>"

        status = "Результат: "

        password = self.ui.le_password.text()

        if len(password) == 0: 
            return

        test = classes.Checked()

        len_password = len(password)

        test_1 = test.check_length_and_complexity(password=password)
        test_2 = test.check_in_popular_password(password=password)
        score_3 = test.check_entropy(password=password)

        score_1 = test_1[0]
        score_2 = test_2[0]

        score_sum = float(score_1 + score_2) + score_3

        message_1 = ""
        message_2 = f"- {test_2[1]}"
        

        
        for i in test_1[1]:
            message_1 += f"- {i}\n"
            

        print(message_1, message_2)

    
    def hide_password(self, cliked: bool) -> None:
        """"""

        if not cliked:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.btn_hide_password.setText("Скрыть пароль")
            self.hide = True

        else: 
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.btn_hide_password.setText("Показать пароль")
            self.hide = False
    
    def copy_password(self) -> None:
        """"""

        style = "background-color: #32CD32;"
        style_normal = "background-color: #3d3d42;"

        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.le_password.text())
        
        self.ui.btn_copy.setText("✅ Скопировано!")
        self.ui.btn_copy.setStyleSheet(style)
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setText("Скопировать пароль"))
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setStyleSheet(style_normal))




app = QApplication(sys.argv)

window = Program()
window.show()

sys.exit(app.exec())