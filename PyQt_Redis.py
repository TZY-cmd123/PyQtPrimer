#1.通过按钮来改变文本
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import redis
import datetime
import time
import easygui
import cx_Oracle
import pymongo
import pymysql


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.v_layout = QVBoxLayout()
        self.button = QPushButton('User1', self)
        self.button1 = QPushButton('User2', self)
        self.button2 = QPushButton('User3', self)
        self.button_show = QPushButton('展示', self)
        self.button.clicked.connect(self.Mytest1)
        self.button1.clicked.connect(self.Mytest2)
        self.button2.clicked.connect(self.Mytest3)
        self.button_show.clicked.connect(self.Mytest_show)
        self.MyRedis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.MyRedis.set("User1","0")
        self.MyRedis.set("User2","0")
        self.MyRedis.set("User3","0")
        # self.MyRedis.hset("User1_time","User1",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        # self.MyRedis.hset("User2_time","User2",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        # self.MyRedis.hset("User3_time","User3",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.MyRedis.lpush("Click_Time",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.MyRedis.sadd("Click_Time_Hour", datetime.datetime.now().strftime('%H'))
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.button_show)
        self.setLayout(self.v_layout)
    def Mytest1(self):
        self.MyRedis.incr("User1")
        self.MyRedis.hset("User1_time","User1",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.MyRedis.lpush("Click_Time",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.MyRedis.sadd("Click_Time_Hour", datetime.datetime.now().strftime('%H'))

    def Mytest2(self):
        self.MyRedis.incr("User2")
        self.MyRedis.hset("User1_time","User1",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.MyRedis.lpush("Click_Time",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.MyRedis.sadd("Click_Time_Hour", datetime.datetime.now().strftime('%H'))

    def Mytest3(self):
        self.MyRedis.incr("User3")
        self.MyRedis.hset("User1_time","User1",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.MyRedis.lpush("Click_Time",datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.MyRedis.sadd("Click_Time_Hour", datetime.datetime.now().strftime('%H'))

    def Mytest_show(self):
        print("-------------------------------------------------------")
        print("User1相关信息:")
        print(self.MyRedis.get("User1"))
        print(self.MyRedis.hgetall("User1_time"))
        print("User2相关信息:")
        print(self.MyRedis.get("User2"))
        print(self.MyRedis.hgetall("User2_time"))
        print("User3相关信息:")
        print(self.MyRedis.get("User2"))
        print(self.MyRedis.hgetall("User2_time"))
        print("点击时间")
        print(self.MyRedis.lrange('Click_Time', 0, -1))
        print("点击时间(小时)")
        print(self.MyRedis.smembers("Click_Time_Hour"))
        print("-------------------------------------------------------")
        self.MyRedis.close()


if __name__ == '__main__':
    print(cx_Oracle.__version__)
    print(redis.__version__)
    app = QApplication(sys.argv)
    demo = Demo()
    demo.resize(200,200)
    demo.setWindowTitle('Redis_Demo')
    demo.show()
    sys.exit(app.exec_())