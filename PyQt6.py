import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.edit_label = QLabel('QTextEdit', self)#编辑框
        self.browser_label = QLabel('QTextBrowser', self)#输出框
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)

        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.text_browser)

        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)  # 1

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())  # 2


if __name__ == '__main__':
    #输出框会执行html代码，比如输入<font color='red'>Hello World</font>
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())