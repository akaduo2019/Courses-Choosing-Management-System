import pymysql

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Login import Ui_Dialog
from runmain_student import Main
from runmain_admin import MainAdmin
from runregister import Register


class Login(QDialog, Ui_Dialog):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

        # clicked信号绑定自定义槽login_to_main_student
        self.login_button_student.clicked.connect(self.login_to_main_student)
        # clicked信号绑定自定义槽login_to_main_admin
        self.login_button_admin.clicked.connect(self.login_to_main_admin)
        # clicked信号链接自定义槽jump_to_register_student
        self.register_button_student.clicked.connect(self.jump_to_register_student)

        # 设置密码文本框显示模式:输入时为密文显示
        self.password_input_student.setEchoMode(QLineEdit.Password)
        self.password_input_admin.setEchoMode(QLineEdit.Password)

    # 给登录窗口设置背景
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    # 学生登陆界面跳转学生主界面
    def login_to_main_student(self):
        # 获取用户(学生)输入文本框内容,即账号密码
        account = self.account_input_student.text()
        password = self.password_input_student.text()

        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "clf20001212", "management_system")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT *FROM STUDENT_ACCOUNT "
        cursor.execute(sql)
        flag = False
        for row in cursor.fetchall():
            if account == row[0] and password == row[1]:
                flag = True
                break
        if flag:
            QMessageBox.information(self, "提示", "登陆成功")
            # 明确当前账户
            sql = "UPDATE NOW_ACCOUNT SET now_account=%s "
            cursor.execute(sql, account)
            db.commit()

            self.close()
            self.main_student = Main()
            self.main_student.show()



        else:
            QMessageBox.warning(self, "警告", "账号或密码输入错误，请重新输入")
            # 清空账号和密码的单行文本框
            self.account_input_student.clear()
            self.password_input_student.clear()

        cursor.close()
        db.close()

    # 教务登录界面跳转管理员主界面
    def login_to_main_admin(self):
        # 获取管理员账号和密码
        admin_user = self.account_input_admin.text()
        admin_password = self.password_input_admin.text()

        db = pymysql.connect("localhost", "root", "clf20001212", "management_system")
        cursor = db.cursor()
        sql = "SELECT *FROM ADMIN_ACCOUNT"
        cursor.execute(sql)
        data = cursor.fetchone()
        if admin_user == data[0] and admin_password == data[1]:
            QMessageBox.information(self, "提示", "admin登录成功")
            self.close()
            self.main_admin = MainAdmin()
            self.main_admin.show()
        else:
            QMessageBox.warning(self, "警告", "admin账号或密码错误，请重新输入")
            self.account_input_student.clear()
            self.password_input_student.clear()

        cursor.close()
        db.close()

    # 学生登录界面跳转注册界面
    def jump_to_register_student(self):
        self.close()
        self.register = Register()
        self.register.show()

