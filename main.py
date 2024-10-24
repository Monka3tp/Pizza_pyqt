import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.orderButton.clicked.connect(self.order)
        self.show()

    def order(self):
        size = "Wybierz rozmiar"
        if self.ui.normalPizza.isChecked():
            size = self.ui.normalPizza.text()
        elif self.ui.bigPizza.isChecked():
            size = self.ui.bigPizza.text()
        elif self.ui.smallPizza.isChecked():
            size = self.ui.smallPizza.text()
        else:
            return

        dodatki = []
        if self.ui.mushroomBox.isChecked():
            dodatki.append(self.ui.mushroomBox.text())
        if self.ui.cheeseBox.isChecked():
            dodatki.append(self.ui.cheeseBox.text())
        if self.ui.pinapleBox.isChecked():
            dodatki.append(self.ui.pinapleBox.text())
        if self.ui.salamiBox.isChecked():
            dodatki.append(self.ui.salamiBox.text())
        dodatki_str = ", ".join(dodatki)
        self.ui.output.setText(f"Wybrano {size} z {dodatki_str}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())