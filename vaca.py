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
    # densidade da água segundo "Tanaka M. et al., Recommended table
    # for the density of water between 0 °C and 40 °C based on
    # recent experimental reports,  Metrologia,  2001, 38, 301-309  
    ro_w = 0.99997495 * (1 - (tw - 3.983035)**2 * (tw + 301.797)/(522528.9 * (tw + 69.34881)))
    # Densidade do ar de acordo com a ISO 8655-6:2022
    ro_a = (1 / 1000) * (0.34848 * pa - 0.009 * ua * math.e**(0.061 * ta))/(ta + 273.15)
    # cálculo de z de acordo com a ISO 8655-6:2022
    z = 1 / (ro_w - ro_a) * (1 - ro_a / 8)
    return z


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Adicionando as fontes Cantarell
        QFontDatabase.addApplicationFont(os.path.join(basedir,"Cantarell-Regular.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir,"Cantarell-Bold.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir,"Cantarell-BoldItalic.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir,"Cantarell-Italic.ttf"))
        # barra de botões
        button_calc = QAction(QIcon(os.path.join(basedir,"calc_icon.svg")), "Calcular", self)
        button_calc.triggered.connect(self.calcular)
        self.toolBar.addAction(button_calc)
        button_relat = QAction(QIcon(os.path.join(basedir,"relat_icon.svg")), "Relatório", self)
        button_relat.triggered.connect(self.relat)
        self.toolBar.addAction(button_relat)
        # populando drop list com o multiplicador pra apresentar o resultado em µL ou mL
        # e tipo de instrumento
        self.instKind.addItem("Balão volumétrico", (1, "bv"))
        self.instKind.addItem("Bureta", (1, "b"))
        self.instKind.addItem("Bureta 'digital' manual", (1, "bdm"))
        self.instKind.addItem("Bureta digital motorizada", (1, "bda"))
        self.instKind.addItem("Dispensador", (1, "d"))
        self.instKind.addItem("Micropipeta tipo A|D1", (1000, "msa"))
        self.instKind.addItem("Micropipeta tipo D2", (1000, "msd2"))
        self.instKind.addItem("Micropipeta multicanal", (1000, "mm"))
        self.instKind.addItem("Pipeta graduada", (1, "pg"))
        self.instKind.addItem("Pipeta volumétrica", (1, "pv"))
        # conecta o combo pra mudar as unidades entre µL e mL
        self.instKind.currentIndexChanged.connect(self.muda_unidade)
    
    def muda_unidade(self):
        # troca a unidade da interface de acordo com a unidade de volume do instrumento
        if self.instKind.currentData()[0] == 1:
            self.tableData.setVerticalHeaderItem(0, QTableWidgetItem("Volume nominal, em mL"))
            self.tableData.setVerticalHeaderItem(1, QTableWidgetItem("Volume ensaiado, em mL"))
            self.tableRes.setVerticalHeaderItem(0, QTableWidgetItem("Volume medido, em mL"))
        else:
            self.tableData.setVerticalHeaderItem(0, QTableWidgetItem("Volume nominal, em µL"))
            self.tableData.setVerticalHeaderItem(1, QTableWidgetItem("Volume ensaiado, em µL"))
            self.tableRes.setVerticalHeaderItem(0, QTableWidgetItem("Volume medido, em µL"))

    def calcular(self):
        # resgatando qual multiplicador usar para calcular em mL ou µL
        mult = self.instKind.currentData()[0]
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
        # extraindo as condições ambientais
        ta = self.tempAmb.value()
        pa = self.presAtm.value()
        ua = self.umidRel.value()
        # transformando massa em volume
        vol_array = []
        for d in table_array:
            if len(d) != 0:
                vol0 = []
                # cálculo de z
                z = calc_z(d[2], ta, ua, pa)
                for i in d:
                    vol0.append(i * z * mult)
                vol = [y - x for x, y in zip(vol0, vol0[1:])]
                # restaurando o volume nominal e ensaiado
                vol[0] = d[0]
                vol[1] = d[1]
                # Reinnserindo o primeiro dado que o "zip" come no processo
                vol[2] = d[3] * z * mult
                vol_array.append(vol)
        # calculando o resultado e salvando em uma nova matriz
        res_array = []
        for i in vol_array:
            res = []
            # a média das medidas
            mean = statistics.mean(i[2:])
            res.append(mean)
            # o erro sistemático como um percentual do volume ensaiado
            e_sis = 100 * (mean - i[1])/i[1]
            res.append(e_sis)
            # o erro aleatório em percentual. Na prática, um CV
            e_ale = 100 * statistics.stdev(i[2:]) / i[1]
            res.append(e_ale)
            res_array.append(res)
        # atribuindo os resultados à tabela tableRes da interface
        for i, j in enumerate(res_array):
            for x, y in enumerate(j):
                self.tableRes.setItem(x, i, QTableWidgetItem("%.2f" % y))
        # Não é legal o usuário poder editar os resultos. Bloqueando!
        self.tableRes.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # Calculando os limites, de acordo com a norma ISO do instrumento
        match self.instKind.currentData()[1]:
            case "msa":
                # comparando o erro sistemático com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(1, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-2:2022
                        if v_nom > 5000:
                            e_vnom = 0.6
                        elif v_nom > 50:
                            e_vnom = 0.8
                        elif v_nom > 10:
                            e_vnom = 1.0
                        elif v_nom > 5:
                            e_vnom = 1.2
                        else:
                            e_vnom = 2.5                    
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8855-2:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
                # comparando o erro aleatório com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(2, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-2:2022
                        if v_nom > 50:
                            e_vnom = 0.3
                        elif v_nom > 10:
                            e_vnom = 0.5
                        elif v_nom > 5:
                            e_vnom = 0.8
                        elif v_nom > 3:
                            e_vnom = 1.5
                        else:
                            e_vnom = 2.0
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8655-2:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
            case "msd2":
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(1, column)               
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-2:2022
                        if v_nom > 100:
                            e_vnom = 1.2
                        elif v_nom > 20:
                            e_vnom = 1.4
                        elif v_nom > 5:
                            e_vnom = 2.0
                        else:
                            e_vnom = 2.5
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8855-2:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
                # comparando o erro aleatório com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(2, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-2:2022
                        if v_nom > 100:
                            e_vnom = 0.4
                        elif v_nom > 20:
                            e_vnom = 0.6
                        elif v_nom > 10:
                            e_vnom = 0.8
                        elif v_nom > 5:
                            e_vnom = 1.0
                        else:
                            e_vnom = 1.5
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8855-2:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
            case "mm":
                # comparando o erro sistemático com o limite da norma
                for column in range(self.tableRes.columnCount()):                
                    _item = self.tableRes.item(1, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-2:2022
                        if v_nom > 50:
                            e_vnom = 1.6
                        elif v_nom > 10:
                            e_vnom = 2.0
                        elif v_nom > 5:
                            e_vnom = 2.4
                        elif v_nom > 2:
                            e_vnom = 5.0
                        else:
                            e_vnom = 8.0
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8855-2:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
                # comparando o erro aleatório com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(2, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-2:2022
                        if v_nom > 50:
                            e_vnom = 0.6
                        elif v_nom > 20:
                            e_vnom = 0.8
                        elif v_nom > 10:
                            e_vnom = 1.0
                        elif v_nom > 5:
                            e_vnom = 1.6
                        elif v_nom > 2:
                            e_vnom = 3.0
                        else:
                            e_vnom = 8.0
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8655-2:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
            case "bda":
                # comparando o erro sistemático com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    item = self.tableRes.item(1, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0, column).text())
                        v_s = float(self.tableData.item(1, column).text())
                        # verificando qual o limite dos erros na ISO 8655-3:2022
                        if v_nom > 5:
                            e_vnom = 0.2
                        elif v_nom > 2:
                            e_vnom = 0.3
                        elif v_nom > 1:
                            e_vnom = 0.5
                        else:
                            e_vnom = 0.6
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8855-3:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
                # comparando o erro aleatório com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(2, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0, column).text())
                        v_s = float(self.tableData.item(1, column).text())
                        # verificando qual o limite dos erros na ISO 8655-3:2022
                        if v_nom > 50:
                            e_vnom = 0.03
                        elif v_nom > 25:
                            e_vnom = 0.05
                        elif v_nom > 5:
                            e_vnom = 0.07
                        else:
                            e_vnom = 0.1
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8655-3:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
            case "bdm":
                # comparando o erro sistemático com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(1, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-3:2022
                        if v_nom > 10:
                            e_vnom = 0.2
                        elif v_nom > 2:
                            e_vnom = 0.3
                        elif v_nom > 1:
                            e_vnom = 0.5
                        else:
                        e_vnom = 0.6
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8855-3:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
                # comparando o erro aleatório com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(2, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-3:2022
                        e_vnom = 0.1
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8655-3:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
            case "d":
                # comparando o erro sistemático com o limite da norma
                for column in range(self.tableRes.columnCount()):                
                    _item = self.tableRes.item(1, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-5:2022
                        if v_nom > 0.5:
                            e_vnom = 0.6
                        elif v_nom > 0.1:
                            e_vnom = 1.0
                        elif v_nom > 0.02:
                            e_vnom = 1.5
                        else:
                            e_vnom = 2.0
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8855-5:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))
                # comparando o erro aleatório com o limite da norma
                for column in range(self.tableRes.columnCount()):
                    _item = self.tableRes.item(2, column)
                    if _item:
                        v_nom =  float(self.tableData.item(0,column).text())
                        v_s = float(self.tableData.item(1,column).text())
                        # verificando qual o limite dos erros na ISO 8655-5:2022
                        if v_nom > 0.2:
                            e_vnom = 0.2
                        elif v_nom > 0.05:
                            e_vnom = 0.3
                        elif v_nom > 0.02:
                            e_vnom = 0.4
                        elif v_nom > 0.01:
                            e_vnom = 0.5
                        else:
                            e_vnom = 1.0
                        limite = v_nom / v_s * e_vnom
                        if abs(float(_item.text())) > limite:
                            conf = False
                        else:
                            conf = True
                        if not conf:
                            _item.setToolTip("Deu ruim de acordo com a norma ISO 8655-5:2022.")
                            _item.setIcon(QIcon(os.path.join(basedir, "alert.svg")))


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