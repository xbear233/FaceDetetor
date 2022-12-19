import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  ##忽略TensorFlow版本警告
import sys

from PyQt5.QtWidgets import QApplication
from UI_faced import *


if __name__ == "__main__":
    """main函数

    主程序由此运行
    """

    app =QApplication(sys.argv)   #  实例化一个app
    window = mainwindow()
    window.show()  #显示窗口

    try:
        sys.exit(app.exec())   #app退出
    except Exception as e:
        print(e)

