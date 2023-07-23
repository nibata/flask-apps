import json
import plotly
import pandas as pd
import plotly.express as px


class GraphBarData:
    """
    Esta clase permite crear gráficos de líneas con sus respectivos filtros
    """
    def __init__(self, data: json, axis_x: str, axis_y: str):
        self._df_data = pd.DataFrame(data)
        self._axis_x = axis_x
        self._axis_y = axis_y

    @property
    def axis_x(self):
        return self._axis_x

    @axis_x.setter
    def axis_x(self, value: str):
        self._axis_x = value

    @property
    def axis_y(self):
        return self._axis_y

    @axis_y.setter
    def axis_y(self, value: str):

        self._axis_y = value

    def update_data_graph(self, data: json):
        aux_df = pd.DataFrame(data)
        self._df_data = aux_df

    def get_filtered_graph(self, **filters):
        """
        Obtiene el objeto json que se utiliza por plotly para graficar datos. Para que este método funcione asume que
        los datos entregados a la clase quedan en un formato de dataframe plano, es decir, sin índice más que el que
        se asigna por defecto.
        Parameters
        ----------
        filters
            name: corresponde con el nombre de la columna a filtrar
            value, list: corresponde a los valores por los que se están filtrando las columnas


        Returns
        -------
        JSON
             estructura de datos necesaria para que sea interpretada por plotly y mostrar el gráfico en una vista
        """
        df_filter = [True] * len(self._df_data)

        if filters is not None:
            for k, v in filters.items():
                if k in self._df_data.columns:
                    df_filter = df_filter & (self._df_data[k].isin(v))

        aux_df = self._df_data[df_filter]

        fig = px.bar(aux_df, x=self._axis_x, y=self._axis_y)
        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return graph_json
