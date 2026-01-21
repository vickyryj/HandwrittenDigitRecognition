# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from imgProcess import *



class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.timer_video = QtCore.QTimer()
        self.setupUi(self)
        self.init_logo()
        self.init_slots()
        self.cap = cv2.VideoCapture()
        self.out = None
        # self.out = cv2.VideoWriter('prediction.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setStyleSheet("#MainWindow{background-color: #f2f6fe}")
        self.widget_menu = QtWidgets.QWidget(MainWindow)
        self.widget_menu.setObjectName("widget_menu")
        self.widget_menu.setGeometry(QtCore.QRect(0, 0, 1440, 80))
        self.widget_menu.setStyleSheet("QWidget{background-color:#368ae2;border:0px solid balck;}")
        self.menuLayout = QtWidgets.QHBoxLayout(self.widget_menu)
        #logo
        label1 = QLabel(self.widget_menu)  # 创建一个标签控件
        label1.setGeometry(15, 10, 70, 60)  # 设置标签控件的位置和大小
        image_path = "./imgs/logo_white_mini.png"  # 图片的路径
        pixmap = QPixmap(image_path)  # 创建一个QPixmap对象并加载图片
        label1.setPixmap(pixmap)  # 在标签控件中显示图片
        label1.setScaledContents (True)
        #标题
        self.title = QLabel('''<font color=white face='黑体' size=16>| 手写数字识别系统<font>''',self.widget_menu)  # 创建一个标签控件
        self.title.setGeometry(95, 10, 300, 60)  # 设置标签控件的位置和大小
        #self.title.setStyleSheet('border-width: 1px;border-style: solid;''border - color: rgb(255, 170, 0);''background - color: rgb(100, 149, 237);')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1440, 820))
        #self.centralwidget.setStyleSheet('''QWidget{background-color:#66CCFF;}''')
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setSpacing(80)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_img = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_img.sizePolicy().hasHeightForWidth())
        self.pushButton_img.setSizePolicy(sizePolicy)
        self.pushButton_img.setMinimumSize(QtCore.QSize(150, 100))
        self.pushButton_img.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton_img.setFont(font)
        self.pushButton_img.setObjectName("pushButton_img")
        self.pushButton_img.setStyleSheet("QPushButton{color:white;font-size:20px;}"
                                  "QPushButton:hover{cursor:pointer;transform: scale(1.2);}"
                                  "QPushButton{background-color:#368ae2;}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
        self.verticalLayout.addWidget(
            self.pushButton_img, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_camera.sizePolicy().hasHeightForWidth())
        self.pushButton_camera.setSizePolicy(sizePolicy)
        self.pushButton_camera.setMinimumSize(QtCore.QSize(150, 100))
        self.pushButton_camera.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton_camera.setFont(font)
        self.pushButton_camera.setObjectName("pushButton_camera")
        self.pushButton_camera.setStyleSheet("QPushButton{color:white;font-size:20px;}"
                                  "QPushButton:hover{cursor:pointer;transform: scale(1.2);}"
                                  "QPushButton{background-color:#368ae2;}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
        self.verticalLayout.addWidget(
            self.pushButton_camera, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel('''<font color=blue face='黑体' size=16>说明<font>''',self.centralwidget)
        self.label.setObjectName("label")
        
        #展示图片和说明的样式
        #self.label.setGeometry(0, 90, 1000, 820)
        self.label.setStyleSheet("QLabel{background:white;margin:90px 10px 0 -10px;border-radius:10px;box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);color:red;}")
        self.label.setText("hello")
        #self.content = QLabel('''<font color=blue face='黑体' size=16>说明<font>''',self.label) 
        #self.content.setGeometry(10, 90, 300, 60)
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        #self.label.setGeometry(QtCore.QRect(300, 100, 600, 800))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 100, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "手写数字串识别系统"))
        #self.widget_menu.setText(_translate("MainWindow", "重庆理工大学"))
        
        self.pushButton_img.setText(_translate("MainWindow", "图片"))
        self.pushButton_camera.setText(_translate("MainWindow", "摄像头"))
        # self.pushButton_video.setText(_translate("MainWindow", "视频检测"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        

    def init_slots(self):
        self.pushButton_img.clicked.connect(self.button_image_open)
        # self.pushButton_video.clicked.connect(self.button_video_open)
        self.pushButton_camera.clicked.connect(self.button_camera_open)
        self.timer_video.timeout.connect(self.show_video_frame)

    def init_logo(self):
        pix = QtGui.QPixmap('./imgs/shuoMing0.png')
        self.label.setScaledContents(True)
        self.label.setPixmap(pix)

    def button_image_open(self):
        print('button_image_open')
        name_list = []

        img_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "打开图片", "", "*.png;;*.jpg;;All Files(*)")
        if not img_name:
            return

        img = cv2.imread(img_name)
        print(img_name)
        showimg = img
        
        # borders = findBorderContours(showimg)
        borders = findBorderHistogram(showimg)
        imgData = transMNIST(showimg, borders)
        results = predict(imgData)
        showimg = showResults(showimg, borders, results)

        
        cv2.imwrite('prediction.jpg', showimg)
        self.result = cv2.cvtColor(showimg, cv2.COLOR_BGR2BGRA)
        self.result = cv2.resize(
            self.result, (640, 480), interpolation=cv2.INTER_AREA)
        #new_dimension = (self.result.shape[1], pic_height)
        self.QtImg = QtGui.QImage(
            self.result.data, self.result.shape[1], self.result.shape[0], QtGui.QImage.Format_RGB32)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
        self.label.setContentsMargins(-10,90,0,0) #left、top、right、bottom

    def button_video_open(self):
        video_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "打开视频", "", "*.mp4;;*.avi;;All Files(*)")

        if not video_name:
            return

        flag = self.cap.open(video_name)
        if flag == False:
            QtWidgets.QMessageBox.warning(
                self, u"Warning", u"打开视频失败", buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.out = cv2.VideoWriter('prediction.avi', cv2.VideoWriter_fourcc(
                *'MJPG'), 20, (int(self.cap.get(3)), int(self.cap.get(4))))
            self.timer_video.start(30)
            self.pushButton_video.setDisabled(True)
            self.pushButton_img.setDisabled(True)
            self.pushButton_camera.setDisabled(True)

    def button_camera_open(self):
        if not self.timer_video.isActive():
            # 默认使用第一个本地camera
            flag = self.cap.open(0)
            if flag == False:
                QtWidgets.QMessageBox.warning(
                    self, u"Warning", u"打开摄像头失败", buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.out = cv2.VideoWriter('prediction.avi', cv2.VideoWriter_fourcc(
                    *'MJPG'), 20, (int(self.cap.get(3)), int(self.cap.get(4))))
                self.timer_video.start(30)
                # self.pushButton_video.setDisabled(True)
                self.pushButton_img.setDisabled(True)
                self.pushButton_camera.setText("关闭摄像头")
        else:
            self.timer_video.stop()
            self.cap.release()
            self.out.release()
            self.label.clear()
            self.init_logo()
            #self.pushButton_video.setDisabled(False)
            self.pushButton_img.setDisabled(False)
            pix1 = QtGui.QPixmap('./prediction.jpg')
            self.label.setScaledContents(True)
            self.label.setPixmap(pix1)
            self.pushButton_camera.setText("摄像头检测")
    
    def show_video_frame(self):
        name_list = []

        flag, img = self.cap.read()
        if img is not None:
            # showimg = cv2.resize(img,(240,320))
            showimg = img
            borders = findBorderContours(showimg)
            # borders = findBorderHistogram(showimg)
            imgData = transMNIST(showimg, borders)
            results = predict(imgData)
            showimg = showResults(showimg, borders, results)

            self.out.write(showimg)
            show = cv2.resize(showimg, (640, 480))
            self.result = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                     QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))

        else:
            self.timer_video.stop()
            self.cap.release()
            self.out.release()
            self.label.clear()
            self.pushButton_video.setDisabled(False)
            self.pushButton_img.setDisabled(False)
            self.pushButton_camera.setDisabled(False)
            self.init_logo()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
