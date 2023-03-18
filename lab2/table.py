from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from root_refirement import ERRORS_INFO


class TableWidget(QTableWidget):
    def __init__(self, parent):
        super(TableWidget, self).__init__(parent)
        self.setColumnCount(5)
        self.setRowCount(0)

        self.setHorizontalHeaderLabels(["[a, b]", "x", "y", "iter", "error"])

    def add_row(self, *args):
        row = self.rowCount()
        self.setRowCount(row + 1)
        self.setVerticalHeaderItem(row, QTableWidgetItem(str(row + 1)))
        for i in range(5):
            item = QTableWidgetItem(args[i])
            item.setFlags(Qt.ItemIsEnabled)
            self.setItem(row, i, item)
        if args[4] in ERRORS_INFO:
            self.item(row, 4).setToolTip(ERRORS_INFO[args[4]])

    def clear(self):
        for i in range(self.rowCount()):
            self.removeRow(0)
