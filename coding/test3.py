import time

import sys
from PyQt5 import QtWidgets

from PyQt5.QtCore import QThread


# 装饰器，用于测量阻塞计时
def test_time(func1):
    def train(self):
        start_time = time.time()
        res = func1(self)
        end_time = time.time()
        print(end_time - start_time)
        # logger.info(f'the ocr parse time is {end_time-start_time} s')
        return res

    return train


class pictureOCR(QThread):
    """
    对图片进行ocr识别，，功能服务，可单独放一个文件
    """

    def __init__(self, *args, **kwargs):
        super(pictureOCR, self).__init__()

    @test_time
    def run(self):
        while True:
            time.sleep(2)  # 制造阻塞
            print('任务执行中')


class MainWindow(QtWidgets.QMainWindow):
    """pyqt主界面"""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # self.setupUi(self)
        self.resize(500, 300)

        self.p = pictureOCR()

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText('开始异步任务')
        self.pushButton.clicked.connect(self.click_event)

    def click_event(self):
        self.p.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
