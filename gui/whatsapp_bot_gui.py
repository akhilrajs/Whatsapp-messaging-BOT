# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'whatsapp_bot_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.phone_numbers_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.phone_numbers_box.setGeometry(QtCore.QRect(30, 100, 131, 341))
        self.phone_numbers_box.setObjectName("phone_numbers_box")
        self.names_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.names_box.setGeometry(QtCore.QRect(170, 100, 161, 341))
        self.names_box.setObjectName("names_box")
        self.phone_numbers_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_numbers_label.setGeometry(QtCore.QRect(30, 70, 111, 29))
        self.phone_numbers_label.setObjectName("phone_numbers_label")
        self.names_label = QtWidgets.QLabel(self.centralwidget)
        self.names_label.setGeometry(QtCore.QRect(170, 70, 111, 29))
        self.names_label.setObjectName("names_label")
        self.country_code_label = QtWidgets.QLabel(self.centralwidget)
        self.country_code_label.setGeometry(QtCore.QRect(30, 10, 90, 30))
        self.country_code_label.setObjectName("country_code_label")
        self.country_code = QtWidgets.QLineEdit(self.centralwidget)
        self.country_code.setGeometry(QtCore.QRect(120, 10, 113, 30))
        self.country_code.setObjectName("country_code")
        self.greet_recipient = QtWidgets.QCheckBox(self.centralwidget)
        self.greet_recipient.setGeometry(QtCore.QRect(30, 510, 120, 20))
        self.greet_recipient.setObjectName("greet_recipient")
        self.send_messages_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_messages_button.setGeometry(QtCore.QRect(30, 540, 120, 31))
        self.send_messages_button.setStyleSheet("font: 81 8pt \"Mukta Malar ExtraBold\";")
        self.send_messages_button.setObjectName("send_messages_button")
        self.send_messages_button.clicked.connect(self.pass_to_collect_data)
        self.activity_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.activity_log.setGeometry(QtCore.QRect(710, 370, 490, 291))
        self.activity_log.setMouseTracking(True)
        self.activity_log.setAutoFillBackground(False)
        self.activity_log.setStyleSheet("background-color : rgb(255, 255, 222)")
        self.activity_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.activity_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.activity_log.setObjectName("activity_log")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 640, 641, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.total_recipients_label = QtWidgets.QLabel(self.centralwidget)
        self.total_recipients_label.setGeometry(QtCore.QRect(180, 540, 100, 16))
        self.total_recipients_label.setObjectName("total_recipients_label")
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(30, 620, 101, 16))
        self.progress_label.setObjectName("progress_label")
        self.message_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message_box.setGeometry(QtCore.QRect(710, 10, 490, 351))
        self.message_box.setObjectName("message_box")
        self.total_recipients_number = QtWidgets.QLabel(self.centralwidget)
        self.total_recipients_number.setGeometry(QtCore.QRect(280, 540, 101, 16))
        self.total_recipients_number.setObjectName("total_recipients_number")
        self.failed_label = QtWidgets.QLabel(self.centralwidget)
        self.failed_label.setGeometry(QtCore.QRect(180, 560, 110, 16))
        self.failed_label.setObjectName("failed_label")
        self.failed_number_label = QtWidgets.QLabel(self.centralwidget)
        self.failed_number_label.setGeometry(QtCore.QRect(280, 560, 101, 16))
        self.failed_number_label.setObjectName("failed_number_label")
        self.failed_numbers_label = QtWidgets.QLabel(self.centralwidget)
        self.failed_numbers_label.setGeometry(QtCore.QRect(370, 80, 111, 29))
        self.failed_numbers_label.setObjectName("failed_numbers_label")
        self.failed_names_label = QtWidgets.QLabel(self.centralwidget)
        self.failed_names_label.setGeometry(QtCore.QRect(510, 80, 111, 29))
        self.failed_names_label.setObjectName("failed_names_label")
        self.failed_numbers_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.failed_numbers_box.setGeometry(QtCore.QRect(370, 110, 131, 331))
        self.failed_numbers_box.setPlainText("")
        self.failed_numbers_box.setObjectName("failed_numebrs_box")
        self.failed_names_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.failed_names_box.setGeometry(QtCore.QRect(510, 110, 161, 331))
        self.failed_names_box.setPlainText("")
        self.failed_names_box.setObjectName("faile_names_box")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(350, 50, 3, 440))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.failed_list_header = QtWidgets.QLabel(self.centralwidget)
        self.failed_list_header.setGeometry(QtCore.QRect(370, 50, 111, 29))
        self.failed_list_header.setObjectName("failed_list_header")
        self.recipients_header = QtWidgets.QLabel(self.centralwidget)
        self.recipients_header.setGeometry(QtCore.QRect(30, 50, 111, 29))
        self.recipients_header.setObjectName("recipients_header")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(690, 50, 3, 440))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 490, 690, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 50, 690, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(30, 580, 93, 30))
        self.quit_button.setStyleSheet("font: 81 8pt \"Nunito Sans ExtraBold\";\n"
"")
        self.quit_button.setObjectName("quit_button")
        self.open_logs_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_logs_button.setGeometry(QtCore.QRect(560, 500, 110, 28))
        self.open_logs_button.setObjectName("open_logs_button")
        self.open_whatsapp_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_whatsapp_button.setGeometry(QtCore.QRect(560, 530, 110, 28))
        self.open_whatsapp_button.setObjectName("open_whatsapp_button")
        self.time_taken_label = QtWidgets.QLabel(self.centralwidget)
        self.time_taken_label.setGeometry(QtCore.QRect(180, 580, 110, 16))
        self.time_taken_label.setObjectName("time_taken_label")
        self.time_taken_number = QtWidgets.QLabel(self.centralwidget)
        self.time_taken_number.setGeometry(QtCore.QRect(280, 580, 101, 16))
        self.time_taken_number.setObjectName("time_taken_number")
        self.send_again_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_again_button.setGeometry(QtCore.QRect(560, 450, 110, 28))
        self.send_again_button.setObjectName("send_again_button")
        self.export_list_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_list_button.setGeometry(QtCore.QRect(440, 450, 110, 28))
        self.export_list_button.setObjectName("export_list_button")
        self.online_status_label = QtWidgets.QLabel(self.centralwidget)
        self.online_status_label.setGeometry(QtCore.QRect(180, 520, 100, 16))
        self.online_status_label.setObjectName("online_status_label")
        self.online_status = QtWidgets.QLabel(self.centralwidget)
        self.online_status.setGeometry(QtCore.QRect(280, 520, 101, 16))
        self.online_status.setObjectName("online_status")
        self.load_previous_session_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_previous_session_button.setGeometry(QtCore.QRect(179, 450, 151, 28))
        self.load_previous_session_button.setObjectName("load_previous_session_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
        self.menubar.setObjectName("menubar")
        self.menuauthor_Akhil_Raj_S = QtWidgets.QMenu(self.menubar)
        self.menuauthor_Akhil_Raj_S.setObjectName("menuauthor_Akhil_Raj_S")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuauthor_Akhil_Raj_S.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.phone_numbers_box.setPlainText(_translate("MainWindow", "999999999\n"
""))
        self.names_box.setPlainText(_translate("MainWindow", "name\n"
""))
        self.phone_numbers_label.setText(_translate("MainWindow", "Phone numbers "))
        self.names_label.setText(_translate("MainWindow", "Names"))
        self.country_code_label.setText(_translate("MainWindow", "Country Code :"))
        self.country_code.setText(_translate("MainWindow", "+91"))
        self.greet_recipient.setText(_translate("MainWindow", "greet recipients "))
        self.send_messages_button.setText(_translate("MainWindow", "SEND MESSAGES"))
        self.activity_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">[#] activity log ...</span></p></body></html>"))
        self.total_recipients_label.setText(_translate("MainWindow", "Total recipients :"))
        self.progress_label.setText(_translate("MainWindow", "Progress :"))
        self.message_box.setPlainText(_translate("MainWindow", "type your message here \n"
"or \n"
"enter the url of the GitHub page containing the message here"))
        self.total_recipients_number.setText(_translate("MainWindow", "0"))
        self.failed_label.setText(_translate("MainWindow", "Failed              : "))
        self.failed_number_label.setText(_translate("MainWindow", "0"))
        self.failed_numbers_label.setText(_translate("MainWindow", "Failed numbers"))
        self.failed_names_label.setText(_translate("MainWindow", "Failed names"))
        self.failed_list_header.setText(_translate("MainWindow", "Failed to send to :"))
        self.recipients_header.setText(_translate("MainWindow", "Recipients :"))
        self.quit_button.setText(_translate("MainWindow", "QUIT"))
        self.open_logs_button.setText(_translate("MainWindow", "Open Logs"))
        self.open_whatsapp_button.setText(_translate("MainWindow", "Open Whatsapp"))
        self.time_taken_label.setText(_translate("MainWindow", "Time taken      :"))
        self.time_taken_number.setText(_translate("MainWindow", "0"))
        self.send_again_button.setText(_translate("MainWindow", "SEND AGAIN"))
        self.export_list_button.setText(_translate("MainWindow", "EXPORT LIST"))
        self.online_status_label.setText(_translate("MainWindow", "Online Status   :"))
        self.online_status.setText(_translate("MainWindow", "Offline"))
        self.load_previous_session_button.setText(_translate("MainWindow", "Load Previous Session"))
        self.menuauthor_Akhil_Raj_S.setTitle(_translate("MainWindow", "author : akhil_raj_s_"))
    
    #displaying everything the program is doing in the activity box 
    def log(self,log_data):
        from time import sleep
        sleep(0.2)
        self.activity_log.moveCursor(QTextCursor.End)
        self.activity_log.append(str(log_data))
        self.activity_log.ensureCursorVisible()
        
    #a function to collect all the data once the send button is clicked
    def pass_to_collect_data(self):
        self.failed_names_box.clear()
        self.failed_numbers_box.clear()
        cd = threading.Thread(target = lambda:collect_data(self))
        cd.start()
        
    # the funtion to send the messages
    def pass_to_send_messages(self):
        sm = threading.Thread(target = lambda:send_messages(self))
        sm.start()
        
        



#collecting the data
def collect_data(self):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    from socket import create_connection; is_online = True if create_connection(('www.google.com', 80), timeout=3) else False
    if is_online == True:
        self.online_status.setText(_translate("MainWindow", "ONLINE"))
    # cc = country code
    # num_list = list of the phone numbers
    # name_list = list of the names
    # greet = whether to greet or not
    # msg = to store the message to sent to the receivers
    global cc, num_list, name_list, greet, msg
    cc = str(self.country_code.text())
    self.log("[#] " + "Country code : " + cc)
    num_list = []
    num_list = (self.phone_numbers_box.toPlainText().splitlines())
    self.log("[#] " + "Total numbers loaded : " + str(len(num_list)))
    name_list = []
    name_list = (self.names_box.toPlainText().splitlines())
    self.total_recipients_number.setText(_translate("MainWindow", str(len(name_list))))
    self.log("[#] " + "Total names loaded : " + str(len(name_list)))
    # checking if there are equal number of names and numbers
    if len(num_list) != len(name_list):
        self.log("[!!!] the total number of names and numbers do not match")
        self.log("[!!!] check the names and numbers and try again")
        sys.exit(app.exec_())
    greet = (self.greet_recipient.isChecked())
    if greet == True:
        self.log("[#] The recipient will be greeted")
    else:
        self.log("[#] The recipient will not be greeted")
    msg = self.message_box.toPlainText()
    self.log('''[#] the message to be send is :
''' + str(msg))
    self.pass_to_send_messages()


# the function for sending messages
def send_messages(self):
    print()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())