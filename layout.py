# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(579, 466)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 561, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.normalPizza = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.normalPizza.setObjectName("normalPizza")
        self.gridLayout.addWidget(self.normalPizza, 0, 2, 1, 1)
        self.bigPizza = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.bigPizza.setAutoFillBackground(False)
        self.bigPizza.setObjectName("bigPizza")
        self.gridLayout.addWidget(self.bigPizza, 0, 3, 1, 2)
        self.pinapleBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.pinapleBox.setObjectName("pinapleBox")
        self.gridLayout.addWidget(self.pinapleBox, 4, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.smallPizza = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.smallPizza.setObjectName("smallPizza")
        self.gridLayout.addWidget(self.smallPizza, 0, 0, 1, 2)
        self.cheeseBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.cheeseBox.setObjectName("cheeseBox")
        self.gridLayout.addWidget(self.cheeseBox, 3, 3, 1, 2)
        self.mushroomBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.mushroomBox.setObjectName("mushroomBox")
        self.gridLayout.addWidget(self.mushroomBox, 1, 3, 1, 2)
        self.salamiBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.salamiBox.setObjectName("salamiBox")
        self.gridLayout.addWidget(self.salamiBox, 2, 3, 1, 2)
        self.orderButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.orderButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.orderButton.setObjectName("orderButton")
        self.gridLayout.addWidget(self.orderButton, 5, 1, 1, 3)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 4, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 4, 1, 1)
        self.output = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.output.setMaximumSize(QtCore.QSize(16777215, 80))
        self.output.setText("")
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 6, 0, 1, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.normalPizza.setText(_translate("Dialog", "Pizza normalna"))
        self.bigPizza.setText(_translate("Dialog", "Pizza duża"))
        self.pinapleBox.setText(_translate("Dialog", "Ananas"))
        self.smallPizza.setText(_translate("Dialog", "Pizza mała"))
        self.cheeseBox.setText(_translate("Dialog", "Podwójny ser"))
        self.mushroomBox.setText(_translate("Dialog", "Pierczarki"))
        self.salamiBox.setText(_translate("Dialog", "Salami"))
        self.orderButton.setText(_translate("Dialog", "Zamów"))
        self.label.setText(_translate("Dialog", "Wybierz dodatki"))
