
class AirportsController():
    """
    Class for the controller.
    ...
    Attributes
    --------
    reader : instance of the DBReader

    view: instance of the UiMainWindow

    cmb_lst: list of the comboboxes the controller works with

    cmb_names: names of comboboxes and columns of the database the controller work with

    Methods
    ------
    set_commands(self):
        sets commands to the widgets of the view

    btn_clicker(self):
        command connected to the button of the view

    cmbbox_clicker(self, inp, cmbboxes, col):
        command connected to the comboboxes of the view

    start_view(self):
        sets initial data for the comboboxes

    """

    def __init__(self, reader, view):
        self.reader = reader
        self.view = view
        self.cmb_lst = [(self.view.comboBox, self.view.comboBox_2, self.view.comboBox_3),
                        (self.view.comboBox_4, self.view.comboBox_5, self.view.comboBox_6)]
        self.cmb_names = ('country', 'city', 'airport')
        self.start_view()
        self.set_commands()

    def set_commands(self):
        """sets commands to the button"""
        self.view.pushButton.clicked.connect(self.btn_clicker)
        for cmb_set in self.cmb_lst:
            for i, cmb in enumerate(cmb_set):
                cmb.activated.connect(lambda e, x=cmb, lst=cmb_set, n=i: self.cmbbox_clicker(x.currentText(), lst, n))

    def btn_clicker(self):
        """command connected to the button, sends data to the DBReader, then received data sends to the UiMainWindow"""
        if self.view.comboBox.currentText() == 'All' and self.view.comboBox_4.currentText() == 'All':
            airport_arr = []
            airport_dep = []
        elif self.view.comboBox_3.currentText() != 'All' and self.view.comboBox_6.currentText() != 'All':
            airport_arr = [self.view.comboBox_3.currentText()]
            airport_dep = [self.view.comboBox_6.currentText()]
        elif self.view.comboBox_3.currentText() != 'All':
            airport_arr = [self.view.comboBox_3.currentText()]
            airport_dep = [self.view.comboBox_6.itemText(i) for i in range(self.view.comboBox_6.count())]
        elif self.view.comboBox_6.currentText() != 'All':
            airport_arr = [self.view.comboBox_3.itemText(i) for i in range(self.view.comboBox_3.count())]
            airport_dep = [self.view.comboBox_6.currentText()]
        else:
            airport_arr = [self.view.comboBox_3.itemText(i) for i in range(self.view.comboBox_3.count())]
            airport_dep = [self.view.comboBox_6.itemText(i) for i in range(self.view.comboBox_6.count())]
        flights = self.reader.find_routes(airport_arr, airport_dep)
        self.view.lbl_upd(len(flights))
        self.view.table_input(flights)

    def cmbbox_clicker(self, inp, cmbboxes, col):
        """command connected to the comboboxes, updates their data depending on the user's choose"""
        def upd_cmb(c_box, input):
            c_box.clear()
            c_box.addItem('All')
            c_box.addItems(input)

        if inp != 'All':
            outp = self.reader.pick_item(inp, self.cmb_names, col)
            j = 0
            for i, cmb in enumerate(cmbboxes):
                if i > col:
                    upd_cmb(cmb, outp[j])
                    cmb.setCurrentText(outp[j][0])
                    j += 1
                elif i < col:
                    cmb.setCurrentText(*outp[j])
                    j += 1
        else:
             if col == 0:
                 for i, cmb in enumerate(cmbboxes):
                     outp = self.reader.get_uniques(self.cmb_names[i])
                     upd_cmb(cmb, outp)
             elif col == 1:
                 current_country = cmbboxes[0].currentText()
                 if current_country != 'All':
                    outp = self.reader.pick_item(current_country, self.cmb_names, 0, all_mode=True)
                    upd_cmb(cmbboxes[2], outp[1])

    def start_view(self):
        """fills in comboboxes at start"""
        for cmb_set in self.cmb_lst:
            for i, cmb in enumerate(cmb_set):
                cmb.addItem('All')
                cmb.addItems(self.reader.get_uniques(self.cmb_names[i]))



