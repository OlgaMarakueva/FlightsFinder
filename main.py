import configparser
import mysql.connector
import sys
import model as m, controller as c, gui as v
from PyQt5 import QtWidgets

"""
The model allows to find flights between different countries/cities/airports.
The user can pick up one particular country/city/airport of departure and arrival 
or use an option 'All' in a corresponding column.
To find flights press the button "Find Flights"
"""

config = configparser.ConfigParser()
config.read("config.ini")
app = QtWidgets.QApplication(sys.argv)

try:
    conn = mysql.connector.connect(user=config['MySQLconn']['user'],
                                password=config['MySQLconn']['password'],
                                host=config['MySQLconn']['host'],
                                database=config['MySQLconn']['database'])
    c.AirportsController(m.DBReader(conn), v.UiMainWindow())
except mysql.connector.Error as err:
    print(f'Something wrong with the connection to the database: {err}')
    sys.exit(1)
sys.exit(app.exec_())



