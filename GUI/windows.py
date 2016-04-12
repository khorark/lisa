# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created: Sun Apr  3 14:03:39 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 400)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dir_name_le = QtWidgets.QLineEdit(self.centralwidget)
        self.dir_name_le.setText("")
        self.dir_name_le.setDragEnabled(True)
        self.dir_name_le.setReadOnly(True)
        self.dir_name_le.setObjectName("dir_name_le")
        self.horizontalLayout.addWidget(self.dir_name_le)
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.extens_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.extens_rb.setObjectName("extens_rb")
        self.verticalLayout.addWidget(self.extens_rb)
        self.date_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.date_rb.setObjectName("date_rb")
        self.verticalLayout.addWidget(self.date_rb)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.year_chb = QtWidgets.QCheckBox(self.centralwidget)
        self.year_chb.setObjectName("year_chb")
        self.horizontalLayout_3.addWidget(self.year_chb)
        self.month_chb = QtWidgets.QCheckBox(self.centralwidget)
        self.month_chb.setObjectName("month_chb")
        self.horizontalLayout_3.addWidget(self.month_chb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.list_files_lw = QtWidgets.QListWidget(self.centralwidget)
        self.list_files_lw.setAcceptDrops(True)
        self.list_files_lw.setProperty("isWrapping", False)
        self.list_files_lw.setViewMode(QtWidgets.QListView.ListMode)
        self.list_files_lw.setModelColumn(0)
        self.list_files_lw.setWordWrap(True)
        self.list_files_lw.setObjectName("list_files_lw")
        self.verticalLayout.addWidget(self.list_files_lw)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress_pg = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_pg.setProperty("value", 0)
        self.progress_pg.setObjectName("progress_pg")
        self.horizontalLayout_2.addWidget(self.progress_pg)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_2.addWidget(self.start_btn)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Dir = QtWidgets.QAction(MainWindow)
        self.actionOpen_Dir.setObjectName("actionOpen_Dir")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_Dir)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.action_2)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "lisa-GUI"))
        self.open_btn.setText(_translate("MainWindow", "Open"))
        self.extens_rb.setText(_translate("MainWindow", "Sort by extansions"))
        self.date_rb.setText(_translate("MainWindow", "Sort by date"))
        self.year_chb.setText(_translate("MainWindow", "year"))
        self.month_chb.setText(_translate("MainWindow", "month"))
        self.list_files_lw.setSortingEnabled(True)
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Dir.setText(_translate("MainWindow", "Open Dir"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.action_2.setText(_translate("MainWindow", "?"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
