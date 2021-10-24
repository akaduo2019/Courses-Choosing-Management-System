import pymysql

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI.register.register import Ui_Dialog


class Register(QDialog, Ui_Dialog):

    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)

        # clicked信号绑定自定义槽jump_to_login
        self.register_confirm_button.clicked.connect(self.jump_to_login)
        # clicked信号链接自定义槽from_register_to_login
        self.register_exit_button.clicked.connect(self.from_register_to_login)

    # 给注册窗口设置背景
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    # 注册确认,跳转到登陆界面
    def jump_to_login(self):

        from runlogin import Login

        # 获取注册的账号，密码以及重复密码
        account = self.account_register_input.text()
        password = self.password_register_input.text()
        re_password = self.re_password_register_input.text()

        # 如果账号为空，则重新输入
        if account == "" or password == "":
            QMessageBox.warning(self, "警告", "账号密码不能为空，请重新输入")
            self.account_register_input.clear()
            self.password_register_input.clear()
            self.re_password_register_input.clear()

        else:
            db = pymysql.connect("localhost", "akaduo", "akaduoadmin", "management_system")
            cursor = db.cursor()
            sql = "SELECT *FROM STUDENT_ACCOUNT "
            cursor.execute(sql)
            # flag=False代表用户名不重复，flag=True代表用户名重复
            flag = False
            for row in cursor.fetchall():
                if account == row[0]:
                    flag = True
                    break
            # 如果用户名重复
            if flag:
                QMessageBox.warning(self, "警告", "账户名已存在，请重新注册")
                self.account_register_input.clear()
                self.password_register_input.clear()
                self.re_password_register_input.clear()

            else:
                if password != re_password:
                    QMessageBox.warning(self, "警告", "两次输入密码不一致，请重新输入")
                    self.account_register_input.clear()
                    self.password_register_input.clear()
                    self.re_password_register_input.clear()
                else:
                    # 向数据库中插入新的账户和密码
                    try:
                        sql = "insert into student_account(account, password) values(%s, %s)"
                        data = (account, password)
                        cursor.execute(sql, data)
                        db.commit()  # 提交
                    except:
                        print(77)
                    cursor.close()
                    db.close()

                    QMessageBox.information(self, "提示", "注册成功，请重新登录")
                    self.close()
                    self.main_student = Login()
                    self.main_student.show()

    # 学生注册界面点击退出按钮跳转回到登录界面
    def from_register_to_login(self):
        from runlogin import Login

        self.close()
        self.login = Login()
        self.login.show()


