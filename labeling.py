import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200        
        self.file_index = 1
        self.initUI()
        #self.filename = './data/1.png'
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        

        button = QPushButton('labeling', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        
        button2 = QPushButton('reverse', self)
        button2.setToolTip('This is an example button')
        button2.move(100,180)
        button2.clicked.connect(self.on_click_rev)

        self.label_img = QLabel(self)
        self.label_img.setPixmap(QPixmap('./data/' + str(self.file_index) + '.png'))
        self.label_img.move(100, 100)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.returnPressed.connect(self.on_click)
        #windowExample = QtWidgets.QWidget()
        '''
        labelA.setText('Label Example')
            labelB.setPixmap(QtGui.QPixmap('python.jpg'))
            windowExample.setWindowTitle('Label Example')
            windowExample.setGeometry(100, 100, 300, 200)
            labelA.move(100, 40)
            labelB.move(120, 120)
            windowExample.show()
        '''
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        if len(textboxValue) < 4:
            return
        output = './data/' + str(self.file_index) + '.png' + ' ' + textboxValue + '\n'
        with open('label.txt', 'a') as f:
            f.write(output)
        self.file_index = self.file_index + 1
        self.label_img.setPixmap(QPixmap('./data/' + str(self.file_index) + '.png'))
        self.textbox.setText('')
        print('PyQt5 button click')

    def on_click_rev(self):
        self.file_index = self.file_index - 1
        self.label_img.setPixmap(QPixmap('./data/' + str(self.file_index) + '.png'))
        self.textbox.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
