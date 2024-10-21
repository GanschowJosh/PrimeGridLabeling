from prime_tools import coprime

class Node:
    """
        Defines the member nodes (verticies) of a Graph

        Typically, this shouldn't be accessed directly.
        Consider implementing functions that access Node or Node attributes as methods of Graph or a Graph subclass
    """


    def __init__(self, neighbors: list["Node"] = None, value: int = None):
        self.neighbors = neighbors if neighbors is not None else []
        self.value = value


    def get_neighbors(self) -> list["Node"]:
        """
            Returns a list of a Node's neighbors
        :return:
        """
        return self.neighbors.copy()


    def set_value(self, n: int):
        self.value = n


    def get_value(self) -> int:
        return self.value


    @classmethod
    def nodes(cls, n: int) -> list["Node"]:
        """
            An alternate constructor that creates n Nodes

            Use to simplify the initialization of Graph subclasses

            Example:

            def __init__(self, n: int):
                # defines a graph subclass with n nodes

                self.nodes = Node.nodes(n)

                ### Insert logic to link nodes here ###

                super().__init__(nodes)
        :param n:
        :return:
        """
        return [cls() for _ in range(n)]


    # Link an arbitrary number of nodes.
    # This only defines a bidirectional link
    # Executing this on every node in a graph creates a complete graph
    # this is broken somehow right now, so MatrixGraph.__init__ directly accesses each node's neighbors attribute
    # @staticmethod
    # def link(*nodes: "Node"):
    #     for node_a in nodes:
    #         for node_b in nodes:
    #             if node_a is not node_b and node_b not in node_a.neighbors:
    #                 node_a.neighbors.append(node_b)

    def __str__(self):
        """
            Use in debugging if the unique identity and value of a node needs to be known

            Example:

            print(Node)
        :return:
        """
        return f"Node {self.__hash__()}: {self.value}"


class Graph:
    """
        Defines an abstract class representing a graph (structure containing unique nodes connected by edges)

        Provides methods common to all graphs.

        Not meant to construct graphs directly, create subclasses instead that implement node linking logic.
    """

    def __init__(self, *nodes: Node):
        self.nodes = list(nodes)
        self.size = len(nodes)

    def get_size(self) -> int:
        """
            Return the number of nodes in the graph
        :return:
        """
        return self.size

    def is_empty(self) -> bool:
        """
            Returns boolean value indicating whether graph is empty (no nodes are labelled)
        :return:
        """
        for node in self.nodes:
            if node.value is not None:
                return False

        return True

    def is_full(self) -> bool:
        """
            Returns boolean value indicating whether graph is full (every node is labelled)
        :return:
        """
        for node in self.nodes:
            if node.value is None:
                return False
        return True

    def get_node(self, n: int) -> Node:
        return self.nodes[n]

    def nodes_by_degree(self) -> list[Node]:
        """
            returns a list of the graph's nodes, sorted by degree (number of neighbors)
        :return:
        """
        return sorted(self.nodes.copy(), key=lambda x: len(x.neighbors))

    def node_index_by_degree(self) -> list[int]:
        """
            return a list of the indexes of the graph's nodes, sorted by degree (number of neighbors)
        :return:
        """
        return sorted(range(self.size), key=lambda x: len(self.nodes[x].neighbors))

    def filled_adj_nodes(self) -> list[Node]|None:
        """
            Gets a list of free nodes that are adjacent to non-free nodes

            If there are no free nodes adjacent to non-free nodes (if the graph is empty/full)
            returns None
        """

        unoccupied_node = (node for node in self.nodes if node.value is None or node.value == 0)
        occupied_adj_node = []

        for node in unoccupied_node:
            neighbor_values = (neighbor.value for neighbor in node.neighbors if neighbor.value is not None)

            if neighbor_values:
                occupied_adj_node.append(node)

        if not occupied_adj_node:
            return None
        return occupied_adj_node

    def print_linked_value(self) -> None:
        """
            Print, for each node, it's value, followed by a list of the values of it's neighbors
        :return:
        """
        for node in self.nodes:
            print(f"{node.get_value()}: ", " ".join(str(x) for x in (i.get_value() for i in node.get_neighbors())))


class CompleteCoprimeGraph(Graph):
    """
        Defines Graph with n nodes labelled 1 through n

        Every node is connected to every other node for which their values are coprime
    """
    def __init__(self, n: int):

        # create n nodes
        nodes = Node.nodes(n)

        # initialize Graph with nodes
        super().__init__(*nodes)

        # label each node
        for i in range(self.size):
            self.get_node(i).set_value(i+1)

        # link every node to every other node it with which it is coprime
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                # print(f"Checking {i+1}, {j+1}")
                if coprime(i+1, j+1):

                    self.get_node(i).neighbors.append(
                        self.get_node(j)
                    )

                    self.get_node(j).neighbors.append(
                        self.get_node(i)
                    )


class MatrixGraph(Graph):
    """
        Defines a graph where the nodes, if each occupied a space on
        an 'n' dimensional tessellation of hypercubes (a grid),
        are linked to their orthagonally adjacent neighbors
    """
    
    # yeah, this is something better handled by numpy. I'll switch to that,
    # but this'll get the project off the ground
    @staticmethod
    def add_coords(*coords: list[int]):
        """
            Perform vector addition on at least two coordinates, returning the summed vectors as a single coordinate
        :param coords:
        :return:
        """
        return [sum(x) for x in zip(*coords)]
    
    def is_valid_coordinate(self, coords: list[int]):
        """
            Check if a given coordinate lies within the valid coordinate space of the graph
        :param coords:
        :return:
        """
        for i in range(len(self.dim)):
            if coords[i] >= self.dim[i] or coords[i] < 0:
                return False
        return True


    def orth_adj_vect(self):
        """
            A generator that yields a unit vector and it's inverse for every dimension in the coordinate space
        :return:
        """
        for i in range(len(self.dim)):
            vect = [0 for _ in range(len(self.dim))]
            vect[i] = 1
            yield vect.copy()
            vect[i] = -1
            yield vect.copy()


    def possible_coords(self):
        """
            A generator that yields every possible coordinate in the coordinate space
        :return:
        """
        vect = [0 for _ in range(len(self.dim))]

        while True:
            yield vect.copy()  # yield a copy to avoid mutations outside
            
            for i in range(len(vect)):
                if vect[i] < self.dim[i] - 1:
                    vect[i] += 1
                    for j in range(i):
                        vect[j] = 0
                    break
            else: # else in a for loop gets executed only if the loop completes without encountering a break
                # if we complete the loop without a break, all coordinates are exhausted
                return

    def linearize(self, coord: list[int]) -> int:
        """
            Maps any coordinate in the graph's coordinate space onto a one-dimensional index

            Used internally by MatrixGraph to index nodes in the nodes list
        :param coord:
        :return:
        """
        index = 0
        stride = 1
        for i in range(len(self.dim)):
            index += coord[i] * stride
            stride *= self.dim[i]
        return index
    
    def get_node_by_coord(self, coord: list[int]):
        """
            Get any node in the graph by coordinate
        :param coord:
        :return:
        """
        return self.nodes[self.linearize(coord)]

    def __init__(self, *dim: int):
        self.dim = list(dim)
        volume = 1

        # pycharm doesn't realize the := operator produces a side-effect
        # and so thinks this list comprehension has no effect
        # noinspection PyStatementEffect
        [volume := volume * i for i in self.dim] # is there an easier way to do this? probably. is it shorter? possibly.
                                                 # but this uses the cool walrus 'assign and return' operator, so it's better.
        # Construct every node the graph will need
        nodes = Node.nodes(volume)
        super().__init__(*nodes)

        for coord in self.possible_coords():

            possible_neighbors = [self.add_coords(coord, vect) for vect in self.orth_adj_vect()]
            valid_neighbors_coord = filter(self.is_valid_coordinate, possible_neighbors)
            valid_nodes = [self.get_node_by_coord(neighbor_coord) for neighbor_coord in valid_neighbors_coord]

            self.get_node_by_coord(coord).neighbors = valid_nodes


def print_2d_matrix_graph(graph: MatrixGraph, mute=False) -> str:
    """
        Takes a MatrixGraph with two dimensions, and formats and prints the values of
        every member node to std out if mute = False

        Also returns the generated string representation, regardless of mute's value
    :param graph:
    :return:
    """

    if len(graph.dim) != 2:
        raise ValueError("MatrixGraph with other than 2 dimensions provided")

    graph_string = ""

    for i in range(graph.dim[1]):
        for j in range(graph.dim[0]):
            value = str(graph.get_node_by_coord([j, i]).value)
            # value = "0" if value is None else str(value) # now, 0 is not treated as None
            print(value + " " * (5 - len(value)), end="")
            graph_string += value + " " * (5 - len(value))
        graph_string += "\n"

    if mute == False:
        print(graph_string)

    return graph_string
