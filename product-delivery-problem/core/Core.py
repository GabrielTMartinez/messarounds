import networkx as nx
import os
import re


class Core:

    customers_routes = nx.DiGraph()

    def run(self):
        weighted_edges_text = input('Enter the graph in the format: AD4, DE1, EC8, ...\n').lower()
        edgeTextList = re.findall('([a-zA-Z]{2}\d)', weighted_edges_text)
        edges = []
        for edgeText in edgeTextList:
            chars = list(edgeText)
            tuple = (chars[0], chars[1], int(chars[2]))
            edges.append(tuple)

        customers_routes = nx.DiGraph()
        customers_routes.add_weighted_edges_from(edges)
        self.customers_routes = customers_routes

        f = open(os.getcwd() + '/core/resources/routesList.txt', 'r')
        lines = f.read().split('\n')
        for line in lines:
            self.print_route_cost(line)

    def print_route_cost(self, route: str):
        WEIGHT_ATTR_NAME = 'weight'

        total_route_cost = 0

        customers_in_route = route.split('-')
        route_size = len(customers_in_route)
        for i in range(0, route_size):
            if i < route_size - 1:
                parcialRoute = self.customers_routes.get_edge_data(customers_in_route[i], customers_in_route[i + 1])

                if parcialRoute is None:
                    print('NO SUCH ROUTE')
                    return

                total_route_cost = total_route_cost + parcialRoute[WEIGHT_ATTR_NAME]

        print(total_route_cost)
