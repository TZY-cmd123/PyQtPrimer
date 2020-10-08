import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout,QPushButton

# 设置布局，把组件放的好看一些
class Demo(QWidget):#继承毛胚房，把他当成界面

    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)#新建标签
        self.pwd_label = QLabel('Password:', self)#新建标签

        self.v_layout = QVBoxLayout()  # 1新建布局，实例化一个垂直布局管理器QVBoxLayout；同时设定布局的类型
        self.v_layout.addWidget(self.user_label)  # 2把组件放在布局里
        self.v_layout.addWidget(self.pwd_label)  # 3

        self.setLayout(self.v_layout)  # 4把布局放入Qwight里
        #总体思路: 新建组件，新建布局，把组件放入布局里，把布局放入类里

class MyDemo(QWidget):

    def __init__(self):
        super(MyDemo, self).__init__()
        self.My_Label = QLabel('Hello World', self)
        self.My_Line = QLineEdit(self)

        self.My_Layout = QHBoxLayout()
        self.My_Layout.addWidget(self.My_Label)
        self.My_Layout.addWidget(self.My_Line)

        self.setLayout(self.My_Layout)

class MyDemo2(QWidget):

    def __init__(self):
        super(MyDemo2, self).__init__()

        self.login = QLabel('登录', self)
        self.resigter = QLabel('注册',self)
        self.login_line = QLineEdit( self)
        self.resigter_line = QLineEdit(self)
        self.login_layout=QHBoxLayout()
        self.resigter_layout=QHBoxLayout()
        self.login_button=QPushButton('注册',self)
        self.resigter_button=QPushButton('登录',self)
        self.button_layout=QHBoxLayout()
        self.All_layout=QVBoxLayout()

        self.login_layout.addWidget(self.login)
        self.login_layout.addWidget(self.login_line)

        self.resigter_layout.addWidget(self.resigter)
        self.resigter_layout.addWidget(self.resigter_line)

        self.button_layout.addWidget(self.login_button)
        self.button_layout.addWidget(self.resigter_button)

        self.All_layout.addLayout(self.login_layout)
        self.All_layout.addLayout(self.resigter_layout)
        self.All_layout.addLayout(self.button_layout)



        self.setLayout(self.All_layout)
        #就这？


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MyDemo2()
    demo.show()
    sys.exit(app.exec_())
