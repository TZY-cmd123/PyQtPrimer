'''
信号与槽
在这里我把信号视作裁判鸣枪，而用于行动的槽函数则视作选手开跑，
当裁判鸣枪后(即信号发出)，选手就开始往前跑(槽函数启动)。
PyQt5中各个对象间或各个对象自身就是通过信号与槽机制来相互通信的
'''

# 1.通过按钮来改变文本
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):  # 1该类继承QWidget，可以将QWidget看作是一种毛坯房，还没有装修，而我们往其中放入QPushButton、QLabel等控件就相当于在装修这间毛坯房。类似的毛坯房还有QMainWindow和QDialog，之后章节再讲述；
    my_signal = pyqtSignal()  # 自定义信号

    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)  # 2(相当于告诉程序这个QPushButton是放在QWidget这个房子中的)；
        self.button.pressed.connect(self.Mytest1)
        self.button.released.connect(self.Mytest2)
        self.button.clicked.connect(
            self.change_text)  # 3clicked(按钮被点击)是该控件的一个信号，所以通用的公式可以是：widget.signal.connect(slot)；
        self.button.clicked.connect(self.Mytest3)  # 同一个信号可以连接多个信号
        self.my_signal.connect(self.Mytest4)  # 发出自定义信号，将信号和指定方法相连接

    def mousePressEvent(self, QMouseEvent):  # 监视鼠标，如果按下就释放信号，重写指定方法
        self.my_signal.emit()  # 发送连接信号
        print("发生甚么事了")

    def change_text(self):
        print('change text')
        self.button.setText('Stop')  # 4
        self.button.clicked.disconnect(self.change_text)  # 5解绑，解绑后再按按钮你会发现控制台不会再输出，namely, We can't control the button after disconnect

    def Mytest1(self):
        print('压下去的操作')

    def Mytest2(self):
        print('松开的操作')  # 所以其实pressed和released两个连起来就是一个完整的clicked

    def Mytest3(self):
        print('第二个信号')

    def Mytest4(self):
        print('鼠标信号')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.resize(300, 300)  # 设置长宽
    demo.setWindowTitle('可以在这里设置标题')
    demo.show()  # 7
    sys.exit(app.exec_())
