#基础布局，用到了垂直和水平
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton


#首先把各个组件设置好最后组合

class LabelDemo(QWidget):  # 标签的布局
    def __init__(self):
        super(LabelDemo, self).__init__()
        self.label_layout = QVBoxLayout()
        self.user_label = QLabel("UserName:")
        self.password_label = QLabel("PassWord:")
        self.label_layout.addWidget(self.user_label)
        self.label_layout.addWidget(self.password_label)
        self.setLayout(self.label_layout)


class ButtonDemo(QWidget):
    def __init__(self):
        super(ButtonDemo, self).__init__()
        self.button_layout = QVBoxLayout()
        self.login = QPushButton("Login")
        self.logup = QPushButton("logup")
        self.button_layout.addWidget(self.login)
        self.button_layout.addWidget(self.logup)
        self.setLayout(self.button_layout)

class EditLineDemo(QWidget):
    def __init__(self):
        super(EditLineDemo, self).__init__()
        self.editline_layout = QVBoxLayout()
        self.login = QLineEdit()
        self.logup = QLineEdit()
        self.editline_layout.addWidget(self.login)
        self.editline_layout.addWidget(self.logup)
        self.setLayout(self.editline_layout)


# 设置布局，把组件放的好看一些


class MyDemo2(QWidget):

    def __init__(self):
        super(MyDemo2, self).__init__()

        self.demo_layout = QHBoxLayout()
        self.label_test=LabelDemo()
        self.button_test=ButtonDemo()
        self.editline_test=EditLineDemo()
        self.demo_layout.addWidget(self.label_test)
        self.demo_layout.addWidget(self.editline_test)
        self.demo_layout.addWidget(self.button_test)
        self.setLayout(self.demo_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MyDemo2()
    demo.setWindowTitle('设置标题')
    demo.show()
    sys.exit(app.exec_())
