#使用groupBox和toolbox组合一些组件
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout, QToolBox, QToolButton


class MyDemo(QWidget):
    def __init__(self):
        super(MyDemo, self).__init__()
        self.groupbox_1 = QGroupBox('On and Off', self)                       # 1这就是关键的groupbox用于放置radio
        self.groupbox_2 = QGroupBox('Change Color', self)

        self.red = QRadioButton('Red', self)                                  # 2
        self.blue = QRadioButton('Blue', self)
        self.green = QRadioButton('Green', self)
        self.yellow = QRadioButton('Yellow', self)
        self.color_list = [self.red, self.blue, self.green, self.yellow]

        self.on = QRadioButton('On', self)                                    # 3
        self.off = QRadioButton('Off', self)

        self.pic_label = QLabel(self)                                         # 4

        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.h1_layout.addWidget(self.on)
        self.h1_layout.addWidget(self.off)
        self.groupbox_1.setLayout(self.h1_layout)           # 通过放置布局来放置多个按钮等


        self.h2_layout.addWidget(self.red)
        self.h2_layout.addWidget(self.blue)
        self.h2_layout.addWidget(self.green)
        self.h2_layout.addWidget(self.yellow)
        self.groupbox_2.setLayout(self.h2_layout)

        self.h3_layout.addWidget(self.groupbox_1)
        self.h3_layout.addWidget(self.groupbox_2)

        self.all_v_layout.addWidget(self.pic_label)
        self.all_v_layout.addLayout(self.h3_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.yellow.setChecked(True)                                         # 5
        for btn in self.color_list:
            btn.clicked.connect(self.change_color_func)

        self.off.setChecked(True)                                            # 6
        self.off.toggled.connect(self.on_and_off_func)

    def label_init(self):                                                    # 7
        self.pic_label.setPixmap(QPixmap('images/Off.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)

    def change_color_func(self):
        if self.on.isChecked():
            path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))

    def on_and_off_func(self):
        if self.on.isChecked():
            path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))
        else:
            self.pic_label.setPixmap(QPixmap('images/Off.png'))







class Demo(QToolBox):                                           # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.groupbox_1 = QGroupBox(self)                       # 2
        self.groupbox_2 = QGroupBox(self)
        self.groupbox_3 = QGroupBox(self)

        self.toolbtn_f1 = QToolButton(self)                     # 3 抽屉按钮
        self.toolbtn_f2 = QToolButton(self)
        self.toolbtn_f3 = QToolButton(self)
        self.toolbtn_m1 = QToolButton(self)
        self.toolbtn_m2 = QToolButton(self)
        self.toolbtn_m3 = QToolButton(self)

        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()
        self.v3_layout = QVBoxLayout()

        self.addItem(self.groupbox_1, 'Couple One')             # 4
        self.addItem(self.groupbox_2, 'Couple Two')
        self.addItem(self.groupbox_3, 'Couple Three')
        self.currentChanged.connect(self.print_index_func)      # 5

        self.layout_init()
        self.groupbox_init()
        self.toolbtn_init()

    def layout_init(self):
        self.v1_layout.addWidget(self.toolbtn_f1)
        self.v1_layout.addWidget(self.toolbtn_m1)
        self.v2_layout.addWidget(self.toolbtn_f2)
        self.v2_layout.addWidget(self.toolbtn_m2)
        self.v3_layout.addWidget(self.toolbtn_f3)
        self.v3_layout.addWidget(self.toolbtn_m3)

    def groupbox_init(self):                                    # 6
        self.groupbox_1.setFlat(True)
        self.groupbox_2.setFlat(True)
        self.groupbox_3.setFlat(True)
        self.groupbox_1.setLayout(self.v1_layout)
        self.groupbox_2.setLayout(self.v2_layout)
        self.groupbox_3.setLayout(self.v3_layout)

    def toolbtn_init(self):                                     # 7关键在这
        self.toolbtn_f1.setIcon(QIcon('f1.ico'))
        self.toolbtn_f2.setIcon(QIcon('f1.ico'))
        self.toolbtn_f3.setIcon(QIcon('f1.ico'))
        self.toolbtn_m1.setIcon(QIcon('f1.ico'))
        self.toolbtn_m2.setIcon(QIcon('f1.ico'))
        self.toolbtn_m3.setIcon(QIcon('f1.ico'))

    def print_index_func(self):# 
        couple_dict = {
            0: 'Couple One',
            1: 'Couple Two',
            2: 'Couple Three'
        }
        sentence = 'You are looking at {}.'.format(couple_dict.get(self.currentIndex()))
        print(sentence)






#QToolBox即抽屉结构，这个十分重要


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())