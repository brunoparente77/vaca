# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vacaDKGlBj.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 900)
        MainWindow.setMinimumSize(QSize(1024, 900))
        MainWindow.setMaximumSize(QSize(2048, 900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(350, 0))
        self.widget_2.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_28)

        self.instId = QLineEdit(self.groupBox)
        self.instId.setObjectName(u"instId")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.instId)

        self.label_29 = QLabel(self.groupBox)
        self.label_29.setObjectName(u"label_29")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_29)

        self.instKind = QComboBox(self.groupBox)
        self.instKind.setObjectName(u"instKind")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.instKind)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_4 = QFormLayout(self.groupBox_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.balId = QLineEdit(self.groupBox_2)
        self.balId.setObjectName(u"balId")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.balId)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.termId = QLineEdit(self.groupBox_2)
        self.termId.setObjectName(u"termId")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.termId)

        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_22)

        self.barId = QLineEdit(self.groupBox_2)
        self.barId.setObjectName(u"barId")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.barId)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_23)

        self.higId = QLineEdit(self.groupBox_2)
        self.higId.setObjectName(u"higId")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.higId)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.presAtm = QDoubleSpinBox(self.groupBox_3)
        self.presAtm.setObjectName(u"presAtm")
        self.presAtm.setMinimum(950.000000000000000)
        self.presAtm.setMaximum(1050.000000000000000)
        self.presAtm.setSingleStep(0.100000000000000)
        self.presAtm.setValue(1013.250000000000000)

        self.gridLayout_2.addWidget(self.presAtm, 1, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 2, 0, 1, 1)

        self.tempAmb = QDoubleSpinBox(self.groupBox_3)
        self.tempAmb.setObjectName(u"tempAmb")
        self.tempAmb.setMaximum(30.000000000000000)
        self.tempAmb.setSingleStep(0.500000000000000)
        self.tempAmb.setValue(20.000000000000000)

        self.gridLayout_2.addWidget(self.tempAmb, 0, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 1, 0, 1, 1)

        self.umidRel = QDoubleSpinBox(self.groupBox_3)
        self.umidRel.setObjectName(u"umidRel")
        self.umidRel.setMinimum(10.000000000000000)
        self.umidRel.setMaximum(100.000000000000000)
        self.umidRel.setSingleStep(0.500000000000000)
        self.umidRel.setValue(45.000000000000000)

        self.gridLayout_2.addWidget(self.umidRel, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(330, 251))
        self.label_2.setPixmap(QPixmap(u"logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QSize(0, 500))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableData = QTableWidget(self.groupBox_5)
        if (self.tableData.columnCount() < 12):
            self.tableData.setColumnCount(12)
        if (self.tableData.rowCount() < 12):
            self.tableData.setRowCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableData.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableData.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableData.setItem(0, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableData.setItem(0, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableData.setItem(0, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableData.setItem(0, 5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableData.setItem(0, 6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableData.setItem(0, 7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableData.setItem(0, 8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableData.setItem(0, 9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableData.setItem(0, 10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableData.setItem(0, 11, __qtablewidgetitem23)
        self.tableData.setObjectName(u"tableData")
        self.tableData.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableData.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableData.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableData.setCornerButtonEnabled(False)
        self.tableData.setRowCount(12)
        self.tableData.setColumnCount(12)
        self.tableData.horizontalHeader().setVisible(True)

        self.verticalLayout_3.addWidget(self.tableData)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableRes = QTableWidget(self.groupBox_4)
        if (self.tableRes.columnCount() < 12):
            self.tableRes.setColumnCount(12)
        if (self.tableRes.rowCount() < 3):
            self.tableRes.setRowCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableRes.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableRes.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableRes.setVerticalHeaderItem(2, __qtablewidgetitem26)
        self.tableRes.setObjectName(u"tableRes")
        self.tableRes.setColumnCount(12)

        self.verticalLayout_4.addWidget(self.tableRes)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o do instrumento ensaiado:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o dos instrumentos utilisados:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Balan\u00e7a:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Term\u00f4metro ambiente:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Bar\u00f4metro:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Higr\u00f4metro:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Term\u00f4metro \u00e1gua:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00f5es ambientais:", None))
        self.presAtm.setSuffix(QCoreApplication.translate("MainWindow", u" hPa", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Umidade relativa:", None))
        self.tempAmb.setSuffix(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Temperatura ambiente:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o atmosf\u00e9rica:", None))
        self.umidRel.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_2.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Dados do ensaio:", None))
        ___qtablewidgetitem = self.tableData.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Volume ensaiado, em mL", None));
        ___qtablewidgetitem1 = self.tableData.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Temperatura da \u00e1gua, em \u00b0C", None));
        ___qtablewidgetitem2 = self.tableData.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1\u00aa pesagem, em g", None));
        ___qtablewidgetitem3 = self.tableData.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2\u00aa pesagem, em g", None));
        ___qtablewidgetitem4 = self.tableData.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"3\u00aa pesagem, em g", None));
        ___qtablewidgetitem5 = self.tableData.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4\u00aa pesagem, em g", None));
        ___qtablewidgetitem6 = self.tableData.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5\u00aa pesagem, em g", None));
        ___qtablewidgetitem7 = self.tableData.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"6\u00aa pesagem, em g", None));
        ___qtablewidgetitem8 = self.tableData.verticalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"7\u00aa pesagem, em g", None));
        ___qtablewidgetitem9 = self.tableData.verticalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8\u00aa pesagem, em g", None));
        ___qtablewidgetitem10 = self.tableData.verticalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"9\u00aa pesagem, em g", None));
        ___qtablewidgetitem11 = self.tableData.verticalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10\u00aa pesagem, em g", None));

        __sortingEnabled = self.tableData.isSortingEnabled()
        self.tableData.setSortingEnabled(False)
        self.tableData.setSortingEnabled(__sortingEnabled)

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Resultados:", None))
        ___qtablewidgetitem12 = self.tableRes.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Volume medido, em mL", None));
        ___qtablewidgetitem13 = self.tableRes.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Erro sistem\u00e1tico, em %", None));
        ___qtablewidgetitem14 = self.tableRes.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Erro aleat\u00f3rio, em %", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

