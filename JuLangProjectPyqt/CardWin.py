# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CardWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 848)
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(548, 520, 91, 31))
        self.clearBtn.setMinimumSize(QtCore.QSize(91, 0))
        self.clearBtn.setObjectName("clearBtn")
        self.generatetBtn = QtWidgets.QPushButton(Form)
        self.generatetBtn.setGeometry(QtCore.QRect(658, 520, 91, 31))
        self.generatetBtn.setObjectName("generatetBtn")
        self.savefile = QtWidgets.QPushButton(Form)
        self.savefile.setGeometry(QtCore.QRect(428, 520, 91, 31))
        self.savefile.setMinimumSize(QtCore.QSize(91, 0))
        self.savefile.setObjectName("savefile")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 1221, 511))
        self.groupBox.setObjectName("groupBox")
        self.label_port_2 = QtWidgets.QLabel(self.groupBox)
        self.label_port_2.setGeometry(QtCore.QRect(720, 70, 181, 20))
        self.label_port_2.setObjectName("label_port_2")
        self.plainTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 90, 1011, 421))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_versions_2 = QtWidgets.QLabel(self.groupBox)
        self.label_versions_2.setGeometry(QtCore.QRect(390, 270, 91, 20))
        self.label_versions_2.setText("")
        self.label_versions_2.setObjectName("label_versions_2")
        self.gameTypeBtn = QtWidgets.QToolButton(self.groupBox)
        self.gameTypeBtn.setGeometry(QtCore.QRect(1020, 90, 161, 41))
        self.gameTypeBtn.setObjectName("gameTypeBtn")
        self.startBtn = QtWidgets.QPushButton(self.groupBox)
        self.startBtn.setGeometry(QtCore.QRect(1020, 270, 161, 41))
        self.startBtn.setObjectName("startBtn")
        self.startBtnOff = QtWidgets.QPushButton(self.groupBox)
        self.startBtnOff.setGeometry(QtCore.QRect(1020, 330, 161, 41))
        self.startBtnOff.setObjectName("startBtnOff")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 461, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_versions = QtWidgets.QLabel(self.layoutWidget)
        self.label_versions.setObjectName("label_versions")
        self.horizontalLayout.addWidget(self.label_versions)
        self.weatherComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.horizontalLayout.addWidget(self.weatherComboBox)
        self.label_port = QtWidgets.QLabel(self.layoutWidget)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout.addWidget(self.label_port)
        self.portComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.portComboBox.setObjectName("portComboBox")
        self.portComboBox.addItem("")
        self.portComboBox.addItem("")
        self.portComboBox.addItem("")
        self.horizontalLayout.addWidget(self.portComboBox)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.game_method = QtWidgets.QPushButton(self.groupBox)
        self.game_method.setGeometry(QtCore.QRect(1020, 390, 161, 41))
        self.game_method.setObjectName("game_method")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(1020, 160, 161, 41))
        self.toolButton.setObjectName("toolButton")
        self.PBYtoolButton = QtWidgets.QToolButton(Form)
        self.PBYtoolButton.setGeometry(QtCore.QRect(1020, 220, 161, 41))
        self.PBYtoolButton.setObjectName("PBYtoolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.clearBtn.setText(_translate("Form", "重置数据"))
        self.generatetBtn.setText(_translate("Form", "提交"))
        self.savefile.setText(_translate("Form", "保存文件"))
        self.groupBox.setTitle(_translate("Form", "巨浪组做牌工具"))
        self.label_port_2.setText(_translate("Form", "可拖拽文件(txt,json文本)"))
        self.gameTypeBtn.setText(_translate("Form", "游戏类型选择"))
        self.startBtn.setText(_translate("Form", "做牌开启"))
        self.startBtnOff.setText(_translate("Form", "做牌关闭"))
        self.label_versions.setText(_translate("Form", "类型"))
        self.weatherComboBox.setItemText(0, _translate("Form", "本地麻将"))
        self.weatherComboBox.setItemText(1, _translate("Form", "本地跑胡子"))
        self.weatherComboBox.setItemText(2, _translate("Form", "本地跑得快"))
        self.weatherComboBox.setItemText(3, _translate("Form", "测试服麻将"))
        self.weatherComboBox.setItemText(4, _translate("Form", "测试服跑胡子"))
        self.weatherComboBox.setItemText(5, _translate("Form", "测试服跑得快"))
        self.label_port.setText(_translate("Form", "版本"))
        self.portComboBox.setItemText(0, _translate("Form", "长沙"))
        self.portComboBox.setItemText(1, _translate("Form", "常德"))
        self.portComboBox.setItemText(2, _translate("Form", "主版本"))
        self.label.setText(_translate("Form", "(9037主版本，9011长沙，9010常德)"))
        self.game_method.setText(_translate("Form", "游戏玩法复现"))
        self.toolButton.setText(_translate("Form", "获取线上牌局数据"))
        self.PBYtoolButton.setText(_translate("Form", "回放码牌获取"))

