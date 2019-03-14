import sys
import horizontalLayoutMainWindow
import FourLayouts
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
   # mainWindow = QWidget()
   # ui = horizontalLayoutMainWindow.Ui_MainWindow()
    ui = FourLayouts.Ui_Form() #不需要传入参数
    #向主界面添加控件
    ui.setupUi(mainWindow)
    #显示主窗口
    mainWindow.show()
    #主程序循环
    sys.exit(app.exec_())

