from PyQt5.QtWidgets import QLineEdit


class FileDropLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            file_path = file_path.replace("/", "\\")
            self.setText(file_path)
            event.acceptProposedAction()
        else:
            event.ignore()
