from PyQt5.QtWidgets import QHBoxLayout, QAbstractItemView
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QVBoxLayout


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.setWindowTitle('Contacts')
        self.resize(500, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self._setupUI()

    def _setupUI(self):
        """Setup the main window gui."""
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # create buttons
        self.addButton = QPushButton("Add..")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
