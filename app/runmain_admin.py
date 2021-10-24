import pymysql
import re

from PyQt5.QtWidgets import *
from UI.main_admin.Main_admin import Ui_MainWindow


class MainAdmin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainAdmin, self).__init__()
        self.setupUi(self)

        self.setStyleSheet('''QWidget#MainWindow{border-image: url(./images/background.png)}''')

        # 信号与槽的绑定
        self.confirm_course_admin_button.clicked.connect(self.admin_set_course)
        self.update_admin_button.clicked.connect(self.admin_statistics)
        self.back_admin_button.clicked.connect(self.admin_to_login)
        self.admin_add_button.clicked.connect(self.add_course)
        self.admin_del_button.clicked.connect(self.delete_course)
        self.admin_reset_button.clicked.connect(self.reset_all)

        db = pymysql.connect("localhost", "akaduo", "akaduoadmin", "management_system")
        cursor = db.cursor()

        # 选课设置板块的初始化
        # 设置选课设置板块表格行数，即教务可设置几门课程
        try:
            sql = "select *from schedule"
            cursor.execute(sql)
            info_schedule = cursor.fetchall()
        except:
            print(33)
        self.admin_setcourse_tableWidget.setRowCount(len(info_schedule))
        # 设置垂直方向的表头标签
        labels = []
        for i in range(0, len(info_schedule)):
            labels.append("课程"+info_schedule[i][0])
        self.admin_setcourse_tableWidget.setVerticalHeaderLabels(labels)
        # 设置表格水平方向自适应
        self.admin_setcourse_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 为表格添加下拉组合框
        for i in range(0, len(info_schedule)):
            combobox = QComboBox()
            # 为每个下拉组合框预设四个默认可选选项并设置为可编辑,并且设置当前下标为-1
            combobox.addItems(['程设', '马原', '毛概', '邓论'])
            combobox.setEditable(True)
            combobox.setCurrentIndex(-1)
            # 为每个下拉组合框重新命名
            combobox.setObjectName(str(i))
            # 将每个下拉组合框添加到表格中
            self.admin_setcourse_tableWidget.setCellWidget(i, 0, combobox)
        # 如果教务之前已经设置过课程，则登录进教务界面时显示它们
        flag = False
        for i in range(0, len(info_schedule)):
            if info_schedule[i][-1] != '':
                flag = True
                break
        if flag:
            for i in range(0, len(info_schedule)):
                if info_schedule[i][-1] != '':
                    self.findChild(QComboBox, str(i)).setCurrentText(info_schedule[i][-1])

        # 初始化教务选课版信息
        try:
            courses = []
            for i in range(0, len(info_schedule)):
                if info_schedule[i][-1] != '':
                    courses.append(info_schedule[i][-1])
            # 设置表格列数
            self.admin_display_tableWidget.setColumnCount(len(courses))
            # 设置表格水平表头标签，即教务设置的课程名
            self.admin_display_tableWidget.setHorizontalHeaderLabels(courses)
        except:
            print(75)
        # 禁止table widget的编辑
        self.admin_display_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 水平方向自适应
        self.admin_display_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        cursor.close()
        db.close()

    # 教务界面的设置课程模块
    def admin_set_course(self):
        db = pymysql.connect("localhost", "akaduo", "akaduoadmin", "management_system")
        cursor = db.cursor()
        # 当教务按下选课设置页面的确定按钮时，student_account表中的course和class字段内容应该被清空
        try:
            sql = 'update student_account set course=null'
            cursor.execute(sql)
            sql = 'update student_account set class=null'
            cursor.execute(sql)
            db.commit()
        except:
            print(96)

        try:
            sql = 'select *from schedule'
            cursor.execute(sql)
            info_schedule = cursor.fetchall()
        except:
            print(103)
        # 获取当前下拉组合框中的课程名
        course_names = []
        for i in range(0, len(info_schedule)):
            course_names.append(self.findChild(QComboBox, str(i)).currentText())
        # 判断当前下拉组合框中的课程名是否至少有一门课程不为空
        flag = False
        for i in range(0, len(info_schedule)):
            if course_names[i] != '':
                flag = True
                break
        if not flag:
            QMessageBox.information(self, "提示", "至少设置一门课程")
        else:
            # 判断当前下拉组合框中的课程名是否重复
            flag = True
            for i in range(0, len(info_schedule)-1):
                for j in range(i+1, len(info_schedule)):
                    if course_names[i] == course_names[j] and course_names[i] != '' and course_names[j] != '':
                        flag = False
                        break
            if not flag:
               QMessageBox.information(self, "提示", "不能设置两门相同的课程")
            else:
                # 更新表schedule中的course字段内容
                for i in range(0, len(info_schedule)):
                    try:
                        sql = 'update schedule set course=%s where id=%s'
                        data = (course_names[i], str(i+1))
                        cursor.execute(sql, data)
                        db.commit()
                    except:
                        print(135)
                QMessageBox.information(self, "提示", "课程设置成功")
        cursor.close()
        db.close()

    # 教务界面的选课版模块
    def admin_statistics(self):
        # 存储人数
        num = []
        total_num = []
        db = pymysql.connect("localhost", "akaduo", "akaduoadmin", "management_system")
        cursor = db.cursor()

        # 重新设置后,点击更新按钮，统计版的标题头应该被刷新
        try:
            sql = "select *from schedule"
            cursor.execute(sql)
            info_schedule = cursor.fetchall()
        except:
            print(154)
        try:
            courses = []
            for i in range(0, len(info_schedule)):
                if info_schedule[i][-1] != '':
                    courses.append(info_schedule[i][-1])
            # 设置表格列数
            self.admin_display_tableWidget.setColumnCount(len(courses))
            # 设置表格水平表头标签，即教务设置的课程名
            self.admin_display_tableWidget.setHorizontalHeaderLabels(courses)
        except:
            print(165)

        # 用i遍历不同的班
        for i in range(0, 4):
            try:
                sql = "select *from student_account where class=%s"
                cursor.execute(sql, str(i+1)+'班')
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
                print(189)

        # 统计各课程总人数
        for col in range(0, len(courses)):
            # count用于存储每个课程的总人数
            count = 0
            for row in range(0, 4):
                count = count + num[row*len(courses)+col]
            total_num.append(count)

        # 将统计好的各班各课程人数显示在选课版的表格上
        for row in range(0, 5):
            for col in range(0, len(courses)):
                if row == 4:
                    item = QTableWidgetItem(str(total_num[col]))
                    self.admin_display_tableWidget.setItem(row, col, item)
                else:
                    item = QTableWidgetItem(str(num[len(courses)*row+col]))
                    self.admin_display_tableWidget.setItem(row, col, item)
        cursor.close()
        db.close()

    # 教务界面增加课程
    def add_course(self):
        # 在教务添加课程之前提示"请先保存未确认的课程，再添加课程"
        reply = QMessageBox.information(self, "提示", "请先保存未确认的课程，再添加课程", QMessageBox.Ok | QMessageBox.Cancel,
                                        QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            db = pymysql.connect("localhost", "akaduo", "akaduoadmin", "management_system")
            cursor = db.cursor()
            # 当教务按下增加课程按钮并选择Ok时，student_account表中的course和class字段内容应该被清空
            try:
                sql = 'update student_account set course=null'
                cursor.execute(sql)
                sql = 'update student_account set class=null'
                cursor.execute(sql)
                db.commit()
            except:
                print(227)

            # 获取添加课程之前已经有多少门课程
            try:
                sql = 'select *from schedule'
                cursor.execute(sql)
                info_schedule = cursor.fetchall()
            except:
                print(241)
            # 如果课程小于9门则可以继续添加,否则提示不能再添加更多课程
            if len(info_schedule) < 9:
                # 往表schedule插入一条记录
                try:
                    sql = 'insert into schedule(id, course) values(%s, %s)'
                    data = (str(len(info_schedule)+1), '')
                    cursor.execute(sql, data)
                    db.commit()
                except:
                    print(245)

                # 刷新教务界面设置课程的表格
                try:
                    sql = "select *from schedule"
                    cursor.execute(sql)
                    info_schedule = cursor.fetchall()
                except:
                    print(253)
                self.admin_setcourse_tableWidget.setRowCount(len(info_schedule))
                # 设置垂直方向的表头标签
                labels = []
                for i in range(0, len(info_schedule)):
                    labels.append("课程"+info_schedule[i][0])
                self.admin_setcourse_tableWidget.setVerticalHeaderLabels(labels)
                # 设置表格水平方向自适应
                self.admin_setcourse_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                # 为表格添加下拉组合框
                for i in range(0, len(info_schedule)):
                    combobox = QComboBox()
                    # 为每个下拉组合框预设四个默认可选选项并设置为可编辑,并且设置当前下标为-1
                    combobox.addItems(['程设', '马原', '毛概', '邓论'])
                    combobox.setEditable(True)
                    combobox.setCurrentIndex(-1)
                    # 为每个下拉组合框重新命名
                    combobox.setObjectName(str(i))
                    # 将每个下拉组合框添加到表格中
                    self.admin_setcourse_tableWidget.setCellWidget(i, 0, combobox)
                # 如果教务之前已经设置过课程，则登录进教务界面时显示它们
                flag = False
                for i in range(0, len(info_schedule)):
                    if info_schedule[i][-1] != '':
                        flag = True
                        break
                if flag:
                    for i in range(0, len(info_schedule)):
                        if info_schedule[i][-1] != '':
                            self.findChild(QComboBox, str(i)).setCurrentText(info_schedule[i][-1])
            else:
                QMessageBox.information(self, "提示", "添加课程已到上限")

            cursor.close()
            db.close()
    # 教务界面删除课程
    def delete_course(self):
        # 在教务添加课程之前提示"请先保存未确认的课程，再添加课程"
        reply = QMessageBox.information(self, "提示", "请先保存未确认的课程，再删除课程", QMessageBox.Ok | QMessageBox.Cancel
                                        , QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            db = pymysql.connect("localhost", "akaduo", "akaduoadmin", "management_system")
            cursor = db.cursor()
            # 当教务按下删除课程按钮并选择Ok时，student_account表中的course和class字段内容应该被清空
            try:
                sql = 'update student_account set course=null'
                cursor.execute(sql)
                sql = 'update student_account set class=null'
                cursor.execute(sql)
                db.commit()
            except:
                print(304)

            # 获取添加课程之前已经有多少门课程
            try:
                sql = 'select *from schedule'
                cursor.execute(sql)
                info_schedule = cursor.fetchall()
            except:
                print(264)
            # 如果之前的课程大于四门则可以删除，否则提示不能再继续删除
            if len(info_schedule) > 4:
                # 在表schedule中删除最后一条记录
                try:
                    sql = 'delete from schedule where id=%s'
                    cursor.execute(sql, len(info_schedule))
                    db.commit()
                except:
                    print(321)

                # 刷新教务界面设置课程的表格
                try:
                    sql = "select *from schedule"
                    cursor.execute(sql)
                    info_schedule = cursor.fetchall()
                except:
                    print(320)
                self.admin_setcourse_tableWidget.setRowCount(len(info_schedule))
                # 设置垂直方向的表头标签
                labels = []
                for i in range(0, len(info_schedule)):
                    labels.append("课程" + info_schedule[i][0])
                self.admin_setcourse_tableWidget.setVerticalHeaderLabels(labels)
                # 设置表格水平方向自适应
                self.admin_setcourse_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                # 为表格添加下拉组合框
                for i in range(0, len(info_schedule)):
                    combobox = QComboBox()
                    # 为每个下拉组合框预设四个默认可选选项并设置为可编辑,并且设置当前下标为-1
                    combobox.addItems(['程设', '马原', '毛概', '邓论'])
                    combobox.setEditable(True)
                    combobox.setCurrentIndex(-1)
                    # 为每个下拉组合框重新命名
                    combobox.setObjectName(str(i))
                    # 将每个下拉组合框添加到表格中
                    self.admin_setcourse_tableWidget.setCellWidget(i, 0, combobox)
                # 如果教务之前已经设置过课程，则登录进教务界面时显示它们
                flag = False
                for i in range(0, len(info_schedule)):
                    if info_schedule[i][-1] != '':
                        flag = True
                        break
                if flag:
                    for i in range(0, len(info_schedule)):
                        if info_schedule[i][-1] != '':
                            self.findChild(QComboBox, str(i)).setCurrentText(info_schedule[i][-1])
            else:
                QMessageBox.information(self, "提示", "不能再继续删除课程")

    # 教务界面重置按钮
    def reset_all(self):
        reply = QMessageBox.information(self, "提示", "将重置整个选课系统为初始状态!", QMessageBox.Yes | QMessageBox.No
                                        , QMessageBox.No)
        if reply == QMessageBox.Yes:
            db = pymysql.connect("localhost", "akaduo", "akaduoadmin", "management_system")
            cursor = db.cursor()
            # 清空表schedule的course字段，并删除id大于4的记录
            try:
                sql = 'select *from schedule'
                cursor.execute(sql)
                info_schedule = cursor.fetchall()
                if len(info_schedule) > 4:
                    for i in range(5, len(info_schedule)+1):
                        sql = 'delete from schedule where id=%s'
                        cursor.execute(sql, str(i))
                        db.commit()
                sql = 'update schedule set course=%s'
                cursor.execute(sql, '')
                db.commit()
            except:
                print(383)
            # 清空表student_account中的class和course字段
            try:
                sql = 'update student_account set class = null'
                cursor.execute(sql)
                sql = 'update student_account set course = null'
                cursor.execute(sql)
                db.commit()
            except:
                print(392)
            # 设置教务设置课程界面为初始状态
            # 选课设置板块的初始化
            # 设置选课设置板块表格行数，即教务可设置几门课程
            try:
                sql = "select *from schedule"
                cursor.execute(sql)
                info_schedule = cursor.fetchall()
            except:
                print(401)
            self.admin_setcourse_tableWidget.setRowCount(len(info_schedule))
            # 设置垂直方向的表头标签
            labels = []
            for i in range(0, len(info_schedule)):
                labels.append("课程" + info_schedule[i][0])
            self.admin_setcourse_tableWidget.setVerticalHeaderLabels(labels)
            # 设置表格水平方向自适应
            self.admin_setcourse_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            # 为表格添加下拉组合框
            for i in range(0, len(info_schedule)):
                combobox = QComboBox()
                # 为每个下拉组合框预设四个默认可选选项并设置为可编辑,并且设置当前下标为-1
                combobox.addItems(['程设', '马原', '毛概', '邓论'])
                combobox.setEditable(True)
                combobox.setCurrentIndex(-1)
                # 为每个下拉组合框重新命名
                combobox.setObjectName(str(i))
                # 将每个下拉组合框添加到表格中
                self.admin_setcourse_tableWidget.setCellWidget(i, 0, combobox)
            cursor.close()
            db.close()

    # 教务界面返回登录界面
    def admin_to_login(self):
        from runlogin import Login
        self.close()
        self.login = Login()
        self.login.show()

