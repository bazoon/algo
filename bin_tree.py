class TreeNode:
    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key

class Tree:
    def __init__(self):
        self.root = None


    def print_all(self):
    	def aux(node):
    		if node != None:
    			aux(node.left_child)
    			print(node.key)
    			aux(node.right_child)

    	aux(self.root)

    def add(self, key):

    	def aux(root):
    		if (root == None):
    			root = TreeNode(self.root, key)
    			if self.root == None:
    				self.root = root
	    	else:
	    		if (root.key <= key):
	    			if root.right_child == None:
	    				root.right_child = TreeNode(root, key)
	    			else:
	    				aux(root.right_child)
	    		else:
	    			if root.left_child == None:
	    				root.left_child = TreeNode(root, key)
	    			else:
	    				root.left_child = aux(root.left_child)

	    	return root

    	aux(self.root)

    def find(self, key):
    	def aux(node):
    		if node is None:
    			return None
    		if node.key == key:
    			return node

    		if node.key < key:
    			return aux(node.right_child)
    		else:
    			return aux(node.left_child)


    	return aux(self.root)


    def find_max_from(self, node):
    	if node is None or node.right_child is None:
    		return node
    	return self.find_max_from(node.right_child)

    def find_min_from(self, node):
    	if node is None or node.left_child is None:
    		return node
    	return self.find_min_from(node.left_child)

    def remove_node(self, node):

    	# no children
        if node.left_child is None and node.right_child is None:
            if node.parent != None:
                if node.parent.left_child == node:
                    node.parent.left_child = None
                else:
                    node.parent.right_child = None
        # have left child
        # Copy the child to the node and delete the child
        elif node.left_child != None and node.right_child is None:
            if node.parent != None:
                if node.parent.left_child == node:
                    node.parent.left_child = node.left_child
                else:
                    node.parent.right_child = node.left_child
        elif node.left_child is None and node.right_child != None:
            if node.parent != None:
                if node.parent.left_child == node:
                    node.parent.left_child = node.right_child
                else:
                    node.parent.right_child = node.right_child
        else:
            # two children
            successor = self.find_min_from(node.right_child)


            if successor.right_child != None:
                right_child = self.find_max_from(successor.right_child)
                right_child.right_child = node.right_child
                successor.parent.left_child = None
                if node.parent is None:
                    self.root = successor
            else:
                node.key = successor.key
                node.right_child = None

            successor.left_child = node.left_child


        

        
                
        
        

	






t = Tree()
# t.add(120)
# t.add(140)
# t.add(115)


t.add(40)
t.add(70)
t.add(60)
t.add(80)
t.add(65)
t.add(66)

a= t.find(80)
t.remove_node(a)
t.print_all()
# print(t.root.left_child.right_child.key)

# t.inorder(t.root)

# print(t.find_min_from(t.root))


