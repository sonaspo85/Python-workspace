class customWinStyle:
    qss = """
        QPushButton {
            border: 1px solid #e63f30;
            font-family: '사각사각';
            font-size: 17px
        }
        QPushButton:hover {
            background-color: rgba(118, 45, 181, 0.6);   
        }
        QComboBox QAbstractItemView {
          selection-color: #e63f30;
          selection-background-color: #ca35f0;
        }
        QListWidget { 
            font-family: '사각사각';
        }

        QLabel {
            font-family: '사각사각';
            font-size: 15px
        }
        #mainTitle {
            font-family: '사각사각';
            font-size: 25px
        }
        QGroupBox {
            border: 1px solid #e63f30;
        }
        QLineEdit {
            border: 1px solid #e63f30;
        }

        """
