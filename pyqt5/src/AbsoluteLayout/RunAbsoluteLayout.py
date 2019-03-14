import  sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSlot
from AbsoluteLayout import Ui_AbsolutelayoutDemo

class layoutDemo(QMainWindow,Ui_AbsolutelayoutDemo):
    '''
    class documenttation goes here
    '''
    def __init__(self,parent = None):
        """

        :param parent:
        """
        super(layoutDemo,self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton1_clicked(self):
        """
        pushButton1名字必须与ui界面上的名字一致
        slot documenttation goes here
        :return:
        """
        print("收益_min:",self.doubleSpinBox_returns_min.text())
        print("收益_max:",self.doubleSpinBox_returns_max.text())
        print("最小回撤_min:",self.doubleSpinBox_maxdrawdown_min.text())
        print("最大回撤_max:",self.doubleSpinBox_maxdrawdown_max.text())
        print("sharp比_min:",self.doubleSpinBox_sharp_min.text())
        print("sharp比_max:",self.doubleSpinBox_sharp_max.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = layoutDemo()
    ui.show()
    sys.exit(app.exec_())