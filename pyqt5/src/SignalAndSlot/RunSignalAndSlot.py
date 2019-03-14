import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from SignalAndSlot import Ui_Form

#下面这段代码每个dialog都需要
class myMainWidgetUi(QMainWindow,Ui_Form):
    def __init__(self,parent = None):
        super(myMainWidgetUi,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = myMainWidgetUi()
    myWin.show()
    sys.exit(app.exec_())
