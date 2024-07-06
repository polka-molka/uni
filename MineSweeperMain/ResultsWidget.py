from PyQt6.QtCore import pyqtSignal, QRect, QSize
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QToolButton, QTableWidget, QAbstractItemView, QTableWidgetItem


class ResultsWidget(QWidget):
    switch_to_main_page = pyqtSignal()

    def __init__(self, results):
        super().__init__()
        self.setStyleSheet("background-color:#B0BFD7")
        # Создание вертикального контейнера
        # layout = QVBoxLayout()

        # Создание метки для заголовка
        title_label = QLabel("Players results:", parent=self)
        title_label.setGeometry(QRect(80, 10, 200, 30))

        # layout.addWidget(title_label)
        font = QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(16)
        title_label.setFont(font)
        title_label.setStyleSheet('Background-color: #8296B4 ')
        self.menu_btn = QToolButton(parent=self)
        self.menu_btn.setGeometry(QRect(10, 10, 31, 31))
        self.menu_btn.setFont(font)
        self.menu_btn.setAutoFillBackground(False)
        self.menu_btn.setStyleSheet("background-color:#B0BFD7\n")
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/menu.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(18, 18))
        self.menu_btn.clicked.connect(self.go_to_menu)
        self.table = QTableWidget(parent=self)
        self.table.setGeometry(QRect(35, 50, 650, 420))
        self.table.setFont(font)
        self.setStyleSheet('Background-color: #B0BFD7')
        self.table.setRowCount(len(results))
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0, 250)
        self.table.setColumnWidth(1, 350)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(["NickName", "Scores"])
        font.setPointSize(11)
        self.table.horizontalHeader().setFont(font)
        self.table.horizontalHeader().setStyleSheet("QTableWidget disabled:{background-color:#B0BFD7}")
        self.table.horizontalHeader().setEnabled(False)
        self.table.verticalHeader().setEnabled(False)

        for row, result in enumerate(results):
            username, score = result.split(" - ")
            self.table.setItem(row, 0, QTableWidgetItem(username))
            self.table.setItem(row, 1, QTableWidgetItem(score))

        self.table.horizontalHeader().setStretchLastSection(True)
        self.setFixedSize(720, 480)
        self.setWindowTitle("Players results:")

    def update_results(self, new_results):
        self.table.clearContents()
        self.table.setRowCount(len(new_results))
        for row, result in enumerate(new_results):
            username, score = result.split(" - ")
            self.table.setItem(row, 0, QTableWidgetItem(username))
            self.table.setItem(row, 1, QTableWidgetItem(score))
        self.table.update()

    def go_to_menu(self):
        self.switch_to_main_page.emit()
