from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import config_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 900)
        MainWindow.setMinimumSize(QSize(750, 900))
        MainWindow.setMaximumSize(QSize(1500, 1800))
        icon = QIcon()
        icon.addFile(u":/icon/config/app/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #3C3C43;\n"
"    font-size: 11pt;\n"
"    color: white;\n"
"    font-family: Inter;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: #61afef;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3d3d42;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #545457;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #6d6d75;\n"
"}\n"
"\n"
"QProgressBar {\n"
"	border: 2px solid #555555;\n"
"    border-radius: 5px;\n"
"    background-color: #3c3c3c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 600))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spacer1 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer1)

        self.lbl_main_name = QLabel(self.centralwidget)
        self.lbl_main_name.setObjectName(u"lbl_main_name")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(20)
        font.setBold(True)
        self.lbl_main_name.setFont(font)
        self.lbl_main_name.setStyleSheet(u"font-size: 20pt;")
        self.lbl_main_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_main_name)

        self.spacer2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer2)

        self.layou_input_button = QHBoxLayout()
        self.layou_input_button.setObjectName(u"layou_input_button")
        self.spacer1_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layou_input_button.addItem(self.spacer1_2)

        self.le_password = QLineEdit(self.centralwidget)
        self.le_password.setObjectName(u"le_password")

        self.layou_input_button.addWidget(self.le_password)

        self.spacer3_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layou_input_button.addItem(self.spacer3_2)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layou_input_button.addWidget(self.btn_start)

        self.spacer2_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layou_input_button.addItem(self.spacer2_2)


        self.verticalLayout_2.addLayout(self.layou_input_button)

        self.spacer3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer3)

        self.layout_status_bar = QHBoxLayout()
        self.layout_status_bar.setObjectName(u"layout_status_bar")
        self.spacer2_4 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout_status_bar.addItem(self.spacer2_4)

        self.status_bar = QProgressBar(self.centralwidget)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setValue(0)
        self.status_bar.setTextVisible(False)

        self.layout_status_bar.addWidget(self.status_bar)

        self.spacer1_4 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout_status_bar.addItem(self.spacer1_4)


        self.verticalLayout_2.addLayout(self.layout_status_bar)

        self.spacer4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer4)

        self.lbl_result = QLabel(self.centralwidget)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setStyleSheet(u"font-size: 16pt;")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_result)

        self.spacer5 = QSpacerItem(20, 85, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer5)

        self.lbl_full_result = QLabel(self.centralwidget)
        self.lbl_full_result.setObjectName(u"lbl_full_result")
        self.lbl_full_result.setStyleSheet(u"font-size: 16pt;")
        self.lbl_full_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_full_result)

        self.spacer6 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer6)

        self.layout_full_text = QGridLayout()
        self.layout_full_text.setObjectName(u"layout_full_text")
        self.lbl_first_text = QLabel(self.centralwidget)
        self.lbl_first_text.setObjectName(u"lbl_first_text")

        self.layout_full_text.addWidget(self.lbl_first_text, 0, 1, 2, 1)

        self.spacer1_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout_full_text.addItem(self.spacer1_3, 0, 0, 2, 1)

        self.spacer2_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout_full_text.addItem(self.spacer2_3, 0, 4, 2, 1)

        self.lbl_second_text = QLabel(self.centralwidget)
        self.lbl_second_text.setObjectName(u"lbl_second_text")

        self.layout_full_text.addWidget(self.lbl_second_text, 0, 3, 1, 1)

        self.lbl_third_text = QLabel(self.centralwidget)
        self.lbl_third_text.setObjectName(u"lbl_third_text")
        self.lbl_third_text.setMinimumSize(QSize(0, 0))

        self.layout_full_text.addWidget(self.lbl_third_text, 1, 3, 1, 1)

        self.spacer1_6 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout_full_text.addItem(self.spacer1_6, 0, 2, 2, 1)


        self.verticalLayout_2.addLayout(self.layout_full_text)

        self.spacer7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer7)

        self.layout_two_button = QGridLayout()
        self.layout_two_button.setObjectName(u"layout_two_button")
        self.btn_hide_password = QPushButton(self.centralwidget)
        self.btn_hide_password.setObjectName(u"btn_hide_password")
        self.btn_hide_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_two_button.addWidget(self.btn_hide_password, 0, 1, 1, 1)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_two_button.addWidget(self.btn_copy, 2, 1, 1, 1)

        self.spacer3_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.layout_two_button.addItem(self.spacer3_3, 1, 1, 1, 1)

        self.spacer1_5 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout_two_button.addItem(self.spacer1_5, 0, 0, 3, 1)

        self.spacer2_5 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout_two_button.addItem(self.spacer2_5, 0, 2, 3, 1)


        self.verticalLayout_2.addLayout(self.layout_two_button)

        self.spacer8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.spacer8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0430\u0442\u043e\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.lbl_main_name.setText(QCoreApplication.translate("MainWindow", u"\U0001f510 \U00000410\U0000043d\U00000430\U0000043b\U00000438\U00000437\U00000430\U00000442\U0000043e\U00000440 \U0000043d\U00000430\U00000434\U00000451\U00000436\U0000043d\U0000043e\U00000441\U00000442\U00000438 \U0000043f\U00000430\U00000440\U0000043e\U0000043b\U00000435\U00000439", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
#if QT_CONFIG(shortcut)
        self.btn_start.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.status_bar.setFormat("")
        self.lbl_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442: ", None))
        self.lbl_full_result.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u044b\u0439 \u043e\u0442\u0447\u0435\u0442\n"
"\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0447\u043a\u043e\u0432: \n"
"\u042d\u043d\u0442\u0440\u043e\u043f\u0438\u044f \u043f\u0430\u0440\u043e\u043b\u044f: ", None))
        self.lbl_first_text.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f: \u2028\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0447\u043a\u043e\u0432: \n"
"\u0412\u044b\u0432\u043e\u0434:", None))
        self.lbl_second_text.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0447\u043a\u043e\u0432: \u2028\u0412\u044b\u0432\u043e\u0434:\u2028", None))
        self.lbl_third_text.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0442\u0440\u043e\u043f\u0438\u044f \u043f\u0430\u0440\u043e\u043b\u044f:  \n"
"\u0412\u044b\u0432\u043e\u0434:", None))
        self.btn_hide_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

