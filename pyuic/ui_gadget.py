# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gadget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Gadget(object):
    def setupUi(self, Gadget):
        Gadget.setObjectName("Gadget")
        Gadget.resize(900, 555)
        Gadget.setMinimumSize(QtCore.QSize(900, 555))
        self.gridLayout = QtWidgets.QGridLayout(Gadget)
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Gadget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.serial_tab = QtWidgets.QWidget()
        self.serial_tab.setObjectName("serial_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.serial_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.formGroupBox = QtWidgets.QGroupBox(self.serial_tab)
        self.formGroupBox.setObjectName("formGroupBox")
        self.label = QtWidgets.QLabel(self.formGroupBox)
        self.label.setGeometry(QtCore.QRect(14, 35, 77, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.formGroupBox)
        self.label_2.setGeometry(QtCore.QRect(13, 79, 78, 18))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.lineEdit.setGeometry(QtCore.QRect(97, 35, 125, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(97, 79, 125, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_10.addWidget(self.formGroupBox, 1, 1, 1, 1)
        self.formGroupBox1 = QtWidgets.QGroupBox(self.serial_tab)
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.formGroupBox1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.gridLayout_5.addWidget(self.s1__lb_1, 0, 0, 1, 1)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.gridLayout_5.addWidget(self.s1__lb_5, 5, 0, 1, 1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox1)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.gridLayout_5.addWidget(self.s1__box_1, 0, 1, 1, 2)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.gridLayout_5.addWidget(self.s1__box_4, 4, 2, 1, 1)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox1)
        self.open_button.setObjectName("open_button")
        self.gridLayout_5.addWidget(self.open_button, 7, 0, 1, 2)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.gridLayout_5.addWidget(self.s1__box_3, 3, 2, 1, 1)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox1)
        self.close_button.setObjectName("close_button")
        self.gridLayout_5.addWidget(self.close_button, 7, 2, 1, 1)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.gridLayout_5.addWidget(self.s1__lb_6, 6, 0, 1, 1)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.gridLayout_5.addWidget(self.s1__lb_4, 4, 0, 1, 1)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.gridLayout_5.addWidget(self.s1__box_6, 6, 2, 1, 1)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.gridLayout_5.addWidget(self.s1__box_5, 5, 2, 1, 1)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_2.setObjectName("s1__box_2")
        self.gridLayout_5.addWidget(self.s1__box_2, 1, 1, 1, 2)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.gridLayout_5.addWidget(self.s1__lb_3, 3, 0, 1, 1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.gridLayout_5.addWidget(self.s1__lb_2, 1, 0, 1, 1)
        self.state_label = QtWidgets.QLabel(self.formGroupBox1)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.gridLayout_5.addWidget(self.state_label, 2, 0, 1, 3)
        self.gridLayout_10.addWidget(self.formGroupBox1, 0, 1, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.serial_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalGroupBox.setFont(font)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.verticalGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.s2__receive_text.setFont(font)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.gridLayout_4.addWidget(self.s2__receive_text, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.verticalGroupBox, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.hex_receive = QtWidgets.QCheckBox(self.serial_tab)
        self.hex_receive.setObjectName("hex_receive")
        self.gridLayout_6.addWidget(self.hex_receive, 3, 0, 1, 1)
        self.save_log_cb = QtWidgets.QCheckBox(self.serial_tab)
        self.save_log_cb.setObjectName("save_log_cb")
        self.gridLayout_6.addWidget(self.save_log_cb, 2, 0, 1, 1)
        self.timestamp_cb = QtWidgets.QCheckBox(self.serial_tab)
        self.timestamp_cb.setObjectName("timestamp_cb")
        self.gridLayout_6.addWidget(self.timestamp_cb, 1, 0, 1, 1)
        self.s2__clear_button = QtWidgets.QPushButton(self.serial_tab)
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.gridLayout_6.addWidget(self.s2__clear_button, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 5, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dw = QtWidgets.QLabel(self.serial_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dw.setFont(font)
        self.dw.setObjectName("dw")
        self.gridLayout_3.addWidget(self.dw, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.serial_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 4, 1, 1)
        self.timer_send_cb = QtWidgets.QCheckBox(self.serial_tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.timer_send_cb.setFont(font)
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.gridLayout_3.addWidget(self.timer_send_cb, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.s3__clear_button = QtWidgets.QPushButton(self.serial_tab)
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.gridLayout_7.addWidget(self.s3__clear_button, 2, 0, 1, 1)
        self.hex_send = QtWidgets.QCheckBox(self.serial_tab)
        self.hex_send.setObjectName("hex_send")
        self.gridLayout_7.addWidget(self.hex_send, 0, 0, 1, 1)
        self.s3__send_button = QtWidgets.QPushButton(self.serial_tab)
        self.s3__send_button.setObjectName("s3__send_button")
        self.gridLayout_7.addWidget(self.s3__send_button, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 1, 2, 1, 1)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.serial_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalGroupBox_2.setFont(font)
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalGroupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.s3__send_text.setFont(font)
        self.s3__send_text.setObjectName("s3__send_text")
        self.gridLayout_2.addWidget(self.s3__send_text, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.verticalGroupBox_2, 1, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        self.tabWidget.addTab(self.serial_tab, "")
        self.tcp_udp_tab = QtWidgets.QWidget()
        self.tcp_udp_tab.setObjectName("tcp_udp_tab")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tcp_udp_tab)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.lb_1 = QtWidgets.QLabel(self.tcp_udp_tab)
        self.lb_1.setObjectName("lb_1")
        self.gridLayout_14.addWidget(self.lb_1, 0, 0, 1, 1)
        self.lineEdit_local_ip = QtWidgets.QLineEdit(self.tcp_udp_tab)
        self.lineEdit_local_ip.setObjectName("lineEdit_local_ip")
        self.gridLayout_14.addWidget(self.lineEdit_local_ip, 0, 1, 1, 1)
        self.pushButton_get_ip = QtWidgets.QPushButton(self.tcp_udp_tab)
        self.pushButton_get_ip.setObjectName("pushButton_get_ip")
        self.gridLayout_14.addWidget(self.pushButton_get_ip, 0, 2, 1, 1)
        self.lb_2 = QtWidgets.QLabel(self.tcp_udp_tab)
        self.lb_2.setObjectName("lb_2")
        self.gridLayout_14.addWidget(self.lb_2, 1, 0, 1, 1)
        self.lineEdit_port = QtWidgets.QLineEdit(self.tcp_udp_tab)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.gridLayout_14.addWidget(self.lineEdit_port, 1, 1, 1, 1)
        self.lb_3 = QtWidgets.QLabel(self.tcp_udp_tab)
        self.lb_3.setObjectName("lb_3")
        self.gridLayout_14.addWidget(self.lb_3, 2, 0, 1, 1)
        self.lineEdit_port_2 = QtWidgets.QLineEdit(self.tcp_udp_tab)
        self.lineEdit_port_2.setObjectName("lineEdit_port_2")
        self.gridLayout_14.addWidget(self.lineEdit_port_2, 2, 1, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(self.tcp_udp_tab)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.gridLayout_14.addWidget(self.comboBox_type, 3, 0, 1, 1)
        self.pushButton_link = QtWidgets.QPushButton(self.tcp_udp_tab)
        self.pushButton_link.setObjectName("pushButton_link")
        self.gridLayout_14.addWidget(self.pushButton_link, 3, 1, 1, 1)
        self.pushButton_unlink = QtWidgets.QPushButton(self.tcp_udp_tab)
        self.pushButton_unlink.setObjectName("pushButton_unlink")
        self.gridLayout_14.addWidget(self.pushButton_unlink, 3, 2, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tcp_udp_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.textBrowser_recv = QtWidgets.QTextBrowser(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_recv.setFont(font)
        self.textBrowser_recv.setObjectName("textBrowser_recv")
        self.gridLayout_12.addWidget(self.textBrowser_recv, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem4, 0, 0, 1, 1)
        self.p_clear_recv_area = QtWidgets.QPushButton(self.tcp_udp_tab)
        self.p_clear_recv_area.setObjectName("p_clear_recv_area")
        self.gridLayout_13.addWidget(self.p_clear_recv_area, 0, 2, 1, 1)
        self.checkBox_timestamp = QtWidgets.QCheckBox(self.tcp_udp_tab)
        self.checkBox_timestamp.setObjectName("checkBox_timestamp")
        self.gridLayout_13.addWidget(self.checkBox_timestamp, 0, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_13, 1, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 1, 2, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox = QtWidgets.QGroupBox(self.tcp_udp_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.textEdit_send = QtWidgets.QTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_send.setFont(font)
        self.textEdit_send.setObjectName("textEdit_send")
        self.gridLayout_11.addWidget(self.textEdit_send, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox, 0, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem5, 1, 0, 1, 1)
        self.p_clear_send_area = QtWidgets.QPushButton(self.tcp_udp_tab)
        self.p_clear_send_area.setObjectName("p_clear_send_area")
        self.gridLayout_15.addWidget(self.p_clear_send_area, 1, 1, 1, 1)
        self.pushButton_send = QtWidgets.QPushButton(self.tcp_udp_tab)
        self.pushButton_send.setObjectName("pushButton_send")
        self.gridLayout_15.addWidget(self.pushButton_send, 1, 2, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tcp_udp_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Gadget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gadget)

    def retranslateUi(self, Gadget):
        _translate = QtCore.QCoreApplication.translate
        Gadget.setWindowTitle(_translate("Gadget", "Form"))
        self.formGroupBox.setTitle(_translate("Gadget", "Port State"))
        self.label.setText(_translate("Gadget", "Recv Length:"))
        self.label_2.setText(_translate("Gadget", "Send Length:"))
        self.formGroupBox1.setTitle(_translate("Gadget", "Port Setting"))
        self.s1__lb_1.setText(_translate("Gadget", "Detection:"))
        self.s1__lb_5.setText(_translate("Gadget", "Check Bit:"))
        self.s1__box_1.setText(_translate("Gadget", "Detection Port"))
        self.s1__box_4.setItemText(0, _translate("Gadget", "8"))
        self.s1__box_4.setItemText(1, _translate("Gadget", "7"))
        self.s1__box_4.setItemText(2, _translate("Gadget", "6"))
        self.s1__box_4.setItemText(3, _translate("Gadget", "5"))
        self.open_button.setText(_translate("Gadget", "Open"))
        self.s1__box_3.setItemText(0, _translate("Gadget", "115200"))
        self.s1__box_3.setItemText(1, _translate("Gadget", "2400"))
        self.s1__box_3.setItemText(2, _translate("Gadget", "4800"))
        self.s1__box_3.setItemText(3, _translate("Gadget", "9600"))
        self.s1__box_3.setItemText(4, _translate("Gadget", "14400"))
        self.s1__box_3.setItemText(5, _translate("Gadget", "19200"))
        self.s1__box_3.setItemText(6, _translate("Gadget", "38400"))
        self.s1__box_3.setItemText(7, _translate("Gadget", "57600"))
        self.s1__box_3.setItemText(8, _translate("Gadget", "76800"))
        self.s1__box_3.setItemText(9, _translate("Gadget", "12800"))
        self.s1__box_3.setItemText(10, _translate("Gadget", "230400"))
        self.s1__box_3.setItemText(11, _translate("Gadget", "460800"))
        self.s1__box_3.setItemText(12, _translate("Gadget", "3000000"))
        self.close_button.setText(_translate("Gadget", "Close"))
        self.s1__lb_6.setText(_translate("Gadget", "Stop Bit:"))
        self.s1__lb_4.setText(_translate("Gadget", "Data Bit:"))
        self.s1__box_6.setItemText(0, _translate("Gadget", "1"))
        self.s1__box_5.setItemText(0, _translate("Gadget", "N"))
        self.s1__lb_3.setText(_translate("Gadget", "Boud Rate:"))
        self.s1__lb_2.setText(_translate("Gadget", "Select:"))
        self.verticalGroupBox.setTitle(_translate("Gadget", "Receiving Area:"))
        self.hex_receive.setText(_translate("Gadget", "Hex Recv"))
        self.save_log_cb.setText(_translate("Gadget", "Save Log"))
        self.timestamp_cb.setText(_translate("Gadget", "Timestamp"))
        self.s2__clear_button.setText(_translate("Gadget", "Clear"))
        self.dw.setText(_translate("Gadget", "ms/times"))
        self.lineEdit_3.setText(_translate("Gadget", "1000"))
        self.timer_send_cb.setText(_translate("Gadget", "Timed transmission"))
        self.s3__clear_button.setText(_translate("Gadget", "Clear"))
        self.hex_send.setText(_translate("Gadget", "Hex Send"))
        self.s3__send_button.setText(_translate("Gadget", " Send Data "))
        self.verticalGroupBox_2.setTitle(_translate("Gadget", "Sending Area:"))
        self.s3__send_text.setHtml(_translate("Gadget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serial_tab), _translate("Gadget", "Serial"))
        self.lb_1.setText(_translate("Gadget", "Localhost ip:"))
        self.pushButton_get_ip.setText(_translate("Gadget", "Get localhost ip"))
        self.lb_2.setText(_translate("Gadget", "Port:"))
        self.lb_3.setText(_translate("Gadget", "Destination ip:"))
        self.comboBox_type.setItemText(0, _translate("Gadget", "TCP Server"))
        self.comboBox_type.setItemText(1, _translate("Gadget", "TCP Client"))
        self.comboBox_type.setItemText(2, _translate("Gadget", "Udp_Server"))
        self.comboBox_type.setItemText(3, _translate("Gadget", "Udp_Client"))
        self.pushButton_link.setText(_translate("Gadget", "Connect"))
        self.pushButton_unlink.setText(_translate("Gadget", "Disconnect"))
        self.groupBox_2.setTitle(_translate("Gadget", "Recv Area:"))
        self.p_clear_recv_area.setText(_translate("Gadget", "Clear"))
        self.checkBox_timestamp.setText(_translate("Gadget", "Timestamp"))
        self.groupBox.setTitle(_translate("Gadget", "Send Area:"))
        self.p_clear_send_area.setText(_translate("Gadget", "clear"))
        self.pushButton_send.setText(_translate("Gadget", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tcp_udp_tab), _translate("Gadget", "TCP/UDP"))

