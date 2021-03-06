
'''
EE397 pyqt5 remote controller

'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
import socket
import sys

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        #socket
        self.sock = QTcpSocket()
        self.isConnect = False
        self.setupUi()
        self.setupSlot()
    def setupUi(self):
        self.resize(1069, 788)
        self.upButton = QtWidgets.QPushButton(self)
        self.upButton.setGeometry(QtCore.QRect(750, 490, 93, 28))
        self.upButton.setObjectName("upButton")
        self.upButton.setText("前进")
        self.leftButton = QtWidgets.QPushButton(self)
        self.leftButton.setGeometry(QtCore.QRect(650, 530, 93, 28))
        self.leftButton.setObjectName("leftButton")
        self.leftButton.setText("后退")
        self.rightButton = QtWidgets.QPushButton(self)
        self.rightButton.setGeometry(QtCore.QRect(850, 530, 93, 28))
        self.rightButton.setObjectName("rightButton")
        self.rightButton.setText("左转")
        self.downButton = QtWidgets.QPushButton(self)
        self.downButton.setGeometry(QtCore.QRect(750, 570, 93, 28))
        self.downButton.setObjectName("downButton")
        self.downButton.setText("右转")
        self.Connect = QtWidgets.QPushButton(self)
        self.Connect.setGeometry(QtCore.QRect(650, 680, 93, 28))
        self.Connect.setObjectName("Connect")
        self.Connect.setText("Connect")
        self.disConnect = QtWidgets.QPushButton(self)
        self.disConnect.setGeometry(QtCore.QRect(870, 680, 93, 28))
        self.disConnect.setObjectName("disConnect")
        self.disConnect.setText("Disconnect")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 581, 390))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.controlLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.controlLayout.setObjectName("controlLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText("BKP")
        self.controlLayout.addWidget(self.label)
        self.BKPEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.BKPEdit.setObjectName("BKPEdit")
        self.controlLayout.addWidget(self.BKPEdit)
        self.BKPSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.BKPSlider.setOrientation(QtCore.Qt.Horizontal)
        self.BKPSlider.setObjectName("BKPSlider")
        self.controlLayout.addWidget(self.BKPSlider)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("BKD")
        self.controlLayout.addWidget(self.label_2)
        self.BKDEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.BKDEdit.setObjectName("BKDEdit")
        self.controlLayout.addWidget(self.BKDEdit)
        self.BKDSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.BKDSlider.setOrientation(QtCore.Qt.Horizontal)
        self.BKDSlider.setObjectName("BKDSlider")
        self.controlLayout.addWidget(self.BKDSlider)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("VKP")
        self.controlLayout.addWidget(self.label_3)
        self.VKPEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.VKPEdit.setObjectName("VKPEdit")
        self.controlLayout.addWidget(self.VKPEdit)
        self.VKPSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.VKPSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VKPSlider.setObjectName("VKPSlider")
        self.controlLayout.addWidget(self.VKPSlider)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("VKI")
        self.controlLayout.addWidget(self.label_4)
        self.VKIEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.VKIEdit.setObjectName("VKIEdit")
        self.controlLayout.addWidget(self.VKIEdit)
        self.VKISlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.VKISlider.setOrientation(QtCore.Qt.Horizontal)
        self.VKISlider.setObjectName("VKISlider")
        self.controlLayout.addWidget(self.VKISlider)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("VKDEdit")
        self.controlLayout.addWidget(self.label_5)
        self.VKDEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.VKDEdit.setObjectName("VKDEdit")
        self.controlLayout.addWidget(self.VKDEdit)
        self.VKDSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.VKDSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VKDSlider.setObjectName("VKDSlider")
        self.controlLayout.addWidget(self.VKDSlider)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 480, 581, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.commandLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.commandLayout.setContentsMargins(0, 0, 0, 0)
        self.commandLayout.setObjectName("commandLayout")
        self.commandBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.commandBrowser.setObjectName("commandBrowser")
        self.commandLayout.addWidget(self.commandBrowser)
        self.CommandEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.CommandEdit.setText("")
        self.CommandEdit.setObjectName("CommandEdit")
        self.commandLayout.addWidget(self.CommandEdit)


        #setup slider
        self.setSlider()

    def setupSlot(self):
        #Slot connect#
        self.Connect.clicked.connect(self.SockConnect)
        #按下回车时，发出指令
        self.CommandEdit.returnPressed.connect(self.WriteCommand)
        # self.disConnect.click.connect(self.SockDisConnect)
        #Value changed in Edit
        self.BKPEdit.returnPressed.connect(self.BKPEdit2Slider)
        self.BKDEdit.returnPressed.connect(self.BKDEdit2Slider)
        self.VKPEdit.returnPressed.connect(self.VKPEdit2Slider)
        self.VKIEdit.returnPressed.connect(self.VKIEdit2Slider)
        self.VKDEdit.returnPressed.connect(self.VKDEdit2Slider)
        self.BKPEdit.returnPressed.connect(self.sendBKP)
        self.BKDEdit.returnPressed.connect(self.sendBKD)
        self.VKPEdit.returnPressed.connect(self.sendVKP)
        self.VKIEdit.returnPressed.connect(self.sendVKI)
        self.VKDEdit.returnPressed.connect(self.sendVKD)

        #Value changed in Slider
        self.BKPSlider.valueChanged.connect(self.BKPSlider2Edit)
        self.BKDSlider.valueChanged.connect(self.BKDSlider2Edit)
        self.VKPSlider.valueChanged.connect(self.VKPSlider2Edit)
        self.VKISlider.valueChanged.connect(self.VKISlider2Edit)
        self.VKDSlider.valueChanged.connect(self.VKDSlider2Edit)

        #按钮信号处理
        self.upButton.clicked.connect(self.upButtonClicked)
        self.downButton.clicked.connect(self.downButtonClicked)
        self.leftButton.clicked.connect(self.leftButtonClicked)
        self.rightButton.clicked.connect(self.rightButtonClicked)

        self.commandBrowser.textChanged.connect(self.cmdBrowserRollDown)
        #键盘事件控制:

    def cmdBrowserRollDown(self):
        self.commandBrowser.moveCursor(QTextCursor.End)

    def setSlider(self):
        #initialize slider paras
        self.BKDSlider.setRange(-100,100)
        self.BKPSlider.setRange(-100,100)
        self.VKPSlider.setRange(-200,200)
        self.VKDSlider.setRange(-200,200)
        self.VKISlider.setRange(-200,200)
        self.BKPSlider.setTickPosition(QSlider.TicksBelow)
        self.BKDSlider.setTickPosition(QSlider.TicksBelow)
        self.VKPSlider.setTickPosition(QSlider.TicksBelow)
        self.VKISlider.setTickPosition(QSlider.TicksBelow)
        self.VKDSlider.setTickPosition(QSlider.TicksBelow)
        self.BKDSlider.setTickInterval(1)
        self.BKPSlider.setTickInterval(1)
        self.VKPSlider.setTickInterval(1)
        self.VKISlider.setTickInterval(1)
        self.VKDSlider.setTickInterval(1)

    def SockConnect(self):
        if self.isConnect ==True:
            return False
        else:
            IP ='101.132.151.237'
            Port = 81
            self.sock.connectToHost(IP,Port)
            if not self.sock.waitForConnected(2500):
                self.commandBrowser.setText("连接失败\n")
                return False

            else:
                print('writing')
                data = QByteArray()
                stream = QDataStream()
                txstring = 'bala_control 2222'
                self.sock.write(txstring.encode('utf-8'))
                self.sock.waitForBytesWritten()
            #
            self.commandBrowser.insertPlainText("连接成功!\n")
            self.isConnect =True

            self.sock.readyRead.connect(self.on_socket_receive)

            return True

    def WriteCommand(self):
        #check command
        self.checkcmd(self.CommandEdit.text())
        self.CommandEdit.clear()

    def checkcmd(self,Message):
        #去除空格
        Message.replace(' ','')
        #get text from Lineedit and show in browser
        self.commandBrowser.insertPlainText('Wrote: '+Message+'\n')
        if Message =='clear':
            self.commandBrowser.clear()
        elif Message =='connect':
            self.SockConnect()

        else:
            if self.isConnect ==True:
                self.sock.write(Message.encode('utf-8'))

    #专门用于发送小车控制指令的函数
    def SendMotionControl(self,cmd):
        if self.isConnect == True:
            self.sock.write(cmd.encode('utf-8'))


    def on_socket_receive(self):
        try:

            mesg = self.sock.readAll()

            mesg = mesg.data().decode('utf-8')
            self.commandBrowser.insertPlainText('Received: '+mesg+'\n')
        except:
            print('error')


    def BKPEdit2Slider(self):
        value = float(self.BKPEdit.text())*10
        self.BKPSlider.setValue(value)
        Txstring = '#'
    def BKDEdit2Slider(self):
        value = float(self.BKDEdit.text())*10
        self.BKDSlider.setValue(value)


    def VKPEdit2Slider(self):
        value = float(self.VKPEdit.text())*10
        self.VKPSlider.setValue(value)

    def VKIEdit2Slider(self):
        value = float(self.VKIEdit.text())*10
        self.VKISlider.setValue(value)

    def VKDEdit2Slider(self):
        value = float(self.VKDEdit.text())*10
        self.VKDSlider.setValue(value)

    def BKPSlider2Edit(self):
        value = self.BKPSlider.value()/10
        self.BKPEdit.setText(str(value))

    def BKDSlider2Edit(self):
        value = self.BKDSlider.value()/10
        self.BKDEdit.setText(str(value))

    def VKPSlider2Edit(self):
        value = self.VKPSlider.value()/10
        self.VKPEdit.setText(str(value))

    def VKISlider2Edit(self):
        value = self.VKISlider.value()/10
        self.VKIEdit.setText(str(value))

    def VKDSlider2Edit(self):
        value = self.VKDSlider.value()/10
        self.VKDEdit.setText(str(value))


    def sendBKP(self):
        cmd_string = '#K1#'+self.BKDEdit.text()+'#'
        self.checkcmd(cmd_string)

    def sendBKD(self):
        cmd_string = '#K2#'+self.BKDEdit.text()+'#'
        self.checkcmd(cmd_string)

    def sendVKP(self):
        cmd_string = '#K3#'+self.BKDEdit.text()+'#'
        self.checkcmd(cmd_string)

    def sendVKI(self):
        cmd_string = '#K4#'+self.BKDEdit.text()+'#'
        self.checkcmd(cmd_string)

    def sendVKD(self):
        cmd_string = '#K5#'+self.BKDEdit.text()+'#'
        self.checkcmd(cmd_string)

    def upButtonClicked(self):
        cmd_string = 'W'
        self.SendMotionControl(cmd = cmd_string)
        self.commandBrowser.insertPlainText('Wrote:'+cmd_string+'\n')

    def downButtonClicked(self):
        cmd_string = 'S'
        self.SendMotionControl(cmd = cmd_string)
        self.commandBrowser.insertPlainText('Wrote:'+cmd_string+'\n')

    def leftButtonClicked(self):
        cmd_string = 'A'
        self.SendMotionControl(cmd = cmd_string)
        self.commandBrowser.insertPlainText('Wrote:'+cmd_string+'\n')

    def rightButtonClicked(self):
        cmd_string = 'D'
        self.SendMotionControl(cmd = cmd_string)
        self.commandBrowser.insertPlainText('Wrote:'+cmd_string+'\n')


app = QtWidgets.QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(app.exec_())