import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout

EMOTION = {  # 1 设置日期和心情的对应表
    '周一': '(╯°Д°)╯︵ ┻━┻',
    '周二': '(╯￣Д￣)╯╘═╛',
    '周三': '╭(￣▽￣)╯╧═╧',
    '周四': '_(:з」∠)_',
    '周五': '(๑•̀ㅂ•́) ✧',
    '周六': '( ˘ 3˘)♥',
    '周日': '(;′༎ຶД༎ຶ`)'
}


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1946, 2, 14))  # 2
        self.calendar.setMaximumDate(QDate(6666, 6, 6))  # 3 设置日历的范围
        # self.calendar.setDateRange(QDate(1946, 2, 14), QDate(6666, 6, 6))
        # self.calendar.setFirstDayOfWeek(Qt.Monday)                            # 4
        # self.calendar.setSelectedDate(QDate(1946, 2, 14))                     # 5
        self.calendar.setGridVisible(True)  # 6  显示日历
        self.calendar.clicked.connect(self.show_emotion_func)  # 6 点击日历时会触发信号

        print(self.calendar.minimumDate())  # 7
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate()) # 选择的天数

        self.label = QLabel(self)  # 8
        self.label.setAlignment(Qt.AlignCenter)

        weekday = self.calendar.selectedDate().toString('ddd')  # 9 获得周几，和系统语言相同
        self.label.setText(EMOTION[weekday])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)
        self.setWindowTitle('QCalendarWidget')

    def show_emotion_func(self):  # 10
        weekday = self.calendar.selectedDate().toString('ddd')#获得周几
        self.label.setText(EMOTION[weekday]) #设置字典


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())