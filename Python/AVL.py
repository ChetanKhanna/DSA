class Node():

	def __init__(self, val, right = None, left = None, parent = None):
		self.val = val
		self.right = right
		self.left = left
		self.parent = parent

	def __str__(self):
		return str(self.val)

	def __repr__(self):
		return repr(self.val)

	def balance_factor(self):
		self.balanceFactor  = 0
		if self.left:
			self.balanceFactor += 1
		if self.right:
			self.balanceFactor -= 1

	def is_left_child(self):
		if self.val < self.parent.val:
			return True
		else:
			return False

	def is_right_child(self):
		if self.val > self.parent.val:
			return True
		else:
			return False

class AVL():
	"""imlementing the AVL data type using Node class
		Addition and Deletion are Recursive
	"""
	def __init__(self):
		self.root = Node(None)

	def _create(self, val):
		if not self.root.val:
			self.root.val = val
		else:
			current = self.root
			stop = False
			while not stop:
				if val < current.val:
					if not current.left:
						current.left = Node(val, parent = current)
						self.update_balance(current.left)
						stop = True
					else:
						current = current.left
				elif val > current.val:
					if not current.right:
						current.right = Node(val, parent = current)
						self.update_balance(current.right)
						stop = True
					else:
						current = current.right
				else:
					stop = True

	def _delete(self, node):
		
		"since AVL tree are always balanced, we can simplfy deletion"
		"Additionaly, when node to be deleted has both children, we need to use"
		"height of tree or some method that reassigns balanceFactor of all nodes above it"

		node.val = None
		new_node = Node(None)
		parent = node.parent
		if not(node.left and node.right):
			if node.val > parent.val:
				parent.right = None
				node.parent = None
				parent.balanceFactor += 1
				self.update_balance(parent)
			else:
				parent.left = None
				node.parent = None
				parent.balanceFactor -= 1
				self.update_balance(parent)
		elif node.left and node.right:
			right = node.right
			left = node.left
			node.right = None
			node.left = None

			s_right = right.left
			while s_right:
				s_right = right.left

			right.parent = node.parent
			if node.val > node.parent.val:
				node.parent.right = right
			else:
				node.parent.left = right

			if s_right:
				left.parent = s_right
				s_right.left = left
			else:
				left.parent = right
				right.left = left
		else:
			if node.left:
				node.val = node.left.val
				node.left.parent = None
				node.left.val = None
				node.left = None
				node.balanceFactor -= 1
				self.update_balance_2(node)
			else:
				node.val = node.right.val
				node.right.parent = None
				node.right.val = None
				node.right = None
				node.balanceFactor += 1
				self.update_balance_2(node)



	def update_balance(self, node):
		if node.balanceFactor > 1 or node.balanceFactor < -1:
			self.rebalance(node)
			return

		if node.parent:
			if node.val < node.parent.val:
				node.parent.balanceFactor += 1
			else:
				node.parent.balanceFactor -= 1

			if node.parent.balanceFactor != 0:
				self.update_balance(node.parent)

	def height(self, node):
		pass

	def update_balance_2(self, node):
		if node.balanceFactor > 1 or node.balanceFactor < -1:
			self.rebalance(node)
			return

		if node.parent:
			if node.val < node.parent.val:
				node.parent.balanceFactor -= 1
			else:
				node.parent.balanceFactor += 1

			if node.parent.balanceFactor != 0:
				self.update_balance_2(node.parent)


	def create_AVL(self, arr):
		for val in arr:
			self._create(val)

	def add_val(self, val):
		self._create(val)

	def right_rotation(self, curr_root):
		new_root = curr_root.right
		curr_root.right = None

		new_root.parent = curr_root.parent
		curr_root.parent = new_root

		if new_root.parent:
			if curr_root.val > new_root.parent.val:
				new_root.parent.right = new_root
			else:
				new_root.parent.left = new_root

		if not new_root.left:
			new_root.left = curr_root
		else:
			curr_root.right = new_root.left
			new_root.left = curr_root
		

	def left_rotation(self, curr_root):
		new_root = curr_root.left
		curr_root.left = None

		new_root.parent = curr_root.parent
		curr_root.parent = new_root

		if new_root.parent:
			if curr_root.val > new_root.parent.val:
				new_root.parent.right = new_root
			else:
				new_root.parent.left = new_root

		if not new_root.right:
			new_root.right = curr_root
		else:
			curr_root.left = new_root.right
			new_root.right = curr_root

	def rebalance(node):
		if node.balanceFactor < -1:
			if node.right.balanceFactor > 0:
				self.right_rotation(node.right)
				self.left_rotation(node)
			else:
				self.left_rotation(node)
		elif node.balanceFactor > 1:
			if node.left.balanceFactor < 0:
				self.left_rotation(node.left)
				self.right_rotation(node)
			else:
				self.right_rotation(node)

# TEST CASES #
# ar = [8, 10, 12]
# at = AVL()
# at.create_AVL(ar)
# print(at.root.val)
# print(at.root.right.val)
# print(at.root.right.right.val)
# at.right_rotation(at.root)
# print("After rotation")
# print(at.root.parent.val)
# print(at.root.val, at.root.right.val, at.left.val)	
