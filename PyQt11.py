#液晶显示
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.lcd_1 = QLCDNumber(self)                                   # 1 液晶屏
        self.lcd_1.setDigitCount(10) #显示数字个数
        self.lcd_1.display(1234567890)

        self.lcd_2 = QLCDNumber(self)                                   # 2显示小数
        self.lcd_2.setSegmentStyle(QLCDNumber.Flat)
        # self.lcd_2.setSmallDecimalPoint(True)
        self.lcd_2.setDigitCount(10)
        self.lcd_2.display(0.123456789)

        self.lcd_3 = QLCDNumber(self)                                   # 3显示字符
        self.lcd_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcd_3.display('HELLO')


        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.lcd_1)
        self.v_layout.addWidget(self.lcd_2)
        self.v_layout.addWidget(self.lcd_3)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())