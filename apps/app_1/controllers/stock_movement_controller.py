from ..modules.table_module import TableToShow
from flask import render_template
import requests
import os


class StockMoveController:
    def __init__(self):
        self._table = None

    @property
    def url(self):
        url = os.environ.get("DB_API_URL")
        return f"{url}/stock/all"

    @property
    def table(self):
        return self._table

    def init_table(self, url):
        response_json = requests.get(url).json()
        self._table = TableToShow(data=response_json,
                                  columns_to_filter=["Product"],
                                  sorteables_columns=["Id","Product", "QuantityUnits"],
                                  columns_order=["Id", "Product", "TypeMovement", "TimeAt", "QuantityUnits"])

    def index(self):
        """ TODO: Ver si la funcion de inicio de tabla es candidato para ser almacenada en tabla
        https://stackoverflow.com/questions/15219858/how-to-store-a-complex-object-in-redis-using-redis-py
        """
        self.init_table(self.url)

        if self.table:
            columns_to_filter = self.table.columns_to_filter
            columns_to_sort = self.table.sorteable_columns
            columns = self.table.get_default_data_columns_config_to_display()

            return render_template('views/stock/index.html',
                                   title="Stock Test",
                                   columns=columns,
                                   columns_to_filter=columns_to_filter,
                                   columns_to_sort=columns_to_sort)

        return render_template('views/stock/index.html',
                               title="Stock Test")

    def data(self):
        rtn = self.table.display_data()
        return rtn
