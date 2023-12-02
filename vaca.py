 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:03:00 2023

@author: bruno parente
"""

import os
import sys
import math
import statistics

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
    QPixmap,
    QColor
)
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QToolBar,
    QTableWidget,
    QTableWidgetItem
)

from platform import python_version
from ui_main_vaca import Ui_MainWindow
from vaca_conf import check_conformidade

basedir = os.path.dirname(__file__)

# gambi pro ícone no Windows...
try:
    # Only exists on Windows.
    from ctypes import windll

    myappid = "edu.eu.vaca.v1"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


def calc_z(tw, ta, ua, pa):
    ro_w = 0.99997495 * (1 - (tw - 3.983035)**2 * (tw + 301.797)/(522528.9 * (tw + 69.34881)))
    ro_a = (1 / 1000) * (0.34848 * pa - 0.009 * ua * math.e**(0.061 * ta))/(ta + 273.15)
    z = 1 / (ro_w - ro_a) * (1 - ro_a / 8)
    return z


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
        button_calc = QAction(QIcon(os.path.join(basedir,"calc_icon.svg")), "Calcular", self)
        button_calc.triggered.connect(self.calcular)
        self.toolBar.addAction(button_calc)
        button_relat = QAction(QIcon(os.path.join(basedir,"relat_icon.svg")), "Relatório", self)
        button_relat.triggered.connect(self.relat)
        self.toolBar.addAction(button_relat)
        #populando drop list com o multiplicador pra apresentar o resultado em µL ou mL
        self.instKind.addItem("Balão volumétrico", 1)
        self.instKind.addItem("Bureta", 1)
        self.instKind.addItem("Bureta 'digital'", 1)
        self.instKind.addItem("Dispensador", 1)
        self.instKind.addItem("Micropipeta de vol. fixo", 1000)
        self.instKind.addItem("Micropipeta de vol. variável", 1000)
        self.instKind.addItem("Micropipeta multicanal", 1000)
        self.instKind.addItem("Pipeta graduada", 1)
        self.instKind.addItem("Pipeta volumétrica", 1)
        # conecta o combo pra mudar as unidades entre µL e mL
        self.instKind.currentIndexChanged.connect(self.muda_unidade)
    
    def muda_unidade(self):
        if self.instKind.currentData() == 1:
            self.tableData.setVerticalHeaderItem(0, QTableWidgetItem("Volume nominal, em mL"))
            self.tableData.setVerticalHeaderItem(1, QTableWidgetItem("Volume ensaiado, em mL"))
            self.tableRes.setVerticalHeaderItem(0, QTableWidgetItem("Volume medido, em mL"))
        else:
            self.tableData.setVerticalHeaderItem(0, QTableWidgetItem("Volume nominal, em µL"))
            self.tableData.setVerticalHeaderItem(1, QTableWidgetItem("Volume ensaiado, em µL"))
            self.tableRes.setVerticalHeaderItem(0, QTableWidgetItem("Volume medido, em µL"))


    def calcular(self):
        mult = self.instKind.currentData()
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
        ta = self.tempAmb.value()
        pa = self.presAtm.value()
        ua = self.umidRel.value()
        vol_array = []
        for d in table_array:
            if len(d) != 0:
                vol0 = []
                z = calc_z(d[2], ta, ua, pa)
                for i in d:
                    vol0.append(i * z * mult)
                vol = [y - x for x, y in zip(vol0, vol0[1:])]
                vol[0] = d[0]
                vol[1] = d[1]
                vol[2] = d[3] * z * mult
                vol_array.append(vol)
        res_array = []
        for i in vol_array:
            res = []
            mean = statistics.mean(i[2:])
            res.append(mean)
            e_sis = 100 * (mean - i[1])/i[1]
            res.append(e_sis)
            e_ale = 100 * statistics.stdev(i[2:]) / i[1]
            res.append(e_ale)
            res_array.append(res)
        for i, j in enumerate(res_array):
            for x, y in enumerate(j):
                self.tableRes.setItem(x, i, QTableWidgetItem("%.2f" % y))
        self.tableRes.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        for column in range(self.tableRes.columnCount()):
            _item = self.tableRes.item(1, column)
            if _item:
                conf = check_conformidade("msa",
                                   float(self.tableData.item(0,column).text()),
                                   float(self.tableData.item(1,column).text()),
                                   abs(float(_item.text())),
                                   True)
                print(conf)

    def relat(self):
        print("ainda não")
            

        
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "icon.svg")))
# Load styles
with open('vaca.qss', 'r') as f:
    _style = f.read()
    app.setStyleSheet(_style)
# App
window = MainWindow()
window.show()

app.exec()