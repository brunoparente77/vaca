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

from datetime import datetime
from PySide6 import QtSvg, QtPrintSupport
from PySide6.QtCore import __version__ as pyside_version

from PySide6.QtGui import (
    QAction,
    QIcon,
    QFontDatabase,
    QTextDocument,
    QPageSize,
    QPageLayout,
    QFont
)
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidget,
    QTableWidgetItem,
    QFileDialog
)
from PySide6.QtCore import (
    QDate,
    QMargins,
    QSizeF
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


def calc_ro_water(tw, ta, ua, pa):
    # densidade da água segundo "Tanaka M. et al., Recommended table
    # for the density of water between 0 °C and 40 °C based on
    # recent experimental reports,  Metrologia,  2001, 38, 301-309  
    ro_w = 0.99997495 * (1 - (tw - 3.983035)**2 * (tw + 301.797)/(522528.9 * (tw + 69.34881)))
    return ro_w

def calc_ro_air(ta, ua, pa):
    # Densidade do ar de acordo com a ISO 8655-6:2022
    ro_a = (1 / 1000) * (0.34848 * pa - 0.009 * ua * math.e**(0.061 * ta))/(ta + 273.15)
    # cálculo de z de acordo com a ISO 8655-6:2022
    return ro_a


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Adicionando as fontes Cantarell
        QFontDatabase.addApplicationFont(os.path.join(basedir, "Cantarell-Regular.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir, "Cantarell-Bold.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir, "Cantarell-BoldItalic.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(basedir, "Cantarell-Italic.ttf"))
        # barra de botões
        button_calc = QAction(QIcon(os.path.join(basedir,"calc_icon.svg")), "Calcular", self)
        button_calc.triggered.connect(self.calcular)
        self.toolBar.addAction(button_calc)
        button_clear = QAction(QIcon(os.path.join(basedir,"clear_icon.svg")), "Limpar", self)
        button_clear.triggered.connect(self.clear_tables)
        self.toolBar.addAction(button_clear)
        button_relat = QAction(QIcon(os.path.join(basedir,"relat_icon.svg")), "Relatório", self)
        button_relat.triggered.connect(self.handlePrint)
        self.toolBar.addAction(button_relat)
        # populando drop list com o multiplicador pra apresentar o resultado em µL ou mL
        # e tipo de instrumento
        self.instKind.addItem("Balão volumétrico", (1, "bv"))
        self.instKind.addItem("Balão volumétrico (boca larga)", (1, "bvl"))
        self.instKind.addItem("Bureta", (1, "b"))
        self.instKind.addItem('Bureta "digital" manual', (1, "bdm"))
        self.instKind.addItem('Bureta "digital" motorizada', (1, "bda"))
        self.instKind.addItem("Dispensador", (1, "d"))
        self.instKind.addItem("Micropipeta tipo A|D1", (1000, "msa"))
        self.instKind.addItem("Micropipeta tipo D2", (1000, "msd2"))
        self.instKind.addItem("Micropipeta multicanal", (1000, "mm"))
        self.instKind.addItem("Pipeta graduada", (1, "pg"))
        self.instKind.addItem("Pipeta volumétrica", (1, "pv"))
        # populando drop list com o coeficiente de expansão térmica de acordo com o material
        self.instMat.addItem("Vidro borossilicato 3.3", 9.9e-6)
        self.instMat.addItem("Vidro borossilicato 5.0", 1.5e-5)
        self.instMat.addItem("Vidro soda-lime", 2.7e-5)
        self.instMat.addItem("Polipropileno (PP)", 2.4e-4)
        self.instMat.addItem("Poliestireno (PS)", 4.5e-4)
        self.instMat.addItem("Policarbonato (PC)", 2.1e-4)
        self.instMat.addItem("Perfluoroalcoxi alcano (PFA)", 3.9e-4)
        self.instMat.addItem("Polimetilpenteno (PMP)", 3.6e-4)
        # conecta o combo pra mudar as unidades entre µL e mL
        self.instKind.currentIndexChanged.connect(self.muda_unidade)
        # seta a data de hoje no caledário do dia do ensaio, pra facilitar a vida do usuário
        self.dateEdit.setDate(QDate.currentDate())
        # alinhando o cabeçalho das linhas nas duas tabelas
        self.tableData.verticalHeader().setFixedWidth(210)
        self.tableRes.verticalHeader().setFixedWidth(210)
    
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

    def clear_tables(self):
        self.tableData.clearContents() 
        self.tableRes.clearContents()

    def calcular(self):
        # limpando a tabela de resultados
        self.tableRes.clearContents()
        # resgatando qual multiplicador usar para calcular em mL ou µL
        mult = self.instKind.currentData()[0]
        # coeficiente de expansão térmica do material
        coef_term = self.instMat.currentData()
        # extarindo o array dos dados de massa
        table_array = []
        for i in range(self.tableData.columnCount()):
            col = []
            table_array.append(col)
            for j in range(self.tableData.rowCount()):
                item = self.tableData.item(j, i)
                if item is not None and item.text().strip():
                    text = item.text().replace(",", ".")
                    try:
                        col.append(float(text))
                    except ValueError:
                        print("." + text + "."  + str(i) + ", " + str(j))                        
        # extraindo as condições ambientais
        ta = self.tempAmb.value()
        pa = self.presAtm.value()
        ua = self.umidRel.value()
        m_evap = self.mEvap.value()
        ro_b = self.densPesos.value()
        # transformando massa em volume
        # um IF, pois há pequenas diferenças entre a ISO 4787 e a ISO 8655
        if self.instKind.currentData()[0] in ["bv", "bvl", "b", "pv", "pg"]:
            print("nada ainda")
        else:
            vol_array = []
            for column in table_array:
                if len(column) != 0:
                    tw = column[2]
                    vol = []
                    for i, ml in enumerate(column):
                        ro_w = calc_ro_water(tw, ta, ua, pa)
                        ro_a = calc_ro_air( ta, ua, pa)
                        if self.checkTara.isChecked():
                            v = (ml + m_evap) * 1/(ro_w + ro_a) * (1 - ro_a / ro_b) * (1 - coef_term * (tw - 20))
                            vol.append(v * mult)
                        else:
                            v = (ml - column[i - 1] + m_evap) * 1/(ro_w + ro_a) * (1 - ro_a / ro_b) * (1 - coef_term * (tw - 20))
                            vol.append(v * mult)
                    # restaurando o volume nominal, ensaiado
                    vol[0] = column[0]
                    vol[1] = column[1]
                    # removendo temperatura e massa do recipiente
                    vol.pop(2)
                    vol.pop(2)
                    # inserindo a coluna no novo array de volumes
                    vol_array.append(vol)
        # calculando os resultados
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
        # novo IF, pois a 47
        if self.instKind.currentData()[0] in ["bv", "bvl", "b", "pv", "pg"]:
            # ISO 4787:2021
            print("nada")
        else:
            # ISO 8655:2022
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


    def handlePrint(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Salvar arquivo', '', ".pdf (*.pdf)")
        if not filename[-4:] == ".pdf":
            filename = filename + ".pdf"
        if filename:
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPageSize(QPageSize.A4)
            printer.setPageOrientation(QPageLayout.Landscape)
            printer.setPageMargins(QMargins(0, 0, 0, 0))
            printer.setOutputFileName(filename)
            document = self.makeTableDocument()
            document.print_(printer)
    
    def makeTableDocument(self):
        document = QTextDocument()
        document.setPageSize(QSizeF(842, 596))
        document.setDocumentMargin(10)
        document.setDefaultFont(QFont("Cantarell", 7))
        html = """<html>
        <head>
        <title>Relatório de ensaio</title>
        <meta name="generator" content="V.A.CA. 1.0"/>
        </head>
        <body dir="ltr">
        <h1 align="center">Relatório de Ensaio</h1>
        """
        html += '<p><b>Identificação do equipamento: </b><big>' + self.instId.text() + '</big></p>'
        html += '<table width="100%"><tr><td width="50%">'
        html += '<p><b>Identificação dos instrumentos de medida utilizados:</b><br>'
        html += 'Balança: ' + self.balId.text() + '<br>'
        html += 'Termômetro (temp. ambiente): ' + self.termId.text() + '<br>'
        html += 'Termômetro (temp. da água): ' + self.term2Id.text() + '<br>'
        html += 'Barômetro: ' + self.barId.text() + '<br>'
        html += 'Higrômetro: ' + self.higId.text() + '</p>'
        html += '</td><td width="50%"></td>'
        html += '<p><b>Condições ambientais:</b><br>'
        html += 'Data de realização do ensaio: ' + self.dateEdit.date().toString("dd/MM/yyyy") + '<br>'
        html += 'Temperatura ambiente: ' + str(self.tempAmb.value()) + '°C <br>'
        html += 'Pressão atmosférica: ' + str(self.presAtm.value()) + ' hPa <br>'
        html += 'Umidade relativa do ar: ' + str(self.umidRel.value()) + '% </p></td></tr></table>'
        html += '<p><b>Dados das medidas de massa:</b></p>'
        html += '<table border="1" cellpadding="2" width="100%" style="border-collapse: collapse"><thead>'
        html += '<tr>'
        for c in range(self.tableData.columnCount() + 1):
            if c == 0:
                html += '<th width="16%" bgcolor="#E5E4E2"></th>'
            else:
                html += '<th bgcolor="#E5E4E2">{}</th>'.format(c)
        html += '</tr></thead>'
        html += '<tbody>'
        for r in range(self.tableData.rowCount()):
            html += '<tr>'
            html += '<td bgcolor="#E5E4E2">{}</td>'.format(self.tableData.verticalHeaderItem(r).text())
            for c in range(self.tableData.columnCount()):
                item = self.tableData.item(r, c)
                if item is not None  and item.text().strip():
                    text = item.text()
                    html += '<td>{}</td>'.format(text)
                else:
                    html += '<td>{}</td>'.format("-")
            html += '</tr>'
        html += '</tbody></table>'
        html += '<p><b>Resultados:</b></p>'        
        html += '<table border="1" cellpadding="2" width="100%" style="border-collapse: collapse"><thead>'
        html += '<tr>'
        for c in range(self.tableRes.columnCount() + 1):
            if c == 0:
                html += '<th width="16%" bgcolor="#E5E4E2"></th>'
            else:
                html += '<th bgcolor="#E5E4E2">{}</th>'.format(c)
        html += '</tr></thead>'
        html += '<tbody>'
        for r in range(self.tableRes.rowCount()):
            html += '<tr>'
            html += '<td bgcolor="#E5E4E2">{}</td>'.format(self.tableRes.verticalHeaderItem(r).text())
            for c in range(self.tableRes.columnCount()):
                item = self.tableRes.item(r, c)
                if item is not None  and item.text().strip():
                    text = item.text()
                    html += '<td>{}</td>'.format(text)
                else:
                    html += '<td>{}</td>'.format("-")
            html += '</tr>'
        html += '</tbody></table>'
        html += '<p align="right"><small>Impresso por V.A.Ca v. 1.0 em {}.</small></p></body></html>'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
#         html += '</tbody></table><div style="page-break-before:always"><p>Apenas um teste</p></div></body></html>'
        document.setHtml(html)
        return document

        
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