import cv2
import time
import tkinter as tk
from tkinter import filedialog

from faced.detector import FaceDetector
from faced.utils import annotate_image

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from FacedDetetor import Ui_MainWindow

class mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None) :
        super(mainwindow,self).__init__(parent)
        self.setupUi(self)


        self.btn_pic.clicked.connect(self.pic)
        self.btn_camare.clicked.connect(self.camare)
        self.btn_video.clicked.connect(self.video)

    def  pic(self):
        '''打开选择文件夹对话框'''
        root = tk.Tk()
        root.withdraw()
        Filepath = filedialog.askopenfilename() #获得选择好的文件
        print(Filepath)

        face_detector = FaceDetector()
        img = cv2.imread(Filepath)
        rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

        # Receives RGB numpy image (HxWxC) and
        # returns (x_center, y_center, width, height, prob) tuples. 
        bboxes = face_detector.predict(rgb_img,thresh=0.85)

        # 实验 utils 的函数来画框
        ann_img = annotate_image(img, bboxes)

        #保存图片
        cv2.imwrite("output.png", ann_img)

        # Show the image展示图片
        cv2.imshow('image',ann_img)
        cv2.waitKey(0)
        #cv2.destroyAllWindows()

    def  video(self):
        '''打开选择文件夹对话框'''
        root = tk.Tk()
        root.withdraw()
        #Folderpath = filedialog.askdirectory() #获得选择好的文件夹
        Filepath = filedialog.askopenfilename() #获得选择好的文件

        face_detector = FaceDetector()
        cap = cv2.VideoCapture(Filepath)        #通过路径找到视频

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
        fps = cap.get(cv2.CAP_PROP_FPS) # float

        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter("output.avi",fourcc, fps, (int(width), int(height)))

        now = time.time()
        while True:
            now = time.time()
            # Capture frame-by-frame
            ret, frame = cap.read()          #读入视频画面

            # if frame.shape[0] == 0:
            #     # cap.release()
            #     # cv2.destroyAllWindows()
            #     break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    #灰度处理

            bboxes = face_detector.predict(rgb_frame)             #画框

            ann_frame = annotate_image(frame, bboxes)             #组合

            out.write(frame)                                      #输出

            cv2.imshow('Show-Window(Press Q to exit)', ann_frame) #显示
            print("FPS: {:0.2f}".format(1 / (time.time() - now)), end="\r", flush=True)
            if cv2.waitKey(1) & 0xFF == ord('q'):   #按q退出
                break
        cap.release()
        cv2.destroyAllWindows()

    def  camare(self):
        face_detector = FaceDetector()
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)          #打开内置摄像头

        while cap.isOpened():
            # Capture frame-by-frame
            ret, frame = cap.read()                      #读入画面

            if frame.shape[0] == 0:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            bboxes = face_detector.predict(rgb_frame)

            ann_frame = annotate_image(frame, bboxes)        #画框组合

            cv2.imshow('Camera-Window(Press Q to exit)', ann_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        