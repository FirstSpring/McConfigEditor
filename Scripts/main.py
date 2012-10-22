# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import config, edit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

CONFIG_DIR = r'..\config'

class Ui_MainWindow(object):
    def __init__(self, configDir):
        self.dataChanged = False
        self.configDir = configDir

    def tableUpdate(self, cfg):
        self.tableWidget_edit.clear()
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "変数名", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_edit.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "型", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_edit.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "規定値", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_edit.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "現在値", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_edit.setHorizontalHeaderItem(3, item)
        r = 0
        self.tableWidget_edit.setRowCount(len(cfg.items))
        for item in cfg.items.values():
            self.tableWidget_edit.setItem(r, 0, QtGui.QTableWidgetItem(item.name))
            self.tableWidget_edit.setItem(r, 1, QtGui.QTableWidgetItem(item.type))
            self.tableWidget_edit.setItem(r, 2, QtGui.QTableWidgetItem(item.default))
            self.tableWidget_edit.setItem(r, 3, QtGui.QTableWidgetItem(item.value))
            r += 1

    def overwrite(self):
        self.dataChanged = False
        self.selectedConfig.writeFile()
        self.pushButton_overwrite.setEnabled(False)

    def reload(self):
        configs = loadconfig(self.configDir)
        self.listWidget_list.clear()
        for config in configs:
            self.listWidget_list.addItem(config)

    def selectconfig(self):
        name = self.listWidget_list.currentItem().text()
        if self.dataChanged:
            if name != self.selectedConfig.name:
                if QtGui.QMessageBox.question(self.window,'確認',
                    '上書きしていない変更がありますがよろしいですか？',
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel
                    ) == QtGui.QMessageBox.Cancel:
                    return
        cfg = config.Config(self.configDir, name)
        self.selectedConfig = cfg
        cfg.readFile()
        self.tableUpdate(cfg)
        self.dataChanged = False
        self.pushButton_overwrite.setEnabled(False)

    def selectItem(self):
        name = self.tableWidget_edit.item(self.tableWidget_edit.currentRow(), 0).text()
        item = self.selectedConfig.items[name]
        prevValue = item.value
        EditDialog = QtGui.QDialog()
        dialog = edit.Ui_Dialog_edit(self.selectedConfig.name, item)
        dialog.setupUi(EditDialog)
        EditDialog.exec_()
        self.tableUpdate(self.selectedConfig)
        newValue = item.value
        if str(prevValue).strip() != str(newValue).strip():
            self.dataChanged = True
            self.pushButton_overwrite.setEnabled(True)

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 630)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_reload = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reload.sizePolicy().hasHeightForWidth())
        self.pushButton_reload.setSizePolicy(sizePolicy)
        self.pushButton_reload.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_reload.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_reload.setObjectName(_fromUtf8("pushButton_reload"))
        self.gridLayout.addWidget(self.pushButton_reload, 0, 0, 1, 1)
        self.pushButton_overwrite = QtGui.QPushButton(self.centralwidget)
        self.pushButton_overwrite.setEnabled(False)
        self.pushButton_overwrite.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_overwrite.setFont(font)
        self.pushButton_overwrite.setObjectName(_fromUtf8("pushButton_overwrite"))
        self.gridLayout.addWidget(self.pushButton_overwrite, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_name = QtGui.QLabel(self.centralwidget)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.gridLayout.addWidget(self.label_name, 1, 1, 1, 1)
        self.listWidget_list = QtGui.QListWidget(self.centralwidget)
        self.listWidget_list.setObjectName(_fromUtf8("listWidget_list"))
        self.gridLayout.addWidget(self.listWidget_list, 2, 0, 1, 1)
        self.tableWidget_edit = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_edit.sizePolicy().hasHeightForWidth())
        self.tableWidget_edit.setSizePolicy(sizePolicy)
        self.tableWidget_edit.setAlternatingRowColors(True)
        self.tableWidget_edit.setObjectName(_fromUtf8("tableWidget_edit"))
        self.tableWidget_edit.setColumnCount(4)
        self.tableWidget_edit.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_edit, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        MainWindow.setMenuBar(self.menubar)
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.menu_file.addAction(self.action_exit)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_reload.clicked.connect(self.reload)
        self.pushButton_overwrite.clicked.connect(self.overwrite)
        self.listWidget_list.itemDoubleClicked.connect(self.selectconfig)
        self.tableWidget_edit.itemDoubleClicked.connect(self.selectItem)
        self.action_exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.reload()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "McConfigEditor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reload.setText(QtGui.QApplication.translate("MainWindow", "再読み込み", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_overwrite.setText(QtGui.QApplication.translate("MainWindow", "ファイルに上書き", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "コンフィグファイル一覧(ダブルクリックで編集)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_name.setText(QtGui.QApplication.translate("MainWindow", "変数一覧（ダブルクリックで編集）", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_edit.setSortingEnabled(True)
        self.tableWidget_edit.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.menu_file.setTitle(QtGui.QApplication.translate("MainWindow", "ファイル", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainWindow", "終了", None, QtGui.QApplication.UnicodeUTF8))

def loadconfig(configDir):
    import os
    try:
        files = os.listdir(configDir)
    except:
        QtGui.QMessageBox.warning(None, 'Error',
        'configフォルダがありませんでした\nアプリケーションを終了します')
        sys.exit()
    configs = []
    for file in files:
        if isMLProp(file):
            configs.append(file)
    return configs

def isMLProp(file):
    import re
    engine = re.compile('^(mod_).*(.cfg)')
    return engine.match(file)

if __name__ == '__main__':
    import sys
    print(sys.argv)
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(sys.argv[1] if len(sys.argv) > 1 else CONFIG_DIR)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

