# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created: Wed Jun  1 00:58:05 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Window(object):

    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(1440, 900)
        Window.setMouseTracking(True)
        self.centralwidget = QtGui.QWidget(Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backBtn = QtGui.QPushButton(self.centralwidget)
        self.backBtn.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setBaseSize(QtCore.QSize(30, 30))
        self.backBtn.setMouseTracking(True)
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.horizontalLayout.addWidget(self.backBtn)
        self.editUrl = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editUrl.sizePolicy().hasHeightForWidth())
        self.editUrl.setSizePolicy(sizePolicy)
        self.editUrl.setObjectName(_fromUtf8("editUrl"))
        self.horizontalLayout.addWidget(self.editUrl)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_2.addWidget(self.webView)
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(_translate("Window", "MyBrowser", None))
        self.backBtn.setText(_translate("Window", "Back", None))

from PyQt4 import QtWebKit
