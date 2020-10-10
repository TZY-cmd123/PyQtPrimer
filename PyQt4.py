#QMessageBox槽函数,弹出交流框
import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton,QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
import face_recognition

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_messagebox)      # 1实例化一个QPushButton并将clicked信号与自定义的show_messagebox槽函数连接起来，这样点击按钮后，信号发出，槽函数就会启动；

    def show_messagebox(self):
        QMessageBox.information(self, 'Title', 'Content',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  #使用QMessageBox.Ok.Yes.No.Close.Cancel.Open.Save
                                                                                       #中间用|连接
        #除了QMessageBox.information，还有QMessageBox.question，QMessageBox.warning，QMessageBox.critical，QMessageBox.about



        #获得输入
        choice = QMessageBox.question(self, 'Change Text?', 'Would you like to change the button text?',
                                      QMessageBox.Yes | QMessageBox.No)  # 1
        #根据获得的输入进行判断
        if choice == QMessageBox.Yes:  # 2
            self.button.setText('Changed!')
        elif choice == QMessageBox.No:  # 4
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    demo.resize(300,300)
    sys.exit(app.exec_())
