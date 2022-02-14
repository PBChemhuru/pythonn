import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar


# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle("this is start")
# window.setGeometry(300, 200, 1000, 1000)
# window.move(60, 15)
# helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
# layout = QGridLayout()
# layout.addWidget(QPushButton('Left'), 0, 0)
# layout.addWidget(QPushButton('Center'), 0, 1)
# layout.addWidget(QPushButton('Right'), 1, 1)
# layout.addWidget((helloMsg), 1, 0)
# layout.addWidget(QLineEdit()), 2, 0, 2, 1
# layout2 = QFormLayout()
# layout2.addRow('Name:', QLineEdit())
# layout2.addRow('Age:', QLineEdit())
# layout2.addRow('Job:', QLineEdit())
# layout2.addRow('Hobbies:', QLineEdit())
# layout3 = QHBoxLayout()
# layout3.addLayout(layout2)
# layout3.addLayout(layout)
# window.setLayout(layout3)


# class Dialog(QDialog):
#     """Dialog."""
#     def __init__(self, parent=None):
#
#         "Initializer"
#         super().__init__(parent)
#         self.setWindowTitle('QDialog')
#         dlgLayout = QVBoxLayout()
#         formLayout = QFormLayout()
#         formLayout.addRow('Name:', QLineEdit())
#         formLayout.addRow('Age:', QLineEdit())
#         formLayout.addRow('Job:', QLineEdit())
#         formLayout.addRow('Hobbies:', QLineEdit())
#         dlgLayout.addLayout(formLayout)
#         btns = QDialogButtonBox()
#         btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
#         dlgLayout.addWidget(btns)
#         self.setLayout(dlgLayout)


class Window(QMainWindow):
    """Main Window"""

    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setGeometry(100, 100, 200, 150)
        self.setCentralWidget(QLabel("I'm the Central Widgets"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

# window.show()

#
# def greeting():
#     """Slot function."""
#     if msg.text():
#         msg.setText("")
#     else:
#         msg.setText("Hello World!")
#
#
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('Signals and slots')
# layout = QVBoxLayout()
#
# btn = QPushButton('Greet')
# btn.clicked.connect(greeting)  # Connect clicked to greeting()
#
# layout.addWidget(btn)
# msg = QLabel('')
# layout.addWidget(msg)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())
