import sys
import time
import queue
import serial
import operator
import threading
import re
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QAbstractItemView,QApplication
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtGui import QIcon,QColor,QStandardItemModel,QStandardItem,QBrush,QColor

from profile.xobj import XObject
from common import common

# Return Code:
Err_ok = 0
Err_fail = -1
Err_timeout = -2

time_out_queue = queue.Queue(maxsize=10)
time_out = 2


def timeout_set(time_interval, to_queue):
    def wrapper(func):
        def time_out():
            to_queue.put(1)
            # print ("Timeout Error: function not responded in %d seconds, exit automatically!" % time_interval)

        def deco(*args, **kwargs):
            timer = threading.Timer(time_interval, time_out)
            timer.start()
            res = func(*args, **kwargs)
            timer.cancel()
            to_queue.queue.clear()
            return res

        return deco
    return wrapper

class pyqt5_serial(object):
    def __init__(self):
        self.ui_obj = XObject.get_object("ui_obj")
        self.main_window_obj = XObject.get_object("main_window_obj")

        self.main_window_obj.setWindowTitle("HT_RF_PRODUCTION_TEST_TOOLS-v0.0.1 by WeiZhenhua")
        self.main_window_obj.setWindowIcon(QIcon('./image/ico.png'))
        self.ser = serial.Serial()
        self.port_check()

        self.send_buf = []

        self.timing_num = 0
        self.ui_obj.timing_le.setText(str(self.timing_num))
        self.test_times = 3
        self.ui_obj.test_times_le.setText(str(self.test_times))

        self.recv_buf_list = [0,0,0,0,0,0]
        self.sta_recv_rssi_thr = 0
        self.sta_send_rssi_thr = 0
        self.meter_addr_list = [0,0,0,0,0,0]
        self.total_pass_cnt = 0
        self.total_fail_cnt = 0
        self.current_testcase_max_row_index = 0
        self.current_history_max_row_index = 0

        #设置数据层次结构，3列
        self.testcase_model=QStandardItemModel(0,3)
        #设置水平方向四个头标签文本内容
        self.testcase_model.setHorizontalHeaderLabels(['接收','发送','测试结果'])
        self.ui_obj.testcase_tv.setModel(self.testcase_model)

        #设置数据层次结构，2列
        self.history_model=QStandardItemModel(0,2)
        #设置水平方向四个头标签文本内容
        self.history_model.setHorizontalHeaderLabels(['测试时间','测试结果'])
        self.ui_obj.history_tv.setModel(self.history_model)

        self.ui_obj.testcase_tv.horizontalHeader().setStretchLastSection(True)# 横向填满表格
        self.ui_obj.testcase_tv.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui_obj.testcase_tv.setSelectionMode(QAbstractItemView.NoSelection) #不可选中
        self.ui_obj.testcase_tv.setEditTriggers(QAbstractItemView.NoEditTriggers) #不可编辑
        self.ui_obj.testcase_tv.setShowGrid(False) #网格线条不可见

        self.ui_obj.history_tv.horizontalHeader().setStretchLastSection(True)# 横向填满表格
        self.ui_obj.history_tv.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui_obj.history_tv.setSelectionMode(QAbstractItemView.NoSelection) #不可选中
        self.ui_obj.history_tv.setEditTriggers(QAbstractItemView.NoEditTriggers) #不可编辑
        self.ui_obj.history_tv.setShowGrid(False) #网格线条不可见

        self.ui_obj.testcase_tv.setAutoScroll(True)
        self.ui_obj.testcase_tv.setAutoScrollMargin(3)

        self.init()

    def init(self):
        # 串口检测按钮
        self.ui_obj.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.ui_obj.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.ui_obj.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.ui_obj.close_button.clicked.connect(self.port_close)

         # 开始测试
        self.ui_obj.start_test_bt.clicked.connect(self.start_test)

        # 停止测试
        self.ui_obj.stop_test_bt.clicked.connect(self.stop_test)

        # 单次测试
        self.ui_obj.one_test_bt.clicked.connect(self.one_test)

        # 清空
        self.ui_obj.clear_bt.clicked.connect(self.clear_result)

        self.ui_obj.pass_cnt_bt.setEnabled(False)
        self.ui_obj.fail_cnt_bt.setEnabled(False)
        self.ui_obj.stop_test_bt.setEnabled(False)

        self.testing_flag = 0

    # 保存日志
    def save_log(self):
        pass
        # try:
        #     if self.ui_obj.save_log_cb.checkState():
        #         self.file_path =  QtWidgets.QFileDialog.getSaveFileName(self.main_window_obj,"save file","" ,"Txt files(*.log)")
        #         self.ui_obj.timestamp_cb.setEnabled(False)
        #         if self.file_path[0] != '':
        #             self.save_log_fd = open(self.file_path[0], "w")
        #         else:
        #             self.ui_obj.timestamp_cb.setEnabled(True)
        #             self.ui_obj.save_log_cb.setCheckState(0)

        #     else:
        #         self.save_log_fd.close()
        #         self.save_log_fd = None
        #         self.ui_obj.timestamp_cb.setEnabled(True)
        # except:
        #     self.save_log_fd = None
        #     self.ui_obj.save_log_cb.setCheckState(0)
        #     self.ui_obj.timestamp_cb.setEnabled(True)
        #     QMessageBox.critical(self.main_window_obj, "Open Error", "Can not open this files, please check!")
        #     return None

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.ui_obj.s1__box_2.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.ui_obj.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.ui_obj.state_label.setText("No Serial Port")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.ui_obj.s1__box_2.currentText()
        if imf_s != "":
            self.ui_obj.state_label.setText(self.Com_Dict[self.ui_obj.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        try:
            self.ser.port = self.ui_obj.s1__box_2.currentText()
            self.ser.baudrate = int(self.ui_obj.s1__box_3.currentText())
            self.ser.bytesize = int(self.ui_obj.s1__box_4.currentText())
            self.ser.stopbits = int(self.ui_obj.s1__box_6.currentText())
            self.ser.parity = self.ui_obj.s1__box_5.currentText()
            self.ser.open()
        except:
            QMessageBox.critical(self.main_window_obj, "Port Error", "Can not open this port, please check!")
            return None

        if self.ser.isOpen():
            #清空缓存区
            self.ser.reset_output_buffer()
            self.ui_obj.open_button.setEnabled(False)
            self.ui_obj.s1__box_1.setEnabled(False)
            self.ui_obj.s1__box_2.setEnabled(False)
            self.ui_obj.s1__box_3.setEnabled(False)
            self.ui_obj.s1__box_4.setEnabled(False)
            self.ui_obj.s1__box_5.setEnabled(False)
            self.ui_obj.s1__box_6.setEnabled(False)
            self.ui_obj.close_button.setEnabled(True)
            self.ui_obj.formGroupBox1.setTitle("串口状态(打开)")

    # 关闭串口
    def port_close(self):
        try:
            self.ser.close()
        except:
            pass
        self.ui_obj.open_button.setEnabled(True)
        self.ui_obj.close_button.setEnabled(False)
        self.ui_obj.s1__box_1.setEnabled(True)
        self.ui_obj.s1__box_2.setEnabled(True)
        self.ui_obj.s1__box_3.setEnabled(True)
        self.ui_obj.s1__box_4.setEnabled(True)
        self.ui_obj.s1__box_5.setEnabled(True)
        self.ui_obj.s1__box_6.setEnabled(True)
        
        self.ui_obj.formGroupBox1.setTitle("串口状态(关闭)")

        self.stop_test()

    # 开始测试
    def start_test(self):
        if self.ser.isOpen():

            self.ui_obj.test_times_le.setEnabled(False)
            self.ui_obj.timing_le.setEnabled(False)

            self.ui_obj.sta_recv_rssi_le.setEnabled(False)
            self.ui_obj.sta_send_rssi_le.setEnabled(False)
            self.ui_obj.meter_addr_le.setEnabled(False)

            self.ui_obj.channel_num_Box.setEnabled(False)
            self.ui_obj.dB_Box.setEnabled(False)

            self.ui_obj.clear_bt.setEnabled(False)

            self.ui_obj.one_test_bt.setEnabled(False)
            self.ui_obj.start_test_bt.setEnabled(False)

            self.ui_obj.stop_test_bt.setEnabled(True)

            self.testing_flag = 1
            QApplication.processEvents()# 刷新页面

            self.start_loop_test()
        else:
            QMessageBox.critical(self.main_window_obj, 'Warning', 'Please check port is opened!')

    # 停止测试
    def stop_test(self):
        self.test_times = 0

        self.ui_obj.test_times_le.setEnabled(True)
        self.ui_obj.timing_le.setEnabled(True)

        self.ui_obj.sta_recv_rssi_le.setEnabled(True)
        self.ui_obj.sta_send_rssi_le.setEnabled(True)
        self.ui_obj.meter_addr_le.setEnabled(True)

        self.ui_obj.channel_num_Box.setEnabled(True)
        self.ui_obj.dB_Box.setEnabled(True)

        self.ui_obj.clear_bt.setEnabled(True)

        self.ui_obj.one_test_bt.setEnabled(True)
        self.ui_obj.start_test_bt.setEnabled(True)


        self.ui_obj.stop_test_bt.setEnabled(False)

        if self.testing_flag == 1:
            self.testing_flag = 0
        else:
            self.show_stop_testing_state()
            
    
    # 开始循环测试 
    def start_loop_test(self):
        #测试之前先清空testcase 
        #设置数据层次结构，3列
        self.testcase_model=QStandardItemModel(0,3)
        #设置水平方向四个头标签文本内容
        self.testcase_model.setHorizontalHeaderLabels(['接收','发送','测试结果'])
        self.ui_obj.testcase_tv.setModel(self.testcase_model)
        self.current_testcase_max_row_index = 0

        # 设置发送状态
        self.show_testing_state()

        # 仅在此处获取发送次数
        self.test_times = int(self.ui_obj.test_times_le.text())

        pass_flag = 0
        while self.test_times:
            self.compose_func()
            return_value = self.data_send(self.send_buf, time_out_queue)
            if return_value == Err_timeout:
                # 向testcase tableview 填写红色超时
                self.show_testcase_timeout()
                pass_flag = 1
            else:
                # 取出该数据帧 校验正确后 比较阈值 填入testcase 
                self.recv_buf_list[0] = int(return_value[0:2], 16)
                self.recv_buf_list[1] = int(return_value[2:4], 16)
                self.recv_buf_list[2] = int(return_value[4:6], 16)
                self.recv_buf_list[3] = int(return_value[6:8], 16)
                self.recv_buf_list[4] = int(return_value[8:10], 16)
                self.recv_buf_list[5] = int(return_value[10:12], 16)

                recv_rssi_result = self.show_test_case_recv_rssi(self.recv_buf_list[2])
                send_rssi_result = self.show_test_case_send_rssi(self.recv_buf_list[3])
                if (recv_rssi_result+send_rssi_result) == 0:
                    self.show_test_case_pass()
                    time.sleep(self.timing_num/1000)# 循环发送间隔
                else:
                    self.show_test_case_fail()
                    pass_flag = 1

            self.test_times -= 1

        if pass_flag == 0:
            self.show_test_pass_state()
        else:
            self.show_test_fail_state()

        self.stop_test()

    def one_test(self):
        if self.ser.isOpen():
            self.ui_obj.one_test_bt.setEnabled(False)
            self.compose_func()
            return_value = self.data_send(self.send_buf, time_out_queue)
            if return_value == Err_timeout:
                # 向testcase tableview 填写红色超时
                self.show_testcase_timeout()
            else:
                # 取出该数据帧 校验正确后 比较阈值 填入testcase 
                self.recv_buf_list[0] = int(return_value[0:2], 16)
                self.recv_buf_list[1] = int(return_value[2:4], 16)
                self.recv_buf_list[2] = int(return_value[4:6], 16)
                self.recv_buf_list[3] = int(return_value[6:8], 16)
                self.recv_buf_list[4] = int(return_value[8:10], 16)
                self.recv_buf_list[5] = int(return_value[10:12], 16)

                if self.recv_buf_list[4] != common.uchar_checksum(self.recv_buf_list[:4]):
                    self.show_testcase_timeout()
                    return

                recv_rssi_result = self.show_test_case_recv_rssi(self.recv_buf_list[2])
                send_rssi_result = self.show_test_case_send_rssi(self.recv_buf_list[3])
                if (recv_rssi_result+send_rssi_result) == 0:
                    self.show_test_case_pass()
                else:
                    self.show_test_case_fail()
            self.ui_obj.one_test_bt.setEnabled(True)
        else:
            QMessageBox.critical(self.main_window_obj, 'Warning', 'Please check port is opened!')

    def clear_result(self):
        self.ui_obj.pass_cnt_bt.setText("0通过")
        self.ui_obj.fail_cnt_bt.setText("0失败")
        self.total_pass_cnt = 0
        self.total_fail_cnt = 0

        #设置数据层次结构，3列
        self.testcase_model=QStandardItemModel(0,3)
        #设置水平方向四个头标签文本内容
        self.testcase_model.setHorizontalHeaderLabels(['接收','发送','测试结果'])
        self.ui_obj.testcase_tv.setModel(self.testcase_model)

        #设置数据层次结构，2列
        self.history_model=QStandardItemModel(0,2)
        #设置水平方向四个头标签文本内容
        self.history_model.setHorizontalHeaderLabels(['测试时间','测试结果'])
        self.ui_obj.history_tv.setModel(self.history_model)

        self.current_testcase_max_row_index = 0
        self.current_history_max_row_index = 0

        self.show_wait_testing_state()

    # 发送数据
    @timeout_set(time_out, time_out_queue)
    def data_send(self, send_list, time_out_queue):
        input_s = ''

        input_s = bytes(send_list)
        num = self.ser.write(input_s)
        return_value, cs_info = 0, ''

        m_tt_comp = re.compile(r"6802\w{6}16")

        while 1:
            # data = self.ser.read(1)
            bytes2read = self.ser.inWaiting()
            tmp = self.ser.read(bytes2read)
            for i in range(0, len(tmp)):
                cs_info = cs_info + '{:02X}'.format(tmp[i])

            m_tt = m_tt_comp.search(cs_info)
            if m_tt:
                return_str = m_tt.group(0)
                return return_str
            if not time_out_queue.empty():
                return Err_timeout
    #组帧
    def compose_func(self):
        # time.sleep(2)
        self.get_parameter()# 获取控件上的参数
        self.send_buf = []
        try:
            self.send_buf = [0x68, 0x00, 0x00, 0x40, 0x04, 0xF4, 0xEE, 0x04, 0x02, 0xE8, 0x00, 0x00, 0x00,]
            dB_dict = {"dB01":1,"dB02":2,"dB05":5,"dB08":8,"dB11":11,"dB14":14,"dB17":17,"dB20":20}

            self.send_buf[10] = int(self.ui_obj.channel_num_Box.currentText()) #信道号0-64
            self.send_buf[11] = dB_dict[self.ui_obj.dB_Box.currentText()] # 发射功率
            self.send_buf[12] = 6 # 数据固定为长度 

            self.send_buf.extend(self.meter_addr_list)
            self.send_buf.append(common.uchar_checksum(self.send_buf[2:]))
            self.send_buf.append(0x16)
            self.send_buf[1] = len(self.send_buf) #GD17帧长度

        except Exception as e:
            QMessageBox.critical(self.main_window_obj, "Data Err", "Data Err!")

    def get_parameter(self):
        self.timing_num = int(self.ui_obj.timing_le.text())

        self.sta_recv_rssi_thr = int(self.ui_obj.sta_recv_rssi_le.text())
        self.sta_send_rssi_thr = int(self.ui_obj.sta_send_rssi_le.text())
        meter_addr_str = self.ui_obj.meter_addr_le.text()
        strlen = len(meter_addr_str)
        if strlen<12:
            meter_addr_str = "0"*(12-strlen)+meter_addr_str

        self.meter_addr_list[5] = int(meter_addr_str[0:2], 16)
        self.meter_addr_list[4] = int(meter_addr_str[2:4], 16)
        self.meter_addr_list[3] = int(meter_addr_str[4:6], 16)
        self.meter_addr_list[2] = int(meter_addr_str[6:8], 16)
        self.meter_addr_list[1] = int(meter_addr_str[8:10], 16)
        self.meter_addr_list[0] = int(meter_addr_str[10:12], 16)

    def show_testing_state(self):
        self.ui_obj.result_lb.setStyleSheet("font: 16pt \"Adobe Devanagari\";\n""color: rgb(0, 0, 0);")
        self.ui_obj.result_lb.setText("正在测试...")
        QApplication.processEvents()# 刷新页面

    def show_stop_testing_state(self):
        self.ui_obj.result_lb.setStyleSheet("font: 16pt \"Adobe Devanagari\";\n""color: rgb(0, 0, 0);")
        self.ui_obj.result_lb.setText("测试中断...")
        QApplication.processEvents()# 刷新页面

    def show_wait_testing_state(self):
        self.ui_obj.result_lb.setStyleSheet("font: 16pt \"Adobe Devanagari\";\n""color: rgb(0, 0, 0);")
        self.ui_obj.result_lb.setText("等待测试...")
        QApplication.processEvents()# 刷新页面

    def show_test_pass_state(self):
        self.ui_obj.result_lb.setText("通过")
        self.ui_obj.result_lb.setStyleSheet("font: 16pt \"Adobe Devanagari\";\n""color: rgb(0, 255, 0);")
        self.total_pass_cnt = self.total_pass_cnt+1
        self.ui_obj.pass_cnt_bt.setText(str(self.total_pass_cnt)+"通过")

        item=QStandardItem(common.get_datetime())
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor(0, 0, 0)))# 绿色
        self.history_model.setItem(self.current_history_max_row_index,0,item)

        item=QStandardItem('通过')
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor(0, 255, 0)))# 绿色
        self.history_model.setItem(self.current_history_max_row_index,1,item)
        self.current_history_max_row_index = self.current_history_max_row_index + 1
        QApplication.processEvents()# 刷新页面

    def show_test_fail_state(self):
        self.ui_obj.result_lb.setText("失败")
        self.ui_obj.result_lb.setStyleSheet("font: 16pt \"Adobe Devanagari\";\n""color: rgb(255, 0, 0);")
        self.total_fail_cnt = self.total_fail_cnt+1
        self.ui_obj.fail_cnt_bt.setText(str(self.total_fail_cnt)+"失败")

        item=QStandardItem(common.get_datetime())
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor(0, 0, 0)))
        self.history_model.setItem(self.current_history_max_row_index,0,item)

        item=QStandardItem('失败')
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor(255, 0, 0)))# 红色
        self.history_model.setItem(self.current_history_max_row_index,1,item)
        self.current_history_max_row_index = self.current_history_max_row_index + 1
        QApplication.processEvents()# 刷新页面

    def show_testcase_timeout(self):
        for i in range(0,3):
            item=QStandardItem('超时')
            item.setTextAlignment(Qt.AlignCenter)
            item.setForeground(QBrush(QColor(255, 0, 0)))# 红色
            self.testcase_model.setItem(self.current_testcase_max_row_index,i,item)
        self.current_testcase_max_row_index = self.current_testcase_max_row_index + 1
        QApplication.processEvents()# 刷新页面

    def show_test_case_recv_rssi(self, rssi):
        if rssi< self.sta_recv_rssi_thr:
            item=QStandardItem(str(rssi))
            item.setTextAlignment(Qt.AlignCenter)
            item.setForeground(QBrush(QColor(0, 255, 0)))# 绿色
            self.testcase_model.setItem(self.current_testcase_max_row_index,0,item)
            QApplication.processEvents()# 刷新页面
            return 0
        else:
            item=QStandardItem(str(rssi))
            item.setTextAlignment(Qt.AlignCenter)
            item.setForeground(QBrush(QColor(255, 0, 0)))# 红色
            self.testcase_model.setItem(self.current_testcase_max_row_index,0,item)
            QApplication.processEvents()# 刷新页面
            return 1

    def show_test_case_send_rssi(self, rssi):
        if rssi< self.sta_send_rssi_thr:
            item=QStandardItem(str(rssi))
            item.setTextAlignment(Qt.AlignCenter)
            item.setForeground(QBrush(QColor(0, 255, 0)))# 绿色
            self.testcase_model.setItem(self.current_testcase_max_row_index,1,item)
            QApplication.processEvents()# 刷新页面
            return 0
        else:
            item=QStandardItem(str(rssi))
            item.setTextAlignment(Qt.AlignCenter)
            item.setForeground(QBrush(QColor(255, 0, 0)))# 红色
            self.testcase_model.setItem(self.current_testcase_max_row_index,1,item)
            QApplication.processEvents()# 刷新页面
            return 1

    def show_test_case_pass(self):
        item=QStandardItem('通过')
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor(0, 255, 0)))# 绿色
        self.testcase_model.setItem(self.current_testcase_max_row_index,2,item)
        self.current_testcase_max_row_index = self.current_testcase_max_row_index + 1
        QApplication.processEvents()# 刷新页面

    def show_test_case_fail(self):
        item=QStandardItem('失败')
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(QBrush(QColor(255, 0, 0)))# 红色
        self.testcase_model.setItem(self.current_testcase_max_row_index,2,item)
        self.current_testcase_max_row_index = self.current_testcase_max_row_index + 1
        QApplication.processEvents()# 刷新页面