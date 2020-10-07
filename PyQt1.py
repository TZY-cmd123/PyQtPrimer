import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 1想要创建应用必须先实例化一个QApplication，并将sys.argv作为参数传入；
    label = QLabel('Hello World') # 2创建Qlabel
    label1=QLabel('<font color="red">Hello</font> <h1>World</h1>')#可以用html语言来写
    label.show()                  # 3展示,通过调用show()方法使控件可见(默认是隐藏)；
    label1.show()
    sys.exit(app.exec())         # 4app.exec_()是执行应用，让应用开始运转循环，直到窗口关闭返回0给sys.exit()