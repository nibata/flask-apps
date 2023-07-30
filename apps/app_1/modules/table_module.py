import json
import pandas as pd
from flask import request
from typing import List, Dict


class TableToShow:
    """
    Esta Clase permite que los datos provenientes de un formato json sencillo (sin estilo tabla, es decir filas y
    columnas simples) sea entregado en un formato compatible con GridJS
    """
    def __init__(self,
                 data: json, columns_alias: Dict = None,
                 columns_to_filter: List = None,
                 sorteables_columns: List = None):

        self._columns_to_filter = columns_to_filter
        self._columns_alias = columns_alias
        self._sorteable_columns = sorteables_columns
        self._df_data = pd.DataFrame(data)
        self._df_data.rename(columns=self._columns_alias, inplace=True)

    @property
    def columns_alias(self):
        return self._columns_alias

    @columns_alias.setter
    def columns_alias(self, value: Dict):
        self._columns_alias = value

    @property
    def columns_to_filter(self):
        return self._columns_to_filter

    @columns_to_filter.setter
    def columns_to_filter(self, value: List):
        self._columns_to_filter = value

    @property
    def sorteable_columns(self):
        return self._sorteable_columns

    @sorteable_columns.setter
    def sorteable_columns(self, value: List):
        self._sorteable_columns = value

    def update_data_table(self, data: json):
        aux_df = pd.DataFrame(data)
        aux_df.rename(columns=self._columns_alias, inplace=True)
        self._df_data = aux_df

    def get_default_data_columns_config_to_display(self, **extras) -> json:
        """
        Entrega en formato JSON la configuración básica para las columnas de la tabla a desplegar por GridJS

        Parameters
        ----------
        extras
            Configuraciones extras aceptadas por GridJS (no se verifica que sean válidas, solamente se entregan en
            formato aceptado por GridJS)
            name: nombre de la columna
            value: Dict:
                    name: nombre del argumento GridJS
                    value: valor aceptado por GridJS

        Returns
        -------
        JSON
            Configuración de columnas en formato json
        """

        rtn = []
        for v in self._df_data.columns.tolist():
            sorteable = v in self._sorteable_columns
            aux_column_config = {"id": v, "name": v, "sort": sorteable}

            extra_config = extras.get(v, None)
            if extra_config:
                aux_column_config.update(extra_config)

            rtn.append(aux_column_config)

        rtn = json.dumps(rtn)
        return rtn

    def display_data(self) -> Dict:
        """
        De los datos entregados en el constructor, obtiene del request los argumentos:
         'search'; 'sort'; 'start'; 'length'
        Con las variables anteriores se genera una estructura de datos ordenada según los criterios mencionados
        en los argumentos anteriores.
        'search' requiere que la propiedad `columns_to_filter` contenga al menos una de las columnas del dataframe
        Returns
        Dicicionario con los siguientes key:
            - data: List[Dict] - Representa la data a mostrar en la tabla
            - total: int - representa la cantidad de datos a mostrar
        -------

        """
        search = request.args.get("search")
        sort = request.args.get("sort")
        start = request.args.get("start", type=int, default=-1)
        length = request.args.get("length", type=int, default=-1)

        # SEARCH
        default_df_filter = [True] * len(self._df_data)
        df_filter = None

        if search:
            df_filter = [False] * len(self._df_data)
            if self._columns_to_filter is not None:
                for v in self._columns_to_filter:
                    df_filter = df_filter | (self._df_data[v].astype(str).str.contains(search))

        if df_filter is not None:
            aux_df = self._df_data[df_filter]
        else:
            aux_df = self._df_data[default_df_filter]

        # SORTING
        if sort:
            field = []
            ascending = []
            for s in sort.split(','):
                direction = s[0]
                name = s[1:]
                if name in self._sorteable_columns:
                    field.append(name)
                    is_ascending = False if direction == "-" else True
                    ascending.append(is_ascending)
            if field and ascending:
                aux_df.sort_values(by=field, ascending=ascending, inplace=True)

        # PAGINATION
        if start != -1 and length != -1:
            end = length * (start + 1)
            aux_df = aux_df.iloc[start:end]

        total = len(self._df_data)
        data = aux_df.to_dict("records")

        rtn = {
            "data": data,
            "total": total
        }

        return rtn
