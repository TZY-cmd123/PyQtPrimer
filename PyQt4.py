#QMessageBox槽函数,弹出交流框
import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton,QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_messagebox)      # 1实例化一个QPushButton并将clicked信号与自定义的show_messagebox槽函数连接起来，这样点击按钮后，信号发出，槽函数就会启动；

    def show_messagebox(self):
        choice = QMessageBox.information(self, 'Title', 'Content',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  #使用QMessageBox.Ok.Yes.No.Close.Cancel.Open.Save
                                                                                       #中间用|连接
        #按键按下后就会消失对话框
        #弹出含有三个选项的对话框

        #除了QMessageBox.information，还有QMessageBox.question，QMessageBox.warning，QMessageBox.critical，QMessageBox.about等对话框，用法类似



        #根据获得的输入进行判断
        if choice == QMessageBox.Yes:  # 2
            print("按下了yes")
        elif choice == QMessageBox.No:  # 4
            print("按下了no")
        elif choice == QMessageBox.Cancel:
            print("按下了cancel")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    demo.resize(300,300)
    sys.exit(app.exec_())
