from circular_queue import CircularQueue
from password_check import *
from frequency import *
import unittest
import threading

class TestMethods(unittest.TestCase): 
	def test_CircularQueue_enqueue1(self):
		obj = CircularQueue()
		obj.enqueue_wrapper(1)
		obj.enqueue_wrapper(2)
		obj.enqueue_wrapper(3)
		obj.enqueue_wrapper(4)
		self.assertEqual(5,obj.enqueue_wrapper(5))

	def test_CircularQueue_enqueue2(self):
		obj = CircularQueue()
		obj.enqueue_wrapper(1)
		obj.enqueue_wrapper(2)
		obj.enqueue_wrapper(3)
		obj.enqueue_wrapper(4)
		obj.enqueue_wrapper(5)
		self.assertEqual(5,obj.enqueue_wrapper(15))

	def test_CircularQueue_dequeue1(self):
		obj = CircularQueue()
		obj.enqueue_wrapper(1)
		obj.enqueue_wrapper(2)
		obj.enqueue_wrapper(3)
		obj.enqueue_wrapper(4)
		obj.enqueue_wrapper(5)
		self.assertEqual(1,obj.dequeue_wrapper())

	def test_CircularQueue_dequeue2(self):
		obj = CircularQueue()
		obj.enqueue_wrapper(1)
		obj.enqueue_wrapper(2)
		obj.enqueue_wrapper(3)
		obj.enqueue_wrapper(4)
		self.assertEqual(1,obj.dequeue_wrapper())

	def test_check_password(self):
		s1 = "asqwr1234@1,aF145#,2w3E*,2We3345"
		self.assertEqual("aF145#",check_password(s1))

	def test_word_frequency(self):
		self.assertEqual({'2': 1, '3': 1, 'better': 1, 'is': 1, 'or': 1, 'python': 2, 'which': 1},
			word_frequency("sub_folder/words.txt"))


if __name__=="__main__": 

	s1 = "asqwr1234@1,aF145#,2w3E*,2We3345"

	t1 = threading.Thread(target=check_password, args=(s1,))
	t2 = threading.Thread(target=word_frequency, args=("sub_folder/words.txt",))

	t1.start()
	t2.start()
 
	t1.join()
	t2.join()

	obj = CircularQueue()
	obj.enqueue(1)
	obj.enqueue(2)
	obj.enqueue(3)
	obj.enqueue(4)
	obj.enqueue(5)
	obj.print_queue()
	obj.enqueue(15)
	obj.print_queue()
	obj.dequeue()
	obj.dequeue()
	obj.print_queue()
	obj.enqueue(25)
	obj.print_queue()
	obj.enqueue(35)
	obj.print_queue()
	obj.enqueue(45)
	obj.print_queue()
	obj.dequeue()
	obj.print_queue()

	print('done')

	unittest.main()

	