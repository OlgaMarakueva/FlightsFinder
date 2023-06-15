from PyQt5 import QtCore, QtWidgets


class UiMainWindow:
    """
    Class for the GUI.
    ...
    Attributes
    --------
    MainWindow : The main window of the GUI

    Methods
    ------
    setupUi(self, MainWindow):
        creates and sets up widgets in the main window

    table_input(self, data):
        fills in tableWidget with the data received from the controller

    lbl_upd(self, txt):
        updates the label with number of flights

    """
    style = """
                .QWidget{
                    background-color: #2F4F4F;
                }
                QComboBox{
                    color: black;
                    background-color: #9C9C9C;
                    border-radius: 5px;
                    font-size: 12pt;
                    selection-color: #2F4F4F;
                    selection-background-color: #EED5D2;
                }
                QListView{
                    color: black;
                    background-color: #9C9C9C;
                    selection-color: #2F4F4F;
                    selection-background-color: #EED5D2;
                }
                QLabel{
                    color : #EED5D2;
                    font-size: 12pt;
                    font-weight: bold;
                }
                QPushButton{
                    color: #2F4F4F;
                    background-color: #9C9C9C;
                    border-radius: 5px;
                    font-size: 12pt; 
                    font-weight: bold;
                }
                QTableWidget{
                    background: #EED5D2;
                    border-radius: 10px;
                    font-size: 10pt;
                }
                QTableWidget::item
                {
                    background: #EED5D2;
                }
                QHeaderView::section
                {
                    background: #EED5D2;
                    font-size: 10pt;
                    font-weight: bold;
                }
                QAbstractButton:hover
                {
                    background: #EED5D2;
                }
                QTableCornerButton::section
                {
                    background: #EED5D2;
                }
        }   
            """

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        """ creates, sets up all the widgets in the main window, applies the style sheet"""
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(991, 876)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle('FlightsFinder')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 931, 831))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 10, 0, 10)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel("FROM", self.gridLayoutWidget)
        self.label2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3 = QtWidgets.QLabel("TO", self.gridLayoutWidget)
        self.label4 = QtWidgets.QLabel("COUNTRY", self.gridLayoutWidget)
        self.label5 = QtWidgets.QLabel("CITY", self.gridLayoutWidget)
        self.label6 = QtWidgets.QLabel("AIRPORT", self.gridLayoutWidget)

        lbl_list = [(self.label, (80, 0), (50, 16777215), (1, 0, 1, 1)),
                    (self.label2, (100, 0), (400, 16777215), (3, 0, 1, 2)),
                    (self.label3, (0, 0), (50, 16777215), (2, 0, 1, 1)),
                    (self.label4, (0, 0), (250, 16777215), (0, 1, 1, 1)),
                    (self.label5, (0, 0), (250, 16777215), (0, 2, 1, 1)),
                    (self.label6, (250, 0), (250, 16777215), (0, 3, 1, 1))]

        for i, lbl in enumerate(lbl_list):
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(lbl[0].sizePolicy().hasHeightForWidth())
            lbl[0].setSizePolicy(sizePolicy)
            lbl[0].setMinimumSize(QtCore.QSize(*lbl[1]))
            lbl[0].setMaximumSize(QtCore.QSize(*lbl[2]))
            if i > 2:
                lbl[0].setAlignment(QtCore.Qt.AlignCenter)
            lbl[0].setObjectName("label_" + str(i))
            self.gridLayout.addWidget(lbl[0], *lbl[3])

        self.label2.setStyleSheet("color: white")

        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget)

        cmb_lst = [(self.comboBox, (1, 1, 1, 1)),
                   (self.comboBox_2, (1, 2, 1, 1)),
                   (self.comboBox_3, (1, 3, 1, 1)),
                   (self.comboBox_4, (2, 1, 1, 1)),
                   (self.comboBox_5, (2, 2, 1, 1)),
                   (self.comboBox_6, (2, 3, 1, 1))]

        for i, cmb in enumerate(cmb_lst):
            cmb[0].setSizePolicy(sizePolicy)
            cmb[0].setMinimumSize(QtCore.QSize(0, 35))
            cmb[0].setMaximumSize(QtCore.QSize(250, 16777215))
            cmb[0].setObjectName("comboBox_" + str(i))
            self.gridLayout.addWidget(cmb[0], *cmb[1])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(cmb[0].sizePolicy().hasHeightForWidth())

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('Airlines', 'Departure from', 'Arrival to'))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 4)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.pushButton = QtWidgets.QPushButton("Find Flights", self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.gridLayout.addLayout(self.horizontalLayout, 3, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.centralwidget.setLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setStyleSheet(self.style)

    def table_input(self, data):
        """insert data to the table widget"""
        self.tableWidget.setRowCount(len(data))
        for i, d in enumerate(data):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(d[0]))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(d[1]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(d[2]))

    def lbl_upd(self, txt):
        """updates the label with the number of flights"""
        self.label2.setText(f'{txt} flights were found')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UiMainWindow()
    sys.exit(app.exec_())
