# Form implementation generated from reading ui file 'ignore\untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 427)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 330, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 251, 321))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listViewDocuments = QtWidgets.QListView(parent=self.widget)
        self.listViewDocuments.setObjectName("listViewDocuments")
        self.horizontalLayout.addWidget(self.listViewDocuments)
        self.listViewAuthors = QtWidgets.QListView(parent=self.widget)
        self.listViewAuthors.setObjectName("listViewAuthors")
        self.horizontalLayout.addWidget(self.listViewAuthors)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(270, 0, 611, 361))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(parent=self.widget1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDocuments = QtWidgets.QMenu(parent=self.menuFile)
        self.menuDocuments.setObjectName("menuDocuments")
        self.menuAuthors = QtWidgets.QMenu(parent=self.menuFile)
        self.menuAuthors.setObjectName("menuAuthors")
        self.menuFile_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile_2.setObjectName("menuFile_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Batch = QtGui.QAction(parent=MainWindow)
        self.actionLoad_Batch.setObjectName("actionLoad_Batch")
        self.actionSave_Group = QtGui.QAction(parent=MainWindow)
        self.actionSave_Group.setObjectName("actionSave_Group")
        self.actionOpen_Set = QtGui.QAction(parent=MainWindow)
        self.actionOpen_Set.setObjectName("actionOpen_Set")
        self.actionSave_Set = QtGui.QAction(parent=MainWindow)
        self.actionSave_Set.setObjectName("actionSave_Set")
        self.actionSave_Set_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_Set_As.setObjectName("actionSave_Set_As")
        self.actionAdd_Document_Type = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Document_Type.setObjectName("actionAdd_Document_Type")
        self.actionAdd_Document_Set = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Document_Set.setObjectName("actionAdd_Document_Set")
        self.actionRemove_Document_Type = QtGui.QAction(parent=MainWindow)
        self.actionRemove_Document_Type.setObjectName("actionRemove_Document_Type")
        self.actionAdd_Author_Style = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Author_Style.setObjectName("actionAdd_Author_Style")
        self.actionAssign_Author_Style = QtGui.QAction(parent=MainWindow)
        self.actionAssign_Author_Style.setObjectName("actionAssign_Author_Style")
        self.actionWrite_Emails = QtGui.QAction(parent=MainWindow)
        self.actionWrite_Emails.setObjectName("actionWrite_Emails")
        self.actionHook_Up_API = QtGui.QAction(parent=MainWindow)
        self.actionHook_Up_API.setObjectName("actionHook_Up_API")
        self.menuDocuments.addAction(self.actionAdd_Document_Type)
        self.menuDocuments.addAction(self.actionAdd_Document_Set)
        self.menuDocuments.addAction(self.actionRemove_Document_Type)
        self.menuAuthors.addAction(self.actionAdd_Author_Style)
        self.menuAuthors.addAction(self.actionAssign_Author_Style)
        self.menuFile.addAction(self.menuDocuments.menuAction())
        self.menuFile.addAction(self.menuAuthors.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHook_Up_API)
        self.menuFile_2.addAction(self.actionOpen_Set)
        self.menuFile_2.addAction(self.actionSave_Set)
        self.menuFile_2.addAction(self.actionSave_Set_As)
        self.menuFile_2.addAction(self.actionLoad_Batch)
        self.menuFile_2.addSeparator()
        self.menuFile_2.addAction(self.actionWrite_Emails)
        self.menubar.addAction(self.menuFile_2.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listViewDocuments, self.listViewAuthors)
        MainWindow.setTabOrder(self.listViewAuthors, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Attach..."))
        self.pushButton_3.setText(_translate("MainWindow", "<"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_4.setText(_translate("MainWindow", ">"))
        self.menuFile.setTitle(_translate("MainWindow", "Edit"))
        self.menuDocuments.setTitle(_translate("MainWindow", "Documents"))
        self.menuAuthors.setTitle(_translate("MainWindow", "Authors"))
        self.menuFile_2.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Batch.setText(_translate("MainWindow", "Load Recipients"))
        self.actionSave_Group.setText(_translate("MainWindow", "Save Group"))
        self.actionOpen_Set.setText(_translate("MainWindow", "Open Set..."))
        self.actionSave_Set.setText(_translate("MainWindow", "Save Set"))
        self.actionSave_Set_As.setText(_translate("MainWindow", "Save Set As..."))
        self.actionAdd_Document_Type.setText(_translate("MainWindow", "Add Document Type..."))
        self.actionAdd_Document_Set.setText(_translate("MainWindow", "Add Document Set..."))
        self.actionRemove_Document_Type.setText(_translate("MainWindow", "Remove Document Type"))
        self.actionAdd_Author_Style.setText(_translate("MainWindow", "Add Author Style..."))
        self.actionAssign_Author_Style.setText(_translate("MainWindow", "Assign Author Style ..."))
        self.actionWrite_Emails.setText(_translate("MainWindow", "Write Emails"))
        self.actionHook_Up_API.setText(_translate("MainWindow", "Hook Up API"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
