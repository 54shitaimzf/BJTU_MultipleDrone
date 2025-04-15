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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_ControlWindow(object):
    def setupUi(self, ControlWindow):
        if not ControlWindow.objectName():
            ControlWindow.setObjectName(u"ControlWindow")
        ControlWindow.resize(348, 529)
        self.centralwidget = QWidget(ControlWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setObjectName(u"leftLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.numDroneBox = QSpinBox(self.centralwidget)
        self.numDroneBox.setObjectName(u"numDroneBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.numDroneBox.sizePolicy().hasHeightForWidth())
        self.numDroneBox.setSizePolicy(sizePolicy1)
        self.numDroneBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.numDroneBox.setMinimum(1)
        self.numDroneBox.setMaximum(10)

        self.horizontalLayout_3.addWidget(self.numDroneBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.typeComboBox = QComboBox(self.centralwidget)
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.setObjectName(u"typeComboBox")

        self.horizontalLayout_3.addWidget(self.typeComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.generateSettingButton = QPushButton(self.centralwidget)
        self.generateSettingButton.setObjectName(u"generateSettingButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.generateSettingButton.sizePolicy().hasHeightForWidth())
        self.generateSettingButton.setSizePolicy(sizePolicy2)
        self.generateSettingButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.generateSettingButton)

        self.horizontalSpacer = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.leftLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.targetXBox = QSpinBox(self.centralwidget)
        self.targetXBox.setObjectName(u"targetXBox")
        self.targetXBox.setMinimum(-99)
        self.targetXBox.setValue(25)

        self.horizontalLayout.addWidget(self.targetXBox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.targetYBox = QSpinBox(self.centralwidget)
        self.targetYBox.setObjectName(u"targetYBox")

        self.horizontalLayout.addWidget(self.targetYBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.testControlButton = QPushButton(self.centralwidget)
        self.testControlButton.setObjectName(u"testControlButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.testControlButton.sizePolicy().hasHeightForWidth())
        self.testControlButton.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.testControlButton)

        self.startFlightButton = QPushButton(self.centralwidget)
        self.startFlightButton.setObjectName(u"startFlightButton")
        sizePolicy3.setHeightForWidth(self.startFlightButton.sizePolicy().hasHeightForWidth())
        self.startFlightButton.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.startFlightButton)

        self.stopFlightButton = QPushButton(self.centralwidget)
        self.stopFlightButton.setObjectName(u"stopFlightButton")
        sizePolicy3.setHeightForWidth(self.stopFlightButton.sizePolicy().hasHeightForWidth())
        self.stopFlightButton.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.stopFlightButton)


        self.leftLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.leftLayout)

        ControlWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlWindow)

        QMetaObject.connectSlotsByName(ControlWindow)
    # setupUi

    def retranslateUi(self, ControlWindow):
        ControlWindow.setWindowTitle(QCoreApplication.translate("ControlWindow", u"AirSim \u591a\u65e0\u4eba\u673a\u98de\u884c\u4eff\u771f\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("ControlWindow", u"\u65e0\u4eba\u673a\u6570\u76ee", None))
        self.label_4.setText(QCoreApplication.translate("ControlWindow", u"\u521d\u59cb\u4f4d\u7f6e\u7c7b\u578b", None))
        self.typeComboBox.setItemText(0, QCoreApplication.translate("ControlWindow", u"\u5706\u5f62", None))
        self.typeComboBox.setItemText(1, QCoreApplication.translate("ControlWindow", u"\u65b9\u5f62", None))
        self.typeComboBox.setItemText(2, QCoreApplication.translate("ControlWindow", u"\u7ebf\u5f62", None))

        self.generateSettingButton.setText(QCoreApplication.translate("ControlWindow", u"\u751f\u6210\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("ControlWindow", u"\u76ee\u6807X\u5750\u6807", None))
        self.label_2.setText(QCoreApplication.translate("ControlWindow", u"\u76ee\u6807Y\u5750\u6807", None))
        self.testControlButton.setText(QCoreApplication.translate("ControlWindow", u"\u98de\u884c\u76d1\u89c6", None))
        self.startFlightButton.setText(QCoreApplication.translate("ControlWindow", u"\u5f00\u59cb\u98de\u884c", None))
        self.stopFlightButton.setText(QCoreApplication.translate("ControlWindow", u"\u505c\u6b62\u98de\u884c", None))
    # retranslateUi

