# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
                               QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

from ui.VedioThread import OpenGLVideoWidget, VideoThread


class Ui_ControlWindow(object):
    def setupUi(self, ControlWindow):
        if not ControlWindow.objectName():
            ControlWindow.setObjectName(u"ControlWindow")
        ControlWindow.resize(771, 556)
        self.centralwidget = QWidget(ControlWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setObjectName(u"leftLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.numDroneBox = QSpinBox(self.centralwidget)
        self.numDroneBox.setObjectName(u"numDroneBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numDroneBox.sizePolicy().hasHeightForWidth())
        self.numDroneBox.setSizePolicy(sizePolicy)
        self.numDroneBox.setMinimum(1)
        self.numDroneBox.setMaximum(10)

        self.verticalLayout.addWidget(self.numDroneBox)

        self.generateSettingButton = QPushButton(self.centralwidget)
        self.generateSettingButton.setObjectName(u"generateSettingButton")
        sizePolicy.setHeightForWidth(self.generateSettingButton.sizePolicy().hasHeightForWidth())
        self.generateSettingButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.generateSettingButton)

        self.leftLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.testControlButton = QPushButton(self.centralwidget)
        self.testControlButton.setObjectName(u"testControlButton")
        sizePolicy.setHeightForWidth(self.testControlButton.sizePolicy().hasHeightForWidth())
        self.testControlButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.testControlButton)

        self.startFlightButton = QPushButton(self.centralwidget)
        self.startFlightButton.setObjectName(u"startFlightButton")
        sizePolicy.setHeightForWidth(self.startFlightButton.sizePolicy().hasHeightForWidth())
        self.startFlightButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.startFlightButton)

        self.stopFlightButton = QPushButton(self.centralwidget)
        self.stopFlightButton.setObjectName(u"stopFlightButton")
        sizePolicy.setHeightForWidth(self.stopFlightButton.sizePolicy().hasHeightForWidth())
        self.stopFlightButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.stopFlightButton)

        self.leftLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.addLayout(self.leftLayout)

        self.displayLayout = QVBoxLayout()
        self.displayLayout.setObjectName(u"displayLayout")

        # 接收airsim视频流的opengl控件
        print("绑定opengl控件")
        self.openGLWidget = OpenGLVideoWidget()
        self.displayLayout.replaceWidget(self.findChild(QOpenGLWidget), self.openGLWidget)

        # 初始化视频线程
        print("绑定视频流")
        self.video_thread = VideoThread()
        self.video_thread.frame_signal.connect(self.openGLWidget.update_frame)
        # 启动线程
        if not self.video_thread.isRunning():
            self.video_thread.start()

        # # 绑定按钮事件
        self.startFlightButton.clicked.connect(self.startFlight)
        # self.stopFlightButton.clicked.connect(self.stop_video_stream)
        #

        self.displayLayout.addWidget(self.openGLWidget)

        self.horizontalLayout_2.addLayout(self.displayLayout)

        ControlWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlWindow)

        QMetaObject.connectSlotsByName(ControlWindow)

    # setupUi

    def startFlight(self):
        import MultipleDrones

    def retranslateUi(self, ControlWindow):
        ControlWindow.setWindowTitle(QCoreApplication.translate("ControlWindow",
                                                                u"AirSim \u591a\u65e0\u4eba\u673a\u98de\u884c\u4eff\u771f\u7cfb\u7edf",
                                                                None))
        self.generateSettingButton.setText(
            QCoreApplication.translate("ControlWindow", u"\u751f\u6210\u8bbe\u7f6e", None))
        self.testControlButton.setText(QCoreApplication.translate("ControlWindow", u"\u6d4b\u8bd5\u8fde\u63a5", None))
        self.startFlightButton.setText(QCoreApplication.translate("ControlWindow", u"\u5f00\u59cb\u98de\u884c", None))
        self.stopFlightButton.setText(QCoreApplication.translate("ControlWindow", u"\u505c\u6b62\u98de\u884c", None))
    # retranslateUi
