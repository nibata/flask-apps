from ..modules.graph_module import GraphBarData
from flask import render_template, request


class GraphController:
    def __init__(self, current_app):
        self.current_app = current_app
        self._test = {'A': ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                      "B": [12, 14, 26, 45, 24, 76, 43, 26, 98]}
        self._fig = GraphBarData(self._test, "A", "B")

    def index(self):
        graph_json = self._fig.get_filtered_graph()
        return render_template('views/graph/index.html', graphJSON=graph_json)

    def callback_graph(self):
        filter = [request.args.get("a_filter")]

        if "" in filter or "all" in filter:
            return self._fig.get_filtered_graph()

        else:
            return self._fig.get_filtered_graph(A=filter)
