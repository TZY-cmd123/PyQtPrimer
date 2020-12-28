#各种按钮以及按钮美化
import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolButton, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel

#按钮的选择性
class MyDemo(QWidget):
    def __init__(self):
        super(MyDemo, self).__init__()
        self.testbutton=QPushButton("测试按钮")
        self.test_button = QPushButton('Test', self)
        self.test_button.setCheckable(True)  # 1将按钮设置为可选中的，类似于多选框
        self.test_button.setIcon(QIcon('button.png'))  # 2设置图标图片
        self.test_button.toggled.connect(self.button_state_func)  # 3监听器
    def button_state_func(self):
        print(self.test_button.isChecked())



#单选按钮
class MyDemo2(QWidget):
    def __init__(self):
        super(MyDemo2, self).__init__()
        self.all_layout= QVBoxLayout()
        self.radio_layout=QHBoxLayout()
        self.on_radio=QRadioButton('on')
        self.off_radio=QRadioButton('off')
        self.off_radio.toggled.connect(self.on_off_bulb_func)      # 6

        self.radio_layout.addWidget(self.on_radio)
        self.radio_layout.addWidget(self.off_radio)
        self.label=QLabel()
        self.label.setPixmap(QPixmap('off.png'))                # 7

        self.all_layout.addWidget(self.label)
        self.all_layout.addLayout(self.radio_layout)
        self.setLayout(self.all_layout)

    def on_off_bulb_func(self):  # 8按钮触发的
        if self.off_radio.isChecked():
            self.label.setPixmap(QPixmap('off.png'))
        else:
            self.label.setPixmap(QPixmap('on.png'))






if __name__=='__main__':
    app = QApplication(sys.argv)
    demo = MyDemo2()
    demo.show()
    sys.exit(app.exec_())