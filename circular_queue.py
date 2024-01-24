import threading

class CircularQueue:
	def __init__(self):
		self.size = 0
		self.max_size = 5
		self.queue = {}
		i = 0
		while i < self.max_size:
			self.queue[i+1] = None
			i += 1
		self.front = self.rear = 1

	def is_empty(self):
		return self.queue[self.front] == None

	def is_full(self):
		return (self.rear % self.max_size) == (self.front - 1)

	def size(self):
		if self.is_empty():
			return 0
		elif self.front <= self.rear:
			return self.rear - self.front + 1
		else:
			return self.size - self.front + self.rear + 1

	def enqueue_wrapper(self, item):
		if self.is_full():
			self.queue[self.rear] = item
		elif self.is_empty():
			self.front = self.rear = 1
		else:
			self.rear = (self.rear % self.max_size) + 1
		self.queue[self.rear] = item
		print("enqueue:", item)
		print("rear:", self.rear)
		return self.rear

	def enqueue(self, item):
		t1 = threading.Thread(target=self.enqueue_wrapper, args=(item,))
		t1.start()
		t1.join()

	def dequeue_wrapper(self):
		if self.is_empty():
			print("Queue is empty")
			return

		removed_item = self.queue[self.front]
		print("dequeue:", removed_item)
		self.queue[self.front] = None
		
		if self.front == self.rear:
			self.front = self.rear = 1
		else:
			self.front = (self.front % self.max_size) + 1
		print("front",self.front)
		return removed_item

	def dequeue(self):
		t1 = threading.Thread(target=self.dequeue_wrapper)
		t1.start()
		t1.join()

	def print_queue(self):
		print("Start")
		for key in self.queue:
			print(key, "->", self.queue[key])
		print("End")