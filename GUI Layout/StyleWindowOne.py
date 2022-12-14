# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bahls\Source\Repos\StyleTransferApp\GUI Layout\StyleWindowOne.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ArtWithMachineLearningLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(36)
        self.ArtWithMachineLearningLabel.setFont(font)
        self.ArtWithMachineLearningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ArtWithMachineLearningLabel.setObjectName("ArtWithMachineLearningLabel")
        self.verticalLayout_2.addWidget(self.ArtWithMachineLearningLabel)
        self.OriginalStyleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(36)
        self.OriginalStyleLabel.setFont(font)
        self.OriginalStyleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OriginalStyleLabel.setObjectName("OriginalStyleLabel")
        self.verticalLayout_2.addWidget(self.OriginalStyleLabel)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(426, 0))
        self.label_3.setMaximumSize(QtCore.QSize(426, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.LaMuseLabel = QtWidgets.QLabel(self.centralwidget)
        self.LaMuseLabel.setMinimumSize(QtCore.QSize(426, 0))
        self.LaMuseLabel.setMaximumSize(QtCore.QSize(426, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(24)
        self.LaMuseLabel.setFont(font)
        self.LaMuseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LaMuseLabel.setObjectName("LaMuseLabel")
        self.horizontalLayout_4.addWidget(self.LaMuseLabel)
        self.RainPrincessLabel = QtWidgets.QLabel(self.centralwidget)
        self.RainPrincessLabel.setMinimumSize(QtCore.QSize(426, 0))
        self.RainPrincessLabel.setMaximumSize(QtCore.QSize(426, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(24)
        self.RainPrincessLabel.setFont(font)
        self.RainPrincessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RainPrincessLabel.setObjectName("RainPrincessLabel")
        self.horizontalLayout_4.addWidget(self.RainPrincessLabel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(426, 0))
        self.label.setMaximumSize(QtCore.QSize(426, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView_Scream_Stylized_16 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_16.setMinimumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_16.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_16.setStyleSheet("border-image: url(:/Logo/Logos/index.png);")
        self.graphicsView_Scream_Stylized_16.setObjectName("graphicsView_Scream_Stylized_16")
        self.horizontalLayout.addWidget(self.graphicsView_Scream_Stylized_16)
        self.graphicsView_Scream_Stylized_18 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_18.setMinimumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_18.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_18.setStyleSheet("Border-image: url(:/Resized/Resized Pictures/La Muse - Resized.jpg)")
        self.graphicsView_Scream_Stylized_18.setObjectName("graphicsView_Scream_Stylized_18")
        self.horizontalLayout.addWidget(self.graphicsView_Scream_Stylized_18)
        self.graphicsView_Scream_Stylized_15 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_15.setMinimumSize(QtCore.QSize(384, 216))
        self.graphicsView_Scream_Stylized_15.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_15.setStyleSheet("Border-image: url(:/Resized/Resized Pictures/Rain Princess - Resized.jpg)")
        self.graphicsView_Scream_Stylized_15.setObjectName("graphicsView_Scream_Stylized_15")
        self.horizontalLayout.addWidget(self.graphicsView_Scream_Stylized_15)
        self.graphicsView_Scream_Stylized_20 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_20.setMinimumSize(QtCore.QSize(384, 216))
        self.graphicsView_Scream_Stylized_20.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_20.setStyleSheet("border-image: url(:/Resized/Resized Pictures/Scream - Resized.jpg);")
        self.graphicsView_Scream_Stylized_20.setObjectName("graphicsView_Scream_Stylized_20")
        self.horizontalLayout.addWidget(self.graphicsView_Scream_Stylized_20)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.YourStylizedResultsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(36)
        self.YourStylizedResultsLabel.setFont(font)
        self.YourStylizedResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.YourStylizedResultsLabel.setObjectName("YourStylizedResultsLabel")
        self.verticalLayout.addWidget(self.YourStylizedResultsLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView_Scream_Stylized_13 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_13.setMinimumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_13.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_13.setStyleSheet("border-image: url(:/Camera/Camera Photo/Input Picture.jpg);")
        self.graphicsView_Scream_Stylized_13.setObjectName("graphicsView_Scream_Stylized_13")
        self.horizontalLayout_2.addWidget(self.graphicsView_Scream_Stylized_13)
        self.graphicsView_Scream_Stylized_19 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_19.setMinimumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_19.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_19.setStyleSheet("border-image: url(:/Stylized/Stylized Pictures/Stylized La Muse.jpg);")
        self.graphicsView_Scream_Stylized_19.setObjectName("graphicsView_Scream_Stylized_19")
        self.horizontalLayout_2.addWidget(self.graphicsView_Scream_Stylized_19)
        self.graphicsView_Scream_Stylized_17 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_17.setMinimumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_17.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_17.setStyleSheet("border-image: url(:/Stylized/Stylized Pictures/Stylized Rain Princess.jpg);")
        self.graphicsView_Scream_Stylized_17.setObjectName("graphicsView_Scream_Stylized_17")
        self.horizontalLayout_2.addWidget(self.graphicsView_Scream_Stylized_17)
        self.graphicsView_Scream_Stylized_14 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized_14.setMinimumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_14.setMaximumSize(QtCore.QSize(426, 240))
        self.graphicsView_Scream_Stylized_14.setStyleSheet("border-image: url(:/Stylized/Stylized Pictures/Stylized Scream.jpg);")
        self.graphicsView_Scream_Stylized_14.setObjectName("graphicsView_Scream_Stylized_14")
        self.horizontalLayout_2.addWidget(self.graphicsView_Scream_Stylized_14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ArtWithMachineLearningLabel.setText(_translate("MainWindow", "Art With Machine Learning"))
        self.OriginalStyleLabel.setText(_translate("MainWindow", "Original Styles"))
        self.label_3.setText(_translate("MainWindow", "<html><center>Your Next Three Results Will Be<br> Ready In 20 Seconds</cenmter></html>"))
        self.LaMuseLabel.setText(_translate("MainWindow", "Picasso\'s\n"
"La Muse"))
        self.RainPrincessLabel.setText(_translate("MainWindow", "Leonid Afremov\'s\n"
"Rain Princess"))
        self.label.setText(_translate("MainWindow", "Edvard Munch\'s\n"
"The Scream"))
        self.YourStylizedResultsLabel.setText(_translate("MainWindow", "Your Stylized Results!"))
import ResourceFile_rc
