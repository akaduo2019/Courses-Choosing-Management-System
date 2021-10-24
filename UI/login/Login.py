# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1050, 750)
        Dialog.setMinimumSize(QtCore.QSize(1050, 750))
        Dialog.setMaximumSize(QtCore.QSize(1050, 750))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/1/icons/window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(550, 400))
        self.tabWidget.setMaximumSize(QtCore.QSize(550, 399))
        self.tabWidget.setStyleSheet("QPushButton{border-radius: 10px;border: 2px groove gray;border-style: outset;}\n"
"QPushButton:hover{color: #66A3FF;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fafafa, stop: 0.4 #f4f4f4,stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}\n"
"QPushButton:pressed{color: #E680BD;}\n"
"QLineEdit{border:0px;margin:10px;border-bottom: 2px solid #B3B3B3}\n"
"QLineEdit:hover{border-bottom: 3px solid #66A3FF;}\n"
"QLineEdit:focus{border-bottom: 3px solid #E680BD;}\n"
"QTabBar::tab:hover{color: #66A3FF;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fafafa, stop: 0.4 #f4f4f4,stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}\n"
"QTabBar::tab:selected{color: #E680BD;}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.register_button_student = QtWidgets.QPushButton(self.tab)
        self.register_button_student.setGeometry(QtCore.QRect(185, 210, 101, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_button_student.sizePolicy().hasHeightForWidth())
        self.register_button_student.setSizePolicy(sizePolicy)
        self.register_button_student.setObjectName("register_button_student")
        self.login_button_student = QtWidgets.QPushButton(self.tab)
        self.login_button_student.setGeometry(QtCore.QRect(295, 210, 101, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button_student.sizePolicy().hasHeightForWidth())
        self.login_button_student.setSizePolicy(sizePolicy)
        self.login_button_student.setObjectName("login_button_student")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 90, 251, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.account_input_student = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_input_student.sizePolicy().hasHeightForWidth())
        self.account_input_student.setSizePolicy(sizePolicy)
        self.account_input_student.setObjectName("account_input_student")
        self.horizontalLayout.addWidget(self.account_input_student)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.password_input_student = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_input_student.sizePolicy().hasHeightForWidth())
        self.password_input_student.setSizePolicy(sizePolicy)
        self.password_input_student.setObjectName("password_input_student")
        self.horizontalLayout_3.addWidget(self.password_input_student)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/1/icons/学生.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.login_button_admin = QtWidgets.QPushButton(self.tab_2)
        self.login_button_admin.setGeometry(QtCore.QRect(235, 210, 101, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button_admin.sizePolicy().hasHeightForWidth())
        self.login_button_admin.setSizePolicy(sizePolicy)
        self.login_button_admin.setObjectName("login_button_admin")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 90, 251, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.account_input_admin = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_input_admin.sizePolicy().hasHeightForWidth())
        self.account_input_admin.setSizePolicy(sizePolicy)
        self.account_input_admin.setObjectName("account_input_admin")
        self.horizontalLayout_4.addWidget(self.account_input_admin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.password_input_admin = QtWidgets.QLineEdit(self.layoutWidget1)
        self.password_input_admin.setObjectName("password_input_admin")
        self.horizontalLayout_2.addWidget(self.password_input_admin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/1/icons/管理员.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.login_button_student.clicked.connect(self.login_button_student.show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.account_input_student)
        Dialog.setTabOrder(self.account_input_student, self.password_input_student)
        Dialog.setTabOrder(self.password_input_student, self.login_button_student)
        Dialog.setTabOrder(self.login_button_student, self.register_button_student)
        Dialog.setTabOrder(self.register_button_student, self.account_input_admin)
        Dialog.setTabOrder(self.account_input_admin, self.password_input_admin)
        Dialog.setTabOrder(self.password_input_admin, self.login_button_admin)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登陆"))
        self.register_button_student.setText(_translate("Dialog", "注册"))
        self.login_button_student.setText(_translate("Dialog", "登陆"))
        self.label.setText(_translate("Dialog", "账号:"))
        self.label_2.setText(_translate("Dialog", "密码:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "学生"))
        self.login_button_admin.setText(_translate("Dialog", "登陆"))
        self.label_4.setText(_translate("Dialog", "账号:"))
        self.label_3.setText(_translate("Dialog", "密码:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "教务"))
import resourse.icons_rc
import resourse.images_rc
