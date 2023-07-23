from ..modules.table_module import TableToShow
from flask import render_template


class TableController:
    def __init__(self, current_app):
        self.current_app = current_app
        self._test = {'A': ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                      "B": [12, 14, 26, 45, 24, 76, 43, 26, 98, 23, 45, 86],
                      "C": [142, 142, 264, 455, 264, 776, 743, 626, 598, 345, 234, 980]}
        self._table = TableToShow(data=self._test,
                                  columns_alias={"A": "Column_A"},
                                  columns_to_filter=["B", "C"],
                                  sorteables_columns=["Column_A"])

    def index(self):
        """
        TODO: hacer que la vista reconozca las columnas que son ordenables. Actualmente la parte funcional está
              implementada pero visualmente las columnas que no se pueden ordenar siguen mostrando como que se pudieran
              ordenar de alguna manera.
        """
        return render_template('views/table/index.html', title="Table Example")

    def data(self):
        rtn = self._table.display_data()
        return rtn
