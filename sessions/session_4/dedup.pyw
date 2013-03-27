#!/usr/bin/env python

import glob
import sys

from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QComboBox, QDialog, QVBoxLayout, QTextBrowser, QFileDialog,
                         QGridLayout, QLabel, QPushButton, QCheckBox, QLineEdit, QTableView)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browseButton = QPushButton("Browse")
	self.fileDialog = QFileDialog()
        layout = QGridLayout()
	layout.addWidget(self.browseButton, 0, 0)
        self.setLayout(layout)
        self.browseButton.clicked.connect(self.browse)

    def browse(self):
	self.fileDialog.show() 
   
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
