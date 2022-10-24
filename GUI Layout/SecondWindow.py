# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1864, 1331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_LaMuse_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_LaMuse_Original.setGeometry(QtCore.QRect(10, 600, 300, 300))
        self.graphicsView_LaMuse_Original.setStyleSheet("background-image: url(:/Resized Images/Resized Pictures/La Muse - Resized.jpg);")
        self.graphicsView_LaMuse_Original.setObjectName("graphicsView_LaMuse_Original")
        self.ArtWithMachineLearningLabel = QtWidgets.QLabel(self.centralwidget)
        self.ArtWithMachineLearningLabel.setGeometry(QtCore.QRect(0, 0, 1861, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.ArtWithMachineLearningLabel.setFont(font)
        self.ArtWithMachineLearningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ArtWithMachineLearningLabel.setObjectName("ArtWithMachineLearningLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1861, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 420, 1861, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.OriginalStyleLabel = QtWidgets.QLabel(self.centralwidget)
        self.OriginalStyleLabel.setGeometry(QtCore.QRect(770, 430, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.OriginalStyleLabel.setFont(font)
        self.OriginalStyleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OriginalStyleLabel.setObjectName("OriginalStyleLabel")
        self.YourStylizedResultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.YourStylizedResultsLabel.setGeometry(QtCore.QRect(0, 910, 1861, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.YourStylizedResultsLabel.setFont(font)
        self.YourStylizedResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.YourStylizedResultsLabel.setObjectName("YourStylizedResultsLabel")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 900, 1861, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.graphicsView_Input_Picture = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Input_Picture.setGeometry(QtCore.QRect(770, 120, 300, 300))
        self.graphicsView_Input_Picture.setStyleSheet("background-image: url(:/Camera Photo/Camera Photo/Input Picture.jpg);\n"
"background-image: url(:/Camera Photo/Camera Photo/Input Picture.jpg);")
        self.graphicsView_Input_Picture.setObjectName("graphicsView_Input_Picture")
        self.LaMuseLabel = QtWidgets.QLabel(self.centralwidget)
        self.LaMuseLabel.setGeometry(QtCore.QRect(10, 480, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.LaMuseLabel.setFont(font)
        self.LaMuseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LaMuseLabel.setObjectName("LaMuseLabel")
        self.graphicsView_RainPrincess_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_RainPrincess_Original.setGeometry(QtCore.QRect(320, 600, 300, 300))
        self.graphicsView_RainPrincess_Original.setStyleSheet("background-image: url(:/Resized Images/Resized Pictures/Rain Princess - Resized.jpg);")
        self.graphicsView_RainPrincess_Original.setObjectName("graphicsView_RainPrincess_Original")
        self.PicassoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PicassoLabel.setGeometry(QtCore.QRect(10, 540, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.PicassoLabel.setFont(font)
        self.PicassoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PicassoLabel.setObjectName("PicassoLabel")
        self.RainPrincessLabel = QtWidgets.QLabel(self.centralwidget)
        self.RainPrincessLabel.setGeometry(QtCore.QRect(320, 480, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.RainPrincessLabel.setFont(font)
        self.RainPrincessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RainPrincessLabel.setObjectName("RainPrincessLabel")
        self.LeonidAfremovLabel = QtWidgets.QLabel(self.centralwidget)
        self.LeonidAfremovLabel.setGeometry(QtCore.QRect(320, 540, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.LeonidAfremovLabel.setFont(font)
        self.LeonidAfremovLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LeonidAfremovLabel.setObjectName("LeonidAfremovLabel")
        self.EdvardMunchLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdvardMunchLabel.setGeometry(QtCore.QRect(630, 540, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.EdvardMunchLabel.setFont(font)
        self.EdvardMunchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EdvardMunchLabel.setObjectName("EdvardMunchLabel")
        self.ScreamLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScreamLabel.setGeometry(QtCore.QRect(630, 480, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.ScreamLabel.setFont(font)
        self.ScreamLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ScreamLabel.setObjectName("ScreamLabel")
        self.graphicsView_Scream_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Original.setGeometry(QtCore.QRect(630, 600, 300, 300))
        self.graphicsView_Scream_Original.setStyleSheet("background-image: url(:/Resized Images/Resized Pictures/Scream - Resized.jpg);")
        self.graphicsView_Scream_Original.setObjectName("graphicsView_Scream_Original")
        self.VanGoghLabel = QtWidgets.QLabel(self.centralwidget)
        self.VanGoghLabel.setGeometry(QtCore.QRect(940, 540, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.VanGoghLabel.setFont(font)
        self.VanGoghLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VanGoghLabel.setObjectName("VanGoghLabel")
        self.StarryNightLabel = QtWidgets.QLabel(self.centralwidget)
        self.StarryNightLabel.setGeometry(QtCore.QRect(940, 480, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.StarryNightLabel.setFont(font)
        self.StarryNightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StarryNightLabel.setObjectName("StarryNightLabel")
        self.graphicsView_StarryNight_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_StarryNight_Original.setGeometry(QtCore.QRect(940, 600, 300, 300))
        self.graphicsView_StarryNight_Original.setStyleSheet("background-image: url(:/Resized Images/Resized Pictures/Starry Night - Resized.jpg);")
        self.graphicsView_StarryNight_Original.setObjectName("graphicsView_StarryNight_Original")
        self.FrancisPicabiaLabel = QtWidgets.QLabel(self.centralwidget)
        self.FrancisPicabiaLabel.setGeometry(QtCore.QRect(1250, 540, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.FrancisPicabiaLabel.setFont(font)
        self.FrancisPicabiaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FrancisPicabiaLabel.setObjectName("FrancisPicabiaLabel")
        self.UdnieLabel = QtWidgets.QLabel(self.centralwidget)
        self.UdnieLabel.setGeometry(QtCore.QRect(1250, 480, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.UdnieLabel.setFont(font)
        self.UdnieLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UdnieLabel.setObjectName("UdnieLabel")
        self.graphicsView_Udnie_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Udnie_Original.setGeometry(QtCore.QRect(1250, 600, 300, 300))
        self.graphicsView_Udnie_Original.setStyleSheet("background-image: url(:/Resized Images/Resized Pictures/Udnie - Resized.jpg);")
        self.graphicsView_Udnie_Original.setObjectName("graphicsView_Udnie_Original")
        self.HokusaiLabel = QtWidgets.QLabel(self.centralwidget)
        self.HokusaiLabel.setGeometry(QtCore.QRect(1560, 540, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.HokusaiLabel.setFont(font)
        self.HokusaiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HokusaiLabel.setObjectName("HokusaiLabel")
        self.GreatWaveLabel = QtWidgets.QLabel(self.centralwidget)
        self.GreatWaveLabel.setGeometry(QtCore.QRect(1560, 480, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.GreatWaveLabel.setFont(font)
        self.GreatWaveLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GreatWaveLabel.setObjectName("GreatWaveLabel")
        self.graphicsView_GreatWave_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_GreatWave_Original.setGeometry(QtCore.QRect(1560, 600, 300, 300))
        self.graphicsView_GreatWave_Original.setStyleSheet("background-image: url(:/Resized Images/Resized Pictures/Great Wave - Resized.jpg);")
        self.graphicsView_GreatWave_Original.setObjectName("graphicsView_GreatWave_Original")
        self.graphicsView_LaMuse_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_LaMuse_Stylized.setGeometry(QtCore.QRect(10, 980, 300, 300))
        self.graphicsView_LaMuse_Stylized.setStyleSheet("background-image: url(:/Stylized Images/Stylized Pictures/Stylized La Muse.jpg);")
        self.graphicsView_LaMuse_Stylized.setObjectName("graphicsView_LaMuse_Stylized")
        self.graphicsView_Udnie_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Udnie_Stylized.setGeometry(QtCore.QRect(1250, 980, 300, 300))
        self.graphicsView_Udnie_Stylized.setStyleSheet("background-image: url(:/Stylized Images/Stylized Pictures/Stylized Udnie.jpg);")
        self.graphicsView_Udnie_Stylized.setObjectName("graphicsView_Udnie_Stylized")
        self.graphicsView_GreatWave_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_GreatWave_Stylized.setGeometry(QtCore.QRect(1560, 980, 300, 300))
        self.graphicsView_GreatWave_Stylized.setStyleSheet("background-image: url(:/Stylized Images/Stylized Pictures/Stylized Great Wave.jpg);")
        self.graphicsView_GreatWave_Stylized.setObjectName("graphicsView_GreatWave_Stylized")
        self.graphicsView_RainPrincess_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_RainPrincess_Stylized.setGeometry(QtCore.QRect(320, 980, 300, 300))
        self.graphicsView_RainPrincess_Stylized.setStyleSheet("background-image: url(:/Stylized Images/Stylized Pictures/Stylized Rain Princess.jpg);")
        self.graphicsView_RainPrincess_Stylized.setObjectName("graphicsView_RainPrincess_Stylized")
        self.graphicsView_Scream_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized.setGeometry(QtCore.QRect(630, 980, 300, 300))
        self.graphicsView_Scream_Stylized.setStyleSheet("background-image: url(:/Stylized Images/Stylized Pictures/Stylized Scream.jpg);")
        self.graphicsView_Scream_Stylized.setObjectName("graphicsView_Scream_Stylized")
        self.graphicsView_StarryNight_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_StarryNight_Stylized.setGeometry(QtCore.QRect(940, 980, 300, 300))
        self.graphicsView_StarryNight_Stylized.setStyleSheet("background-image: url(:/Stylized Images/Stylized Pictures/Stylized Starry Night.jpg);")
        self.graphicsView_StarryNight_Stylized.setObjectName("graphicsView_StarryNight_Stylized")
        self.OriginalPictureLabel = QtWidgets.QLabel(self.centralwidget)
        self.OriginalPictureLabel.setGeometry(QtCore.QRect(770, 60, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.OriginalPictureLabel.setFont(font)
        self.OriginalPictureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OriginalPictureLabel.setObjectName("OriginalPictureLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1864, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ArtWithMachineLearningLabel.setText(_translate("MainWindow", "Art With Machine Learning"))
        self.OriginalStyleLabel.setText(_translate("MainWindow", "Original Style"))
        self.YourStylizedResultsLabel.setText(_translate("MainWindow", "Your Stylized Results!"))
        self.LaMuseLabel.setText(_translate("MainWindow", "La Muse by"))
        self.PicassoLabel.setText(_translate("MainWindow", "Picasso"))
        self.RainPrincessLabel.setText(_translate("MainWindow", "Rain Princess by"))
        self.LeonidAfremovLabel.setText(_translate("MainWindow", "Leonid Afremov"))
        self.EdvardMunchLabel.setText(_translate("MainWindow", "Edvard Munch"))
        self.ScreamLabel.setText(_translate("MainWindow", "Scream by"))
        self.VanGoghLabel.setText(_translate("MainWindow", "Van Gogh"))
        self.StarryNightLabel.setText(_translate("MainWindow", "Starry Night by"))
        self.FrancisPicabiaLabel.setText(_translate("MainWindow", "Francis Picabia"))
        self.UdnieLabel.setText(_translate("MainWindow", "Udnie by"))
        self.HokusaiLabel.setText(_translate("MainWindow", "Hokusai"))
        self.GreatWaveLabel.setText(_translate("MainWindow", "Great Wave by"))
        self.OriginalPictureLabel.setText(_translate("MainWindow", "Original Picture"))
import Image Resource File_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
