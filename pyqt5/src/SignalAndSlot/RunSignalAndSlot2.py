import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSlot
from SignalAndSlot2 import Ui_Form

class myMainWidget(QMainWindow,Ui_Form):
    def __init__(self,parent = None):
        super(myMainWidget,self).__init__(parent)
        self.setupUi(self)
        self.label.setVisible(0)
        self.lineEdit.setText("checkBox 没被点击")

    @pyqtSlot(bool)
    def on_checkBox_clicked(self,checked):
        if self.checkBox.isChecked():
            self.label.setVisible(1)
            self.lineEdit.setText("checkBox 被点击")
            self.lineEdit.setVisible(1)
        else:
            self.label.setVisible(0)
            self.lineEdit.setText("checkBox 没被点击")
            self.lineEdit.setVisible(1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = myMainWidget()
    myWidget.show()
    sys.exit(app.exec_())