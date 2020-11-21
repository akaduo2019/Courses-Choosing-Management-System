import pymysql
import re

from PyQt5.QtWidgets import *
from Main_student import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setStyleSheet('''#MainWindow{border-image: url(./images/background.png)}''')

        # 自定义槽与clicked信号
        self.student_update_button.clicked.connect(self.succeed_choose_course) # 确认选课按钮
        self.student_back.clicked.connect(self.main_student_to_login) # 返回按钮
        self.update_information.clicked.connect(self.statistics_course_student) # 更新选课版信息
        self.student_find_button.clicked.connect(self.display_information) #查询按钮

        # 初始化学生选课表格
        db = pymysql.connect("localhost", "root", "clf20001212", "management_system")
        cursor = db.cursor()
        # 获取当前操作账户并清空表now_account
        try:
            sql = "select *from now_account"
            cursor.execute(sql)
            self.user = cursor.fetchone()
            sql = "update now_account set now_account='' "
            cursor.execute(sql)
            db.commit()
        except:
            print(31)
        # 获取教务预设的课程
        try:
            sql = "select *from schedule"
            cursor.execute(sql)
            info_schedule = cursor.fetchall()
        except:
            print(33)
        # 创建一个列表courses，存放教务预设的课程
        courses = []
        for i in range(0, len(info_schedule)):
            if info_schedule[i][-1] != '':
                courses.append(info_schedule[i][-1])
        # 设置学生选课表格的行数
        self.student_setcourse_tableWidget.setRowCount(len(courses))
        # 设置学生选课表格垂直表头标签
        labels = []
        for i in range(0, len(courses)):
            labels.append(str(i+1))
        self.student_setcourse_tableWidget.setVerticalHeaderLabels(labels)
        # 设置表格水平方向自适应
        self.student_setcourse_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 为学生选课表格的每一行的第一列创建复选框checkbox
        for i in range(0, len(courses)):
            checkbox = QCheckBox()
            # 设置复选框初始状态为未选中
            checkbox.setChecked(False)
            # 为复选框重新命名
            checkbox.setObjectName(str(i))
            # 将复选框添加到学生选课表格中
            self.student_setcourse_tableWidget.setCellWidget(i, 0, checkbox)
        # 为学生选课表格每一行的第二列初始化教务设置的课程
        for i in range(0, len(courses)):
            item = QTableWidgetItem(courses[i])
            self.student_setcourse_tableWidget.setItem(i, 1, item)
        # 将学生选课表格设置为禁止编辑
        self.student_setcourse_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 初始化学生选课版表格信息
        # 设置水平标题栏和列数
        try:
            self.student_display_tableWidget.setColumnCount(len(courses))
            self.student_display_tableWidget.setHorizontalHeaderLabels(courses)
        except:
            print(67)
        # 将表格设置为禁止编辑
        self.student_display_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 水平方向自适应
        self.student_display_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        cursor.close()
        db.close()

    # 学生选课成功，将学生信息录入模块
    def succeed_choose_course(self):
        db = pymysql.connect("localhost", "root", "clf20001212", "management_system")
        cursor = db.cursor()
        # 获取教务预设的课程
        try:
            sql = "select *from schedule"
            cursor.execute(sql)
            info_schedule = cursor.fetchall()
        except:
            print(86)
        # 创建一个列表courses，存放教务预设的课程
        courses = []
        for i in range(0, len(info_schedule)):
            if info_schedule[i][-1] != '':
                courses.append(info_schedule[i][-1])
        # 若没有选择班级，则提示"请先选择班级"
        if self.stu_set_class_comboBox.currentText() == '':
            QMessageBox.information(self, "提示", "请先选择班级")
        else:
            # 若所有复选框都没被选择，则提示"请至少选择一门课程"
            flag = False
            for i in range(0, len(courses)):
                if self.findChild(QCheckBox, str(i)).isChecked() == True:
                    flag = True
                    break
            if not flag:
                QMessageBox.information(self, "提示", "请至少选择一门课程")
            else:
                # 将学生选择的班级和课程录入表student_account的中的class字段和course字段中
                # 查找当前账户
                # 录入学生班级
                try:
                    sql = 'update student_account set class=%s where account=%s'
                    data = (self.stu_set_class_comboBox.currentText(), self.user[0])
                    cursor.execute(sql, data)
                    db.commit()
                except:
                    print(118)
                # 录入学生选择的课程
                # 创建一个空字符串stu_courses存储这个学生选择的所有课程
                stu_courses = ""
                for i in range(0, len(courses)):
                    if self.findChild(QCheckBox, str(i)).isChecked() == True:
                        stu_courses = stu_courses + courses[i] + ';'
                try:
                    sql = 'update student_account set course=%s where account=%s'
                    data = (stu_courses, self.user[0])
                    cursor.execute(sql, data)
                    db.commit()
                except:
                    print(133)
                # 提示选课成功
                QMessageBox.information(self, "提示", "选课成功")

        cursor.close()
        db.close()

    # 学生界面选课版,点击刷新按钮，统计选课情况
    def statistics_course_student(self):
        # 存储人数
        num = []
        total_num = []
        db = pymysql.connect("localhost", "root", "clf20001212", "management_system")
        cursor = db.cursor()

        # 重新设置后,点击更新按钮，统计版的标题头应该被刷新
        try:
            sql = "select *from schedule"
            cursor.execute(sql)
            info_schedule = cursor.fetchall()
        except:
            print(112)
        try:
            courses = []
            for i in range(0, len(info_schedule)):
                if info_schedule[i][-1] != '':
                    courses.append(info_schedule[i][-1])
            # 设置表格列数
            self.student_display_tableWidget.setColumnCount(len(courses))
            # 设置表格水平表头标签，即教务设置的课程名
            self.student_display_tableWidget.setHorizontalHeaderLabels(courses)
        except:
            print(132)

        # 用i遍历不同的班
        for i in range(0, 4):
            try:
                sql = "select *from student_account where class=%s"
                cursor.execute(sql, str(i + 1) + '班')
                info = cursor.fetchall()
                if info is not None:
                    # 创建一个列表counts,存储该班每门课对应人数
                    counts = []
                    # 为每门课初始人数赋值为0
                    for k in range(0, len(courses)):
                        counts.append(0)
                    # 用j遍历同班中每个人的course字段内容
                    for j in range(0, len(info)):
                        # 用k遍历courses列表中的课，即教务预设的课
                        for k in range(0, len(courses)):
                            # 使用正则表达式检索course字段中的内容，发现这门课在该字符串中，则这门课的人数加一
                            if re.search(courses[k], info[j][-1]) is not None:
                                counts[k] = counts[k] + 1
                    for k in range(0, len(courses)):
                        num.append(counts[k])
            except:
                print(192)

        # 统计各课程总人数
        for col in range(0, len(courses)):
            # count用于存储每个课程的总人数
            count = 0
            for row in range(0, 4):
                count = count + num[row * len(courses) + col]
            total_num.append(count)

        # 将统计好的各班各课程人数显示在选课版的表格上
        for row in range(0, 5):
            for col in range(0, len(courses)):
                if row == 4:
                    item = QTableWidgetItem(str(total_num[col]))
                    self.student_display_tableWidget.setItem(row, col, item)
                else:
                    item = QTableWidgetItem(str(num[len(courses) * row + col]))
                    self.student_display_tableWidget.setItem(row, col, item)
        cursor.close()
        db.close()

    # 学生查询模块
    def display_information(self):
        db = pymysql.connect('localhost', 'root', 'clf20001212', 'management_system')
        cursor = db.cursor()

        # 每次点击查询按钮都要清空之前的内容
        self.display_student_information.clear()

        # 获取该账户所有信息
        try:
            sql = "select *from student_account where account = %s"
            cursor.execute(sql, self.user[0])
            info_user = cursor.fetchone()
        except:
            print(257)

        # 显示所选班级
        if info_user[2] is None:
            self.display_student_information.append("班级:未选")
            self.display_student_information.ensureCursorVisible()
            self.display_student_information.append(" ")
            self.display_student_information.ensureCursorVisible()
        else:
            self.display_student_information.append("班级:" + info_user[2])
            self.display_student_information.ensureCursorVisible()
            self.display_student_information.append(" ")
            self.display_student_information.ensureCursorVisible()
        # 显示所选课程
        if info_user[-1] is None:
            self.display_student_information.append("未选一门课程")
        else:
            self.display_student_information.append("已选课程:")
            self.display_student_information.ensureCursorVisible()
            self.display_student_information.append(info_user[-1])


        cursor.close()
        db.close()

    # 学生选课界面返回按钮,跳转回登录界面
    def main_student_to_login(self):
        from runlogin import Login

        self.close()
        self.login = Login()
        self.login.show()


