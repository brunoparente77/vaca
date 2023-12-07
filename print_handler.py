from PySide6.QtCore import (
    QEventLoop,
    QObject,
    QPointF,
    Slot,
)
from PySide6.QtGui import QPainter
from PySide6.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QDialog,
    QProgressBar,
    QProgressDialog,
)

class PrintHandler(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_page = None
        self.m_inPrintPreview = False

    def setPage(self, page):
        assert not self.m_page
        self.m_page = page
        self.m_page.printRequested.connect(self.printPreview)

    @Slot()
    def print(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, QWebEngineView.forPage(self.m_page))
        if dialog.exec_() != QDialog.Accepted:
            return
        self.printDocument(printer)

    @Slot()
    def printPreview(self):
        if not self.m_page:
            return
        if self.m_inPrintPreview:
            return
        self.m_inPrintPreview = True
        printer = QPrinter()
        preview = QPrintPreviewDialog(printer, QWebEngineView.forPage(self.m_page))
        preview.paintRequested.connect(self.printDocument)
        preview.exec()
        self.m_inPrintPreview = False

    @Slot(QPrinter)
    def printDocument(self, printer):
        loop = QEventLoop()
        result = False

        def printPreview(success):
            nonlocal result
            result = success
            loop.quit()

        view = QWebEngineView.forPage(self.m_page)
        view.printFinished.connect(printPreview)
        progressbar = QProgressDialog(view)
        progressbar.findChild(QProgressBar).setTextVisible(False)
        progressbar.setLabelText("Wait please...")
        progressbar.setRange(0, 0)
        progressbar.show()
        progressbar.canceled.connect(loop.quit)
        view.print(printer)
        loop.exec()
        progressbar.close()
        if not result:
            painter = QPainter()
            if painter.begin(printer):
                font = painter.font()
                font.setPixelSize(20)
                painter.setFont(font)
                painter.drawText(QPointF(10, 25), "Could not generate print preview.")
                painter.end()