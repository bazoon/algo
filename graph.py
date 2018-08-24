class Vertex:
    pass

class SimpleGraph:
    def __init__(self, max_vertex):
        self.max_vertex = max_vertex
        self.m_adjacency = [[0] * max_vertex for i in range(max_vertex)]
        self.vertex = []

    def add_vertex(self, vertex):
    	self.vertex.append(vertex)
    	index = self.get_vertex_index(vertex)
    	return vertex

    def get_vertex_index(self, vertex):
    	return self.vertex.index(vertex)


    def add_edge(self, fromVertex, toVertex):
    	fromIndex = self.get_vertex_index(fromVertex)
    	toIndex = self.get_vertex_index(toVertex)
    	self.m_adjacency[fromIndex][toIndex] = 1
    	self.m_adjacency[toIndex][fromIndex] = 1

    def remove_edge(self, fromVertex, toVertex):
    	fromIndex = self.get_vertex_index(fromVertex)
    	toIndex = self.get_vertex_index(toVertex)
    	self.m_adjacency[fromIndex][toIndex] = 0
    	self.m_adjacency[toIndex][fromIndex] = 0

    def remove_vertex(self, vertex):
    	index = self.get_vertex_index(vertex)

    	for a in self.m_adjacency:
    		del a[index]

    	del self.m_adjacency[index]
    	del self.vertex[index]

s = SimpleGraph(4)
a = s.add_vertex(Vertex())
b = s.add_vertex(Vertex())

s.add_edge(a, b)
s.remove_vertex(a)
s.remove_vertex(b)
print(s.m_adjacency)