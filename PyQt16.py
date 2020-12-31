# 获得鼠标坐标
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(200, 200)  # 1 变换大小
    widget.move(100, 100)  # 2 移动
    # widget.setGeometry(100, 100, 200, 200)   # 3 设置在客户区的位置
    widget.show()

    print('-----------------x(), y(), pos()-----------------')
    print(widget.x())
    print(widget.y())
    print(widget.pos())  # 左上角的坐标

    print('-----------------width(), height()-----------------')
    print(widget.width())
    print(widget.height())  # 长宽

    print('-----------------geometry().x(), geometry.y(), geometry()-----------------')
    print(widget.geometry().x())
    print(widget.geometry().y())
    print(widget.geometry()) # 在客户区的坐标

    print('-----------------geometry.width(), geometry().height()-----------------')
    print(widget.geometry().width())
    print(widget.geometry().height()) # 客户区，即界面中用户可以点击的位置，除了标题栏等

    print('-----------------frameGeometry().x(), frameGeometry().y(), frameGeometry(), '
          'frameGeometry().width(), frameGeometry().height()-----------------')
    print(widget.frameGeometry().x())
    print(widget.frameGeometry().y())
    print(widget.frameGeometry()) # 加上外框的位置信息
    print(widget.frameGeometry().width())
    print(widget.frameGeometry().height())

    sys.exit(app.exec_())
