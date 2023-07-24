from ..modules.table_module import TableToShow
from flask import render_template
import json


class TableController:
    def __init__(self, current_app):
        self.current_app = current_app
        self._test = {'A': ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9", "j10", "k11", "l12"],
                      "B": [12, 14, 26, 45, 24, 76, 43, 26, 98, 23, 45, 86],
                      "C": [142, 142, 264, 455, 264, 776, 743, 626, 598, 345, 234, 980]}
        self._table = TableToShow(data=self._test,
                                  columns_alias={"A": "Column A"},
                                  columns_to_filter=["B", "C"],
                                  sorteables_columns=["Column A", "B"])

    def index(self):
        columns_to_filter = self._table.columns_to_filter
        columns_to_sort = self._table.sorteable_columns
        columns_name = self._table.get_data_columns_config_to_display()

        return render_template('views/table/index.html',
                               title="Table Example",
                               columns_name=columns_name,
                               columns_to_filter=columns_to_filter,
                               columns_to_sort=columns_to_sort)

    def data(self):
        rtn = self._table.display_data()
        return rtn
