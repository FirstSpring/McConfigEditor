# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import config

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_edit(object):
    def __init__(self, config, item):
        self.modName = config
        self.item = item

    def draw(self):
        self.label_modName.setText(self.modName)
        self.label_itemName.setText(self.item.name)
        self.label_type.setText(self.item.type)
        self.label_defaultValue.setText(self.item.default)
        self.label_minValue.setText(self.item.min)
        self.label_maxValue.setText(self.item.max)
        self.label_info.setText(self.item.info)
        self.lineEdit_value.setText(self.item.value)

    def typecheck(self, value):
        if self.item.type == 'string':
            return True
        elif self.item.type == 'boolean':
            if value == 'true' or value == 'false':
                return True
        else:
            import re
            p = re.compile(r'[0-9.]+')
            if p.match(value):
                return True
        return False


    def accept(self):
        value = self.lineEdit_value.text().strip()
        if self.typecheck(value):
            self.item.setValue(value)
        else:
            QtGui.QMessageBox.warning(self.dialog, 'Error', '不正な形式です')
        self.dialog.accept()

    def setupUi(self, Dialog_edit):
        self.dialog = Dialog_edit
        Dialog_edit.setObjectName(_fromUtf8("Dialog_edit"))
        Dialog_edit.resize(230, 215)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_edit.sizePolicy().hasHeightForWidth())
        Dialog_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        Dialog_edit.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Dialog_edit)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_modName = QtGui.QLabel(Dialog_edit)
        self.label_modName.setObjectName(_fromUtf8("label_modName"))
        self.gridLayout.addWidget(self.label_modName, 0, 1, 1, 1)
        self.label_itemName = QtGui.QLabel(Dialog_edit)
        self.label_itemName.setObjectName(_fromUtf8("label_itemName"))
        self.gridLayout.addWidget(self.label_itemName, 1, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog_edit)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_type = QtGui.QLabel(Dialog_edit)
        self.label_type.setObjectName(_fromUtf8("label_type"))
        self.gridLayout.addWidget(self.label_type, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog_edit)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_defaultValue = QtGui.QLabel(Dialog_edit)
        self.label_defaultValue.setObjectName(_fromUtf8("label_defaultValue"))
        self.gridLayout.addWidget(self.label_defaultValue, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog_edit)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1 ,1)
        self.label_minValue = QtGui.QLabel(Dialog_edit)
        self.label_minValue.setObjectName(_fromUtf8("label_minValue"))
        self.gridLayout.addWidget(self.label_minValue, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog_edit)

        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_maxValue = QtGui.QLabel(Dialog_edit)
        self.label_maxValue.setObjectName(_fromUtf8("label_maxValue"))
        self.gridLayout.addWidget(self.label_maxValue, 5, 1, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog_edit)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_info = QtGui.QLabel(Dialog_edit)
        self.label_info.setObjectName(_fromUtf8("label_info"))
        self.gridLayout.addWidget(self.label_info, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog_edit)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.lineEdit_value = QtGui.QLineEdit(Dialog_edit)
        self.lineEdit_value.setObjectName(_fromUtf8("lineEdit_value"))
        self.gridLayout.addWidget(self.lineEdit_value, 7, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_edit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)

        self.retranslateUi(Dialog_edit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_edit.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_edit)

        self.draw()

    def retranslateUi(self, Dialog_edit):
        Dialog_edit.setWindowTitle(QtGui.QApplication.translate("Dialog_edit", "編集ダイアログ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_modName.setText(QtGui.QApplication.translate("Dialog_edit", "modName", None, QtGui.QApplication.UnicodeUTF8))
        self.label_itemName.setText(QtGui.QApplication.translate("Dialog_edit", "itemName", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_edit", "種類 :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_type.setText(QtGui.QApplication.translate("Dialog_edit", "type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_edit", "規定値 :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_defaultValue.setText(QtGui.QApplication.translate("Dialog_edit", "defaultValue", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_edit", "最小値 :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog_edit", "最大値 :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_minValue.setText(QtGui.QApplication.translate("Dialog_edit", "minValue", None, QtGui.QApplication.UnicodeUTF8))
        self.label_maxValue.setText(QtGui.QApplication.translate("Dialog_edit", "maxValue", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog_edit", "情報 :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_info.setText(QtGui.QApplication.translate("Dialog_edit", "info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_edit", "設定値 :", None, QtGui.QApplication.UnicodeUTF8))


