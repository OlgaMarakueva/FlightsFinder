
class DBReader:
    """
    Class for the database reader.
    ...
    Attributes
    --------
    conn : mysql connection

    Methods
    ------
    get_uniques(self, item):
        returns a list of all uniques for a chosen column from the "airports" table

    corr_name(self, name_str):
        corrects data from the database, which include a slash or quotes. Returns a corrected data

    pick_item(self, item_name, columns_names, item_col, all=False):
        sends queries to the database to get data for two columns based on the value of the third one.
        Returns lists for two columns

    find_routes(self, airport_dep, airport_arr):
        sends queries to the database to find flights between two lists of airports.
        Returns a list of flights
    """

    def __init__(self, conn):
        self.conn = conn

    def get_uniques(self, item):
        """ finds uniques for a particular column"""
        with self.conn.cursor() as cursor:
            # processes cities with one name but with different countries, add the corresponding ending to the city name
            if item == 'city':
                query1 = f"SELECT city FROM(SELECT city, country FROM airports GROUP BY city, country) " \
                         f"as a GROUP BY city HAVING COUNT(city) > 1"
                cursor.execute(query1)
                several_city = [tup[0] for tup in cursor.fetchall()]
                query = f"SELECT {item}, country FROM airports GROUP BY city, country ORDER BY {item}"
                cursor.execute(query)
                lst = [tup[0] + '--' + tup[1] if tup[0] in several_city
                       else tup[0] for tup in cursor.fetchall()]
            else:
                query = f"SELECT {item} FROM airports GROUP BY {item} ORDER BY {item}"
                cursor.execute(query)
                lst = [tup[0] for tup in cursor.fetchall()]
        return lst

    def corr_name(self, name_str):
        """ finds slashes and quotes in the names, corrects it so they could be used in queries"""
        if '\\' in name_str:
            name_str = name_str.replace('\\', '\\\\')
            if '"' in name_str:
                name_str = name_str.replace('"', '\\"')
        return name_str

    def pick_item(self, item_name, columns_names, item_col, all_mode=False):
        """ sends queries to the database to get data for the columns when one of them is changed"""
        item_name = self.corr_name(item_name)
        other = [n for i, n in enumerate(columns_names) if i != item_col]
        item = columns_names[item_col]
        with self.conn.cursor() as cursor:
            if item == 'city' and '--' in item_name:
                lst_1 = [item_name.split('--')[1]]
                query2 = (f"SELECT {other[1]} FROM airports WHERE city = '{item_name.split('--')[0]}' "
                          f"AND country = '{lst_1[0]}'")
            else:
                query1 = (f'SELECT {other[0]} FROM airports WHERE {item} = "{item_name}"'
                          f'GROUP BY {other[0]} ORDER BY {other[0]}')
                cursor.execute(query1)
                lst_1 = [row[0] for row in cursor.fetchall()]
                if item == 'country' and all_mode is False:
                    query2 = f'SELECT {other[1]} FROM airports WHERE city = "{self.corr_name(lst_1[0])}" ' \
                             f'ORDER BY {other[1]}'
                else:
                    query2 = (f'SELECT {other[1]} FROM airports WHERE {item} = "{item_name}" '
                              f'GROUP BY {other[1]} ORDER BY {other[1]}')
            cursor.execute(query2)
            lst_2 = [row[0] for row in cursor.fetchall()]
        return lst_1, lst_2

    def find_routes(self, airport_dep, airport_arr):
        """ finds flight between 2 lists with airports"""
        ap_dep = tuple(map(self.corr_name, airport_dep))
        ap_arr = tuple(map(self.corr_name, airport_arr))
        query = f"SELECT a.name, r.src_airport, r.dst_airport, ap_src.airport, ap_dst.airport " \
                f"FROM airlines a " \
                f"JOIN routes r ON r.airline_id = a.id " \
                f"JOIN airports ap_src ON r.src_airport = ap_src.iata " \
                f"JOIN airports ap_dst ON r.dst_airport = ap_dst.iata "
        if len(airport_dep) == 1:
            query = query + f'WHERE r.src_airport_id IN (SELECT id FROM airports WHERE airport = "{ap_dep[0]}") '
        elif len(airport_dep) > 1:
            query = query + f"WHERE r.src_airport_id IN (SELECT id FROM airports WHERE airport IN {ap_dep}) "
        if len(airport_arr) == 1:
            query = query + f'AND r.dst_airport_id IN (SELECT id FROM airports WHERE airport = "{ap_arr[0]}") '
        elif len(airport_arr) > 1:
            query = query + f"AND r.dst_airport_id IN (SELECT id FROM airports WHERE airport IN {ap_arr}) "
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            lst_ap = cursor.fetchall()
        out_lst = [(row[0], row[3] + ' (' + row[1] + ')', row[4] + ' (' + row[2] + ')') for row in lst_ap]
        return out_lst
