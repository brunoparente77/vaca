# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vacasfsDjU.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDateEdit, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 960)
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1220, 899))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(400, 0))
        self.widget_2.setMaximumSize(QSize(390, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 175))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
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

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEdit)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.instMat = QComboBox(self.groupBox)
        self.instMat.setObjectName(u"instMat")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.instMat)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 205))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
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

        self.term2Id = QLineEdit(self.groupBox_2)
        self.term2Id.setObjectName(u"term2Id")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.term2Id)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(0, 205))
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.presAtm = QDoubleSpinBox(self.groupBox_3)
        self.presAtm.setObjectName(u"presAtm")
        self.presAtm.setMinimum(600.000000000000000)
        self.presAtm.setMaximum(1100.000000000000000)
        self.presAtm.setSingleStep(0.100000000000000)
        self.presAtm.setValue(1013.250000000000000)

        self.gridLayout_2.addWidget(self.presAtm, 1, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 0, 0, 1, 1)

        self.umidRel = QDoubleSpinBox(self.groupBox_3)
        self.umidRel.setObjectName(u"umidRel")
        self.umidRel.setMinimum(20.000000000000000)
        self.umidRel.setMaximum(80.000000000000000)
        self.umidRel.setSingleStep(0.500000000000000)
        self.umidRel.setValue(45.000000000000000)

        self.gridLayout_2.addWidget(self.umidRel, 2, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 1, 0, 1, 1)

        self.tempAmb = QDoubleSpinBox(self.groupBox_3)
        self.tempAmb.setObjectName(u"tempAmb")
        self.tempAmb.setMinimum(15.000000000000000)
        self.tempAmb.setMaximum(27.000000000000000)
        self.tempAmb.setSingleStep(0.500000000000000)
        self.tempAmb.setValue(20.000000000000000)

        self.gridLayout_2.addWidget(self.tempAmb, 0, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.mEvap = QDoubleSpinBox(self.groupBox_3)
        self.mEvap.setObjectName(u"mEvap")
        self.mEvap.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.mEvap.setDecimals(5)
        self.mEvap.setMaximum(10.000000000000000)
        self.mEvap.setSingleStep(0.010000000000000)
        self.mEvap.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout_2.addWidget(self.mEvap, 3, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.densPesos = QDoubleSpinBox(self.groupBox_3)
        self.densPesos.setObjectName(u"densPesos")
        self.densPesos.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.densPesos.setDecimals(2)
        self.densPesos.setMinimum(1.000000000000000)
        self.densPesos.setMaximum(20.000000000000000)
        self.densPesos.setValue(8.000000000000000)

        self.gridLayout_2.addWidget(self.densPesos, 4, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 226))
        self.label_2.setPixmap(QPixmap(u"logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMinimumSize(QSize(0, 600))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkTara = QCheckBox(self.groupBox_5)
        self.checkTara.setObjectName(u"checkTara")

        self.verticalLayout_4.addWidget(self.checkTara)

        self.tableData = QTableWidget(self.groupBox_5)
        if (self.tableData.columnCount() < 5):
            self.tableData.setColumnCount(5)
        if (self.tableData.rowCount() < 14):
            self.tableData.setRowCount(14)
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
        self.tableData.setVerticalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(13, __qtablewidgetitem13)
        self.tableData.setObjectName(u"tableData")
        self.tableData.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableData.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableData.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableData.setAutoScroll(True)
        self.tableData.setCornerButtonEnabled(False)
        self.tableData.setRowCount(14)
        self.tableData.setColumnCount(5)
        self.tableData.horizontalHeader().setVisible(True)

        self.verticalLayout_4.addWidget(self.tableData, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(0, 205))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableRes = QTableWidget(self.groupBox_4)
        if (self.tableRes.columnCount() < 5):
            self.tableRes.setColumnCount(5)
        if (self.tableRes.rowCount() < 3):
            self.tableRes.setRowCount(3)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableRes.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableRes.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableRes.setVerticalHeaderItem(2, __qtablewidgetitem16)
        self.tableRes.setObjectName(u"tableRes")
        self.tableRes.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableRes.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableRes.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableRes.setAutoScroll(True)
        self.tableRes.setCornerButtonEnabled(False)
        self.tableRes.setRowCount(3)
        self.tableRes.setColumnCount(5)
        self.tableRes.horizontalHeader().setVisible(True)

        self.verticalLayout_5.addWidget(self.tableRes, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.groupBox_4, 0, Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"V.A.Ca.", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o do instrumento ensaiado:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o:", None))
        self.instId.setText(QCoreApplication.translate("MainWindow", u"Meu equipamento", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Data do ensaio:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o dos instrumentos utilizados:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Balan\u00e7a:", None))
        self.balId.setText(QCoreApplication.translate("MainWindow", u"Minha balan\u00e7a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Term\u00f4metro ambiente:", None))
        self.termId.setText(QCoreApplication.translate("MainWindow", u"Meu term\u00f4metro", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Bar\u00f4metro:", None))
        self.barId.setText(QCoreApplication.translate("MainWindow", u"Meu bar\u00f4metro", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Higr\u00f4metro:", None))
        self.higId.setText(QCoreApplication.translate("MainWindow", u"Meu higr\u00f4metro", None))
        self.term2Id.setText(QCoreApplication.translate("MainWindow", u"Meu outro term\u00f4metro", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Term\u00f4metro \u00e1gua:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Par\u00e2metros ambientais:", None))
        self.presAtm.setSuffix(QCoreApplication.translate("MainWindow", u" hPa", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Temperatura ambiente:", None))
        self.umidRel.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o atmosf\u00e9rica:", None))
        self.tempAmb.setSuffix(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Umidade relativa:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Perda por evapora\u00e7\u00e3o:", None))
        self.mEvap.setSuffix(QCoreApplication.translate("MainWindow", u" g", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dens. dos pesos de ref.:", None))
        self.densPesos.setSuffix(QCoreApplication.translate("MainWindow", u" g\u00b7mL\u207b\u00b9", None))
        self.label_2.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Dados do ensaio:", None))
        self.checkTara.setText(QCoreApplication.translate("MainWindow", u"Balan\u00e7a tarada entre as medidas", None))
        ___qtablewidgetitem = self.tableData.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Volume nominal, em mL", None));
        ___qtablewidgetitem1 = self.tableData.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Volume ensaiado, em mL", None));
        ___qtablewidgetitem2 = self.tableData.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Temperatura da \u00e1gua, em \u00b0C", None));
        ___qtablewidgetitem3 = self.tableData.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Massa do recipiente, em g", None));
        ___qtablewidgetitem4 = self.tableData.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1\u00aa medida, em g", None));
        ___qtablewidgetitem5 = self.tableData.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2\u00aa medida, em g", None));
        ___qtablewidgetitem6 = self.tableData.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3\u00aa medida, em g", None));
        ___qtablewidgetitem7 = self.tableData.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4\u00aa medida, em g", None));
        ___qtablewidgetitem8 = self.tableData.verticalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"5\u00aa medida, em g", None));
        ___qtablewidgetitem9 = self.tableData.verticalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"6\u00aa medida, em g", None));
        ___qtablewidgetitem10 = self.tableData.verticalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"7\u00aa medida, em g", None));
        ___qtablewidgetitem11 = self.tableData.verticalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"8\u00aa medida, em g", None));
        ___qtablewidgetitem12 = self.tableData.verticalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"9\u00aa medida, em g", None));
        ___qtablewidgetitem13 = self.tableData.verticalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"10\u00aa medida, em g", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Resultados:", None))
        ___qtablewidgetitem14 = self.tableRes.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Volume medido, em mL", None));
        ___qtablewidgetitem15 = self.tableRes.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Erro sistem\u00e1tico, em mL", None));
        ___qtablewidgetitem16 = self.tableRes.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Erro aleat\u00f3rio, em %", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

