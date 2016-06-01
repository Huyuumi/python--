import sys
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow
from Mainwindow import Ui_Window

defpath = "http://google.com"


class Window(QMainWindow, Ui_Window):

    load_end_sig = QtCore.pyqtSignal()
    backpath = defpath

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.editUrl.returnPressed.connect(self.seturl)
        self.backBtn.clicked.connect(self.urlback)
        self.webView.urlChanged.connect(self.UrlChanged)

    @QtCore.pyqtSlot()
    def urlback(self):
        self.webView.back()

    @QtCore.pyqtSlot()
    def seturl(self):
        if self.editUrl.text():
            url = self.editUrl.text()
        else:
            url = defpath
        self.webView.load(QtCore.QUrl(url))

    @QtCore.pyqtSlot()
    def UrlChanged(self):
        self.editUrl.setText(self.webView.url().toString())


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.seturl()
    app.exec_()

if __name__ == '__main__':
    main()
