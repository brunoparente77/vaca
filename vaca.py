 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:03:00 2023

@author: bruno parente
"""

import os
import sys
import math
import time

from PySide6 import QtSvg
from PySide6.QtCore import (
    QUrl,
    Qt,
    QPointF
)
from PySide6.QtCore import __version__ as pyside_version
from PySide6.QtGui import (
    QAction,
    QIcon,
    QFont,
    QFontDatabase,
    QFontInfo,
    QPixmap
)
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QToolBar,
    QSplashScreen
)

from platform import python_version
from ui_main_vaca import Ui_MainWindow

basedir = os.path.dirname(__file__)

# gambi pro ícone no Windows...
try:
    # Only exists on Windows.
    from ctypes import windll

    myappid = "edu.eu.vaca.v1"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Adicionando as fontes Ubuntu Mono
        QFontDatabase.addApplicationFont(os.path.join(basedir,"UbuntuMono-Regular.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir,"UbuntuMono-Bold.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir,"UbuntuMono-BoldItalic.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir,"UbuntuMono-Italic.ttf"))
        # barra de botões
        button_calc = QAction("Calcular", self)
        button_calc.setStatusTip("This is your button")
        button_calc.triggered.connect(self.calcular)
        self.toolBar.addAction(button_calc)
        

    def calcular(self):
        # extarindo o array
        table_array = []
        for i in range(self.tableData.columnCount()):
            col = []
            table_array.append(col)
            for j in range(self.tableData.rowCount()):
                item = self.tableData.item(j, i)
                if item is not None:
                    if item.text().strip():
                        text = item.text().replace(",", ".")
                        col.append(float(text))
        print(table_array)
        
        
        
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "icon.svg")))
# Load styles
with open('vaca.qss', 'r') as f:
    _style = f.read()
    app.setStyleSheet(_style)
pixmap = QPixmap(os.path.join(basedir,"splash.jpg"))
splash = QSplashScreen(pixmap)
splash.show()
# App
window = MainWindow()
window.show()

app.exec()