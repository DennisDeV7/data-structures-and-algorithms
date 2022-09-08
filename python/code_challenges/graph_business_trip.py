from data_structures.graph import Graph
from data_structures.queue import Queue


def direct_flights(graph, places_list):
    price = 0
    breadth = Queue()
    visited = set()

    nodes = {}
    for vertex in graph.get_nodes():
        nodes[vertex.value] = vertex
    # nodes = graph.adjacency_list

    for place in places_list:
        breadth.enqueue(nodes[place])

    visited.add(nodes[places_list[0]])
    count = 1
    while not breadth.is_empty():
        if count < len(places_list):
            visited.add(nodes[places_list[count]])
        front = breadth.dequeue()
        direct_flights = graph.get_neighbors(front)

        for flight in direct_flights:
            if flight.vertex in visited:
                price += flight.weight / 2
        if price == 0:
            return (False, price)
        count += 1
    return (True, price)
