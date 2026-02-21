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
        self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.btn_hide_password.clicked.connect(lambda f: self.hide_password(self.hide))

        self.ui.btn_copy.clicked.connect(self.copy_password)

    
    def start_program(self) -> None:
        """"""

        text_1 = "Длина пароля: <len>\nКоличество очков: <score>\nВывод:"
        text_2 = "Количество очков: <score>\nВывод:\n"
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

        score_sum = score_1 + score_2

        message_1 = ""
        message_2 = "- "
        
        count = 0
        for i in (str(test_2[1][0]).split(" ")):
            
            if count >= 5:
                message_2 += f"\n{i} "
                count = 1
                continue


            message_2 += f"{i} "
            count += 1

        
        for i in test_1[1]:
            message_1 += f"- {i}\n"

        status_text = ""
        percent = 0
        color = ""

        if score_sum <= -100:
            status_text = "Ужасный пароль"
            percent = 5
            color = "#FF0000"

        elif score_sum <= 0:
            status_text = "Очень плохой пароль"
            percent = 10
            color = "#FF3333"
        
        elif score_sum <= 15:
            status_text = "Плохой пароль"
            percent = 20
            color = "#FF8000"
        
        elif score_sum <= 30:
            status_text = "Нормальный пароль"
            percent = 30
            color = "#FFFF00"
        
        elif score_sum <= 50:
            status_text = "Хороший пароль"
            percent = 50
            color = "#FFFF66"
        
        elif score_sum <= 75:
            status_text = "Отличный пароль"
            percent = 75
            color = "#00FF80"
        
        elif score_sum < 95:
            status_text = "Превосходный пароль"
            percent = 95
            color = "#80FF00"
        
        elif score_sum == 95:
            status_text = "Самый защищеный пароль"
            percent = 100
            color = "#00FF00"
        
        else: 
            status_text = "Ошибка"
            percent = 0
            color = "#FFFFFF"


        
        text = status + status_text

        style_status = f"""
            QProgressBar::chunk {{
                background-color: {color};
            }}
        """

        
        text_first = f"{(text_1.replace("<len>", str(len_password))).replace("<score>", str(score_1))} {message_1}"
        text_second = f"{(text_2.replace("<score>", str(score_2)))} {message_2}"
        text_third = f"{text_3.replace("<score_entropy>", str(score_3))}"

        text_main = f"{(text_full.replace("<score>", str(score_sum))).replace("<score_entropy>", str(score_3))}"

        self.ui.lbl_result.setText(text)
        self.ui.status_bar.setValue(percent)
        self.ui.status_bar.setStyleSheet(style_status)
        self.ui.lbl_full_result.setText(text_main)
        self.ui.lbl_first_text.setText(text_first)
        self.ui.lbl_second_text.setText(text_second)
        self.ui.lbl_third_text.setText(text_third)


    
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