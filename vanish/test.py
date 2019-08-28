#!python3

# code credit: Ansel

from adjancy_list import Graph
import unittest

class GraphTest(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        assert graph.size == 0

    def test_size(self):
        graph = Graph()

        # size should increase when a vertex is added
        assert graph.size == 0
        graph.add_vertex('A')
        assert graph.size == 1
        graph.add_vertex('B')
        assert graph.size == 2
        graph.add_vertex('C')
        assert graph.size == 3

        # size should increase once when an edgraphe is added with a new vertex
        graph.add_edge('A', 'B')
        assert graph.size == 3
        graph.add_edge('B', 'C')
        assert graph.size == 3
        graph.add_edge('C', 'D')
        assert graph.size == 4

        # size should increase twice when an edgraphe is added with two new vertices
        graph.add_edge('E', 'F')
        assert graph.size == 6

        # error should be raised when a vertex, that already exists, is added
        # size should not change when error is raised
        with self.assertRaises(KeyError):
            graph.add_vertex('B')  # Vertex already exists
        assert graph.size == 6
        with self.assertRaises(KeyError):
            graph.add_vertex('D')  # Vertex already exists
        assert graph.size == 6

    def test_add_vertex(self):
        graph = Graph()

        #graph should hae a newly added Vertex
        assert graph.size==0
        graph.add_vertex('A')
        assert graph.size == 1
        assert graph.has_vertex('A') is True
        graph.add_vertex('B')
        assert graph.size == 2
        assert graph.has_vertex('B') is True
        graph.add_vertex('C')
        assert graph.size == 3
        assert graph.has_vertex('C') is True

        #Test to raise rerror if vertex already exists
        with self.assertRaises(KeyError):
            graph.add_vertex('A')
        with self.assertRaises(KeyError):
            graph.add_vertex('B')
        with self.assertRaises(KeyError):
            graph.add_vertex('C')


    def test_add_edge(self):
        graph = Graph()

        # start with graph that already has vertices in it
        graph.add_vertex('A')
        assert graph.has_vertex('A') is True
        graph.add_vertex('B')
        assert graph.has_vertex('B') is True
        graph.add_vertex('C')
        assert graph.has_vertex('C') is True
        assert graph.size == 3

        print(graph.graph)

       # when edge is added with existing vertices, second vertex
       # should be a neighbor of first vertex
        graph.add_edge('A', 'B')
        self.assertCountEqual(graph.get_neighbors('A'), ['B'])
        self.assertCountEqual(graph.get_neighbors('B'), [])
        graph.add_edge('A', 'C')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])
        graph.add_edge('B', 'C')
        self.assertCountEqual(graph.get_neighbors('B'), ['C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])

        # when edge is added with nonexistent vertices, add nonexistent vertices
        # then, second vertex should be a neighbor of first vertex
        graph.add_edge('B', 'D')
        self.assertCountEqual(graph.get_neighbors('B'), ['C', 'D'])
        self.assertCountEqual(graph.get_neighbors('D'), [])
        graph.add_edge('E', 'F')
        self.assertCountEqual(graph.get_neighbors('E'), ['F'])
        self.assertCountEqual(graph.get_neighbors('F'), [])

        # when duplicate edge is added, the duplicate edge should be ignored
        graph.add_edge('A', 'C')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])
        graph.add_edge('E', 'F')
        self.assertCountEqual(graph.get_neighbors('E'), ['F'])
        self.assertCountEqual(graph.get_neighbors('F'), [])


    def test_has_vertex(self):
        graph = Graph()

        # has_vertex should return false if vertex not in graph
        # has_vertex should return true if vertex added through add_vertex
        assert graph.has_vertex('A') is False
        graph.add_vertex('A')
        assert graph.has_vertex('A') is True
        assert graph.has_vertex('B') is False
        graph.add_vertex('B')
        assert graph.has_vertex('B') is True
        assert graph.has_vertex('C') is False
        graph.add_vertex('C')
        assert graph.has_vertex('C') is True

        # has_vertex should return true if vertex added through add_edge
        assert graph.has_vertex('D') is False
        assert graph.has_vertex('E') is False
        graph.add_edge('D', 'E')
        assert graph.has_vertex('D') is True
        assert graph.has_vertex('E') is True


    def test_get_vertices(self):
        graph = Graph()

        # get_vertices should return all vertices added by add_vertex
        assert graph.has_vertex('A') is False
        graph.add_vertex('A')
        self.assertCountEqual(graph.get_vertices(), ['A'])
        assert graph.has_vertex('B') is False
        graph.add_vertex('B')
        self.assertCountEqual(graph.get_vertices(), ['A', 'B'])
        assert graph.has_vertex('C') is False
        graph.add_vertex('C')
        self.assertCountEqual(graph.get_vertices(), ['A', 'B', 'C'])

        # get_vertices should return all vertices added by add_edge
        assert graph.has_vertex('D') is False
        assert graph.has_vertex('E') is False
        graph.add_edge('D', 'E')
        self.assertCountEqual(graph.get_vertices(), ['A', 'B', 'C', 'D', 'E'])


    def test_get_neighbors(self):
        graph = Graph()

        # neighbors should return all vertices that a given vertex directs to
        # neighbors should not return any vertices that direct to a given vertex
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B')
        self.assertCountEqual(graph.get_neighbors('A'), ['B'])
        self.assertCountEqual(graph.get_neighbors('B'), [])
        graph.add_edge('A', 'C')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])


        # neighbors can return any vertices that direct to a given vertex,
        # if that vertex directs back as well
        graph.add_edge('C', 'A')
        self.assertCountEqual(graph.get_neighbors('C'), ['A'])
        graph.add_edge('C', 'B')
        self.assertCountEqual(graph.get_neighbors('C'), ['A', 'B'])


        # neighbor should still be added even if vertex is added through add_edge
        graph.add_edge('A', 'D')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C', 'D'])  # Item order does not matter
        self.assertCountEqual(graph.get_neighbors('D'), [])  # Item order does not matter

        # error should be raised when key is not in graph
        with self.assertRaises(KeyError):
            graph.get_neighbors('E')  # Vertex does not exist
        with self.assertRaises(KeyError):
            graph.get_neighbors('F')  # Vertex does not exist


if __name__ == '__main__':
    unittest.main()
