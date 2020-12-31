# 增加了格子布局
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QGridLayout
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton,QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
import pymysql
class MyDemo2(QWidget):

    def __init__(self):
        super(MyDemo2, self).__init__()
        self.resize(300, 100)

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()  # 格子布局
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)

        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        # 以下是虚化效果
        self.user_line.setPlaceholderText('Please enter your username')
        self.pwd_line.setPlaceholderText('Please enter your password')

        # 初始时设置为不可用的
        self.login_button.setEnabled(False)
        self.signin_button.setEnabled(False)

        # 在用户输入账号密码和账号后才能按按钮,这里需要自定义槽函数
        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

        #绑定登录判定接口
        self.login_button.clicked.connect(self.login_check)



    def check_input_func(self):
        if self.user_line.text() == "" or self.pwd_line.text() == "":
            self.login_button.setEnabled(False)
            self.signin_button.setEnabled(False)
        else:
            self.login_button.setEnabled(True)
            self.signin_button.setEnabled(True)

    def login_check(self):#验证登录成功与否
        conn = pymysql.connect(host="cdb-l1c6g0ne.bj.tencentcdb.com", port=10166,user="root", passwd="tzyTZY123", db='AndroidUser')
        cur = conn.cursor()
        cur.execute("SELECT PassWord FROM android_user where UserName=%s",(self.user_line.text()))#试行操作
        for r in cur:
            print(r)

        if self.pwd_line.text()=='123':
            choice = QMessageBox.information(self, '成功', '登录成功',
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # 使用QMessageBox.Ok.Yes.No.Close.Cancel.Open.Save
            # 中间用|连接
        else:
            choice = QMessageBox.critical(self, '失败', '登录失败',
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        cur.close()
        conn.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MyDemo2()
    demo.setWindowTitle('设置标题')
    demo.show()
    sys.exit(app.exec_())
