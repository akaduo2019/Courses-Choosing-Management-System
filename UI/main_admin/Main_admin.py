# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 810)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 810))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 810))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/1/icons/window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(270, 80, 860, 560))
        self.tabWidget.setMinimumSize(QtCore.QSize(860, 560))
        self.tabWidget.setMaximumSize(QtCore.QSize(860, 560))
        self.tabWidget.setStyleSheet("QPushButton{border-radius: 10px;border: 2px groove gray;border-style: outset;}\n"
"QPushButton:hover{color: #66A3FF;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fafafa, stop: 0.4 #f4f4f4,stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}\n"
"QPushButton:pressed{color: #E680BD;}\n"
"QTabBar::tab:hover{color: #66A3FF;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fafafa, stop: 0.4 #f4f4f4,stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}\n"
"QTabBar::tab:selected{color: #E680BD;}")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.confirm_course_admin_button = QtWidgets.QPushButton(self.tab)
        self.confirm_course_admin_button.setGeometry(QtCore.QRect(740, 480, 101, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/1/icons/确认.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm_course_admin_button.setIcon(icon1)
        self.confirm_course_admin_button.setObjectName("confirm_course_admin_button")
        self.admin_setcourse_tableWidget = QtWidgets.QTableWidget(self.tab)
        self.admin_setcourse_tableWidget.setGeometry(QtCore.QRect(110, 40, 611, 391))
        self.admin_setcourse_tableWidget.setObjectName("admin_setcourse_tableWidget")
        self.admin_setcourse_tableWidget.setColumnCount(1)
        self.admin_setcourse_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/1/icons/选择.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.admin_setcourse_tableWidget.setHorizontalHeaderItem(0, item)
        self.admin_add_button = QtWidgets.QPushButton(self.tab)
        self.admin_add_button.setGeometry(QtCore.QRect(740, 50, 101, 28))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/1/icons/增加课程.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.admin_add_button.setIcon(icon3)
        self.admin_add_button.setObjectName("admin_add_button")
        self.admin_del_button = QtWidgets.QPushButton(self.tab)
        self.admin_del_button.setGeometry(QtCore.QRect(740, 100, 101, 28))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/1/icons/减少课程.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.admin_del_button.setIcon(icon4)
        self.admin_del_button.setObjectName("admin_del_button")
        self.back_admin_button = QtWidgets.QPushButton(self.tab)
        self.back_admin_button.setGeometry(QtCore.QRect(20, 480, 101, 28))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/1/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_admin_button.setIcon(icon5)
        self.back_admin_button.setObjectName("back_admin_button")
        self.admin_reset_button = QtWidgets.QPushButton(self.tab)
        self.admin_reset_button.setGeometry(QtCore.QRect(740, 230, 101, 28))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/1/icons/重置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.admin_reset_button.setIcon(icon6)
        self.admin_reset_button.setObjectName("admin_reset_button")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/1/icons/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon7, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.update_admin_button = QtWidgets.QPushButton(self.tab_2)
        self.update_admin_button.setGeometry(QtCore.QRect(370, 50, 93, 28))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/1/icons/更新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_admin_button.setIcon(icon8)
        self.update_admin_button.setObjectName("update_admin_button")
        self.admin_display_tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.admin_display_tableWidget.setGeometry(QtCore.QRect(0, 110, 851, 421))
        self.admin_display_tableWidget.setObjectName("admin_display_tableWidget")
        self.admin_display_tableWidget.setColumnCount(0)
        self.admin_display_tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.admin_display_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_display_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_display_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_display_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_display_tableWidget.setVerticalHeaderItem(4, item)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/1/icons/统计.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon9, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 201, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/1/icons/管理员.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.confirm_course_admin_button, self.update_admin_button)
        MainWindow.setTabOrder(self.update_admin_button, self.admin_display_tableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "教务管理"))
        self.confirm_course_admin_button.setText(_translate("MainWindow", "确认"))
        item = self.admin_setcourse_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选择栏"))
        self.admin_add_button.setText(_translate("MainWindow", "增加课程"))
        self.admin_del_button.setText(_translate("MainWindow", "删除课程"))
        self.back_admin_button.setText(_translate("MainWindow", "退出"))
        self.admin_reset_button.setText(_translate("MainWindow", "重置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "课程设置"))
        self.update_admin_button.setText(_translate("MainWindow", "更新"))
        item = self.admin_display_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1班"))
        item = self.admin_display_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2班"))
        item = self.admin_display_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3班"))
        item = self.admin_display_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4班"))
        item = self.admin_display_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "总人数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "选课统计"))
import resourse.icons_rc
import resourse.images_rc
