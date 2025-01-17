import threading
from concurrent_and_linear_vector_sum.linear_vector_sum import linear_sum

class CustomThread(threading.Thread):
	def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, vervose=None):
		super().__init__(group, target, name, args, kwargs)
		self._return = None
        
	def run(self):
		if self._target is not None:
			self._return = self._target(*self._args, **self._kwargs)
	
	def join (self):
		super().join()
		return self._return
	







