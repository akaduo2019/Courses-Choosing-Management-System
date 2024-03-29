# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1050, 750)
        Dialog.setMinimumSize(QtCore.QSize(1050, 750))
        Dialog.setMaximumSize(QtCore.QSize(1050, 750))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/1/icons/window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("font: 10pt \"微软雅黑\";")
        Dialog.setSizeGripEnabled(False)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(550, 400))
        self.tabWidget.setMaximumSize(QtCore.QSize(550, 400))
        self.tabWidget.setStyleSheet("QPushButton{border-radius: 10px;border: 2px groove gray;border-style: outset;}\n"
"QPushButton:hover{color: #66A3FF;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fafafa, stop: 0.4 #f4f4f4,stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}\n"
"QPushButton:pressed{color: #E680BD;}\n"
"QLineEdit{border:0px;margin:10px;border-bottom: 2px solid #B3B3B3}\n"
"QLineEdit:hover{border-bottom: 3px solid #66A3FF;}\n"
"QLineEdit:focus{border-bottom: 3px solid #E680BD;}\n"
"QTabBar::tab:hover{color: #66A3FF;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fafafa, stop: 0.4 #f4f4f4,stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}\n"
"QTabBar::tab:selected{color: #E680BD;}")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.register_exit_button = QtWidgets.QPushButton(self.tab)
        self.register_exit_button.setGeometry(QtCore.QRect(150, 220, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_exit_button.sizePolicy().hasHeightForWidth())
        self.register_exit_button.setSizePolicy(sizePolicy)
        self.register_exit_button.setObjectName("register_exit_button")
        self.register_confirm_button = QtWidgets.QPushButton(self.tab)
        self.register_confirm_button.setGeometry(QtCore.QRect(310, 220, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_confirm_button.sizePolicy().hasHeightForWidth())
        self.register_confirm_button.setSizePolicy(sizePolicy)
        self.register_confirm_button.setObjectName("register_confirm_button")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(151, 126, 235, 49))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_register_input = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_register_input.sizePolicy().hasHeightForWidth())
        self.password_register_input.setSizePolicy(sizePolicy)
        self.password_register_input.setObjectName("password_register_input")
        self.horizontalLayout_2.addWidget(self.password_register_input)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(151, 81, 235, 49))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.account_register_input = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_register_input.sizePolicy().hasHeightForWidth())
        self.account_register_input.setSizePolicy(sizePolicy)
        self.account_register_input.setObjectName("account_register_input")
        self.horizontalLayout.addWidget(self.account_register_input)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(152, 173, 269, 49))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.re_password_register_input = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.re_password_register_input.sizePolicy().hasHeightForWidth())
        self.re_password_register_input.setSizePolicy(sizePolicy)
        self.re_password_register_input.setObjectName("re_password_register_input")
        self.horizontalLayout_3.addWidget(self.re_password_register_input)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/1/icons/注册.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.account_register_input, self.password_register_input)
        Dialog.setTabOrder(self.password_register_input, self.register_confirm_button)
        Dialog.setTabOrder(self.register_confirm_button, self.register_exit_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注册"))
        self.register_exit_button.setText(_translate("Dialog", "退出"))
        self.register_confirm_button.setText(_translate("Dialog", "确认注册"))
        self.label_2.setText(_translate("Dialog", "密码:"))
        self.label.setText(_translate("Dialog", "账号:"))
        self.label_3.setText(_translate("Dialog", "重复密码:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "学生注册"))
import resourse.icons_rc
import resourse.images_rc