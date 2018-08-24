
class Editor():
	def __init__(self):
		self.s = ""
		self.undos = []
		

	def op(self, s):
		operation = s[0]
		text = s[2:]

		if operation == "1":
			self.add(text)
		elif operation == "2":
			self.remove(int(text))
		elif operation == "3":
			self.puts(int(text))
		elif operation == "4":
			self.undo()
		else:
			print('Unknown operation!')
			print("Enter 1 to append")
			print("Enter 2 to remove")
			print("Enter 3 to print char")
			print("Enter 4 to undo")

	def add(self, s):
		self.store()
		self.s += s

	def remove(self, n):
		self.store()
		if len(self.s) > n:
			self.s = self.s[:-n]
		else:
			print("Can not remove substring! Current string is too small")
		

	def puts(self, n):
		print(self.s[n])

	def undo(self):
		if len(self.undos) > 0:
			self.s = self.undos.pop()
		else:
			print('Nothing to undo!')

	def store(self):
		self.undos.append(self.s)


	def run(self):
		while True:
			text = input("Enter command: ") 
			self.op(text)
			print("Current string: " + self.s)


e = Editor()


# Run script at console to see editor working in action
e.run()