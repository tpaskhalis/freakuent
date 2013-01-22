from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 565)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label.setObjectName("label")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 20, 281, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 81, 17))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 150, 281, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 59, 17))
        self.label_5.setObjectName("label_5")
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 340, 291, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 291, 95))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.inputPathEdit = QtGui.QLineEdit(self.widget)
        self.inputPathEdit.setObjectName("inputPathEdit")
        self.gridLayout.addWidget(self.inputPathEdit, 0, 1, 1, 1)
        self.inputDocumentBrowser = QtGui.QPushButton(self.widget)
        self.inputDocumentBrowser.setObjectName("inputDocumentBrowser")
        self.gridLayout.addWidget(self.inputDocumentBrowser, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.languageCombo = QtGui.QComboBox(self.widget)
        self.languageCombo.setObjectName("languageCombo")
        self.gridLayout.addWidget(self.languageCombo, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.encodingCombo = QtGui.QComboBox(self.widget)
        self.encodingCombo.setObjectName("encodingCombo")
        self.gridLayout.addWidget(self.encodingCombo, 2, 1, 1, 2)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 370, 381, 143))
        self.widget1.setObjectName("widget1")
        self.gridLayout_4 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.outputWordsRadio = QtGui.QRadioButton(self.widget1)
        self.outputWordsRadio.setObjectName("outputWordsRadio")
        self.gridLayout_3.addWidget(self.outputWordsRadio, 0, 0, 1, 2)
        self.outputTagsRadio = QtGui.QRadioButton(self.widget1)
        self.outputTagsRadio.setObjectName("outputTagsRadio")
        self.gridLayout_3.addWidget(self.outputTagsRadio, 1, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.outputPathEdit = QtGui.QLineEdit(self.widget1)
        self.outputPathEdit.setObjectName("outputPathEdit")
        self.gridLayout_3.addWidget(self.outputPathEdit, 2, 1, 1, 1)
        self.outputDocumentBrowser = QtGui.QPushButton(self.widget1)
        self.outputDocumentBrowser.setObjectName("outputDocumentBrowser")
        self.gridLayout_3.addWidget(self.outputDocumentBrowser, 2, 2, 1, 1)
        self.processButton = QtGui.QPushButton(self.widget1)
        self.processButton.setObjectName("processButton")
        self.gridLayout_3.addWidget(self.processButton, 3, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 180, 391, 158))
        self.widget2.setObjectName("widget2")
        self.gridLayout_5 = QtGui.QGridLayout(self.widget2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lowerCheck = QtGui.QCheckBox(self.widget2)
        self.lowerCheck.setObjectName("lowerCheck")
        self.gridLayout_2.addWidget(self.lowerCheck, 0, 0, 1, 1)
        self.regexpCheck = QtGui.QCheckBox(self.widget2)
        self.regexpCheck.setObjectName("regexpCheck")
        self.gridLayout_2.addWidget(self.regexpCheck, 1, 0, 1, 1)
        self.regexpEdit = QtGui.QLineEdit(self.widget2)
        self.regexpEdit.setObjectName("regexpEdit")
        self.gridLayout_2.addWidget(self.regexpEdit, 1, 1, 1, 1)
        self.stopwordsCheck = QtGui.QCheckBox(self.widget2)
        self.stopwordsCheck.setObjectName("stopwordsCheck")
        self.gridLayout_2.addWidget(self.stopwordsCheck, 2, 0, 1, 1)
        self.stopwordsCombo = QtGui.QComboBox(self.widget2)
        self.stopwordsCombo.setObjectName("stopwordsCombo")
        self.gridLayout_2.addWidget(self.stopwordsCombo, 2, 1, 1, 1)
        self.stemmerCheck = QtGui.QCheckBox(self.widget2)
        self.stemmerCheck.setObjectName("stemmerCheck")
        self.gridLayout_2.addWidget(self.stemmerCheck, 3, 0, 1, 1)
        self.stemmerCombo = QtGui.QComboBox(self.widget2)
        self.stemmerCombo.setObjectName("stemmerCombo")
        self.gridLayout_2.addWidget(self.stemmerCombo, 3, 1, 1, 1)
        self.tokenizerCheck = QtGui.QCheckBox(self.widget2)
        self.tokenizerCheck.setObjectName("tokenizerCheck")
        self.gridLayout_2.addWidget(self.tokenizerCheck, 4, 0, 1, 1)
        self.tokenizerCombo = QtGui.QComboBox(self.widget2)
        self.tokenizerCombo.setObjectName("tokenizerCombo")
        self.gridLayout_2.addWidget(self.tokenizerCombo, 4, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Documents = QtGui.QAction(MainWindow)
        self.actionAdd_Documents.setObjectName("actionAdd_Documents")
        self.actionRemove_Documents = QtGui.QAction(MainWindow)
        self.actionRemove_Documents.setObjectName("actionRemove_Documents")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAdd_Documents)
        self.menuFile.addAction(self.actionRemove_Documents)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Document", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.inputDocumentBrowser.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.outputWordsRadio.setText(QtGui.QApplication.translate("MainWindow", "Words", None, QtGui.QApplication.UnicodeUTF8))
        self.outputTagsRadio.setText(QtGui.QApplication.translate("MainWindow", "POS tags", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDocumentBrowser.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.processButton.setText(QtGui.QApplication.translate("MainWindow", "&Process", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerCheck.setText(QtGui.QApplication.translate("MainWindow", "Lowercase", None, QtGui.QApplication.UnicodeUTF8))
        self.regexpCheck.setText(QtGui.QApplication.translate("MainWindow", "Remove regexp", None, QtGui.QApplication.UnicodeUTF8))
        self.stopwordsCheck.setText(QtGui.QApplication.translate("MainWindow", "Remove stopwords", None, QtGui.QApplication.UnicodeUTF8))
        self.stemmerCheck.setText(QtGui.QApplication.translate("MainWindow", "Apply stemmer", None, QtGui.QApplication.UnicodeUTF8))
        self.tokenizerCheck.setText(QtGui.QApplication.translate("MainWindow", "Apply tokenizer", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Documents.setText(QtGui.QApplication.translate("MainWindow", "Add Documents", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_Documents.setText(QtGui.QApplication.translate("MainWindow", "Remove Documents", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))