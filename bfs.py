class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)


	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def rotate(self, n):
		while n > 0:
			self.enqueue(self.dequeue())
			n -= 1


class Vertex:
    def __init__(self, name):
        self.hit = False
        self.name = name

class SimpleGraph:
    def __init__(self, max_vertex):
        self.max_vertex = max_vertex
        self.m_adjacency = [[0] * max_vertex for i in range(max_vertex)]
        self.vertex = []

    def get_by_name(self, name):
        for vertex in self.vertex:
            if vertex.name == name:
                return vertex

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

    def get_adjacent(self, vertex):
        index = self.get_vertex_index(vertex)
        adjucent_row = self.m_adjacency[index]
        vertexes = [];

        for index, i in enumerate(adjucent_row):
            if i == 1:
                vertexes.append(self.vertex[index])

        return vertexes

    def dfs(self, fromVertex, toVertex):
        stack = Stack()
        for vertex in self.vertex:
            vertex.hit = False

        vertex = fromVertex

        while True:
            vertex.hit = True
            stack.push(vertex)
            adjacent_vertexes = [v for v in self.get_adjacent(vertex) if not v.hit]

            if toVertex in adjacent_vertexes:
                stack.push(toVertex)
                return stack
            else:
                if len(adjacent_vertexes) > 0:
                    vertex = adjacent_vertexes[0]
                else:
                    stack.pop()
                    if stack.size() == 0:
                        return False
                    else:
                        vertex = stack.pop()


    def bfs(self, fromVertex, toVertex):
    	def get_path(path, a, b):
	    	result = Queue()
	    	
	    	while path.has_key(b.name):
	    		result.enqueue(b)
	    		b = path[b.name]
	    	
	    	result.enqueue(a)
	    	return result

    	queue = Queue()
    	queue.enqueue(fromVertex)
    	
    	d = {};
    	vertex = None

    	while queue.size() > 0:
    		vertex = queue.dequeue()

    		if vertex == toVertex:
    			return get_path(d, fromVertex, toVertex)

    		vertex.hit = True
    		adjacent_vertexes = [v for v in self.get_adjacent(vertex) if not v.hit]
    		for x in adjacent_vertexes:
    			d[x.name] = vertex
    			queue.enqueue(x)

    
    	return False

s = SimpleGraph(10)

for x in ["a", "b", "c", "d", "e", "f", "g", "h"]:
    s.add_vertex(Vertex(x))

s.add_edge(s.get_by_name("a"), s.get_by_name("b"))
s.add_edge(s.get_by_name("a"), s.get_by_name("c"))
s.add_edge(s.get_by_name("b"), s.get_by_name("d"))
s.add_edge(s.get_by_name("b"), s.get_by_name("e"))
s.add_edge(s.get_by_name("c"), s.get_by_name("f"))
s.add_edge(s.get_by_name("c"), s.get_by_name("g"))
s.add_edge(s.get_by_name("e"), s.get_by_name("h"))

path = s.bfs(s.get_by_name("a"), s.get_by_name("h"))

print([p.name for p in path.items])








