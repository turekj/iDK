TaskExecutionOrder = 0


class TaskOne(object):
	def __init__(self):
		self.order = -1
		self.parameters = None

	def execute_task(**kwargs):
		self.order = ++TaskExecutionOrder
		self.parameters = kwargs


class TaskTwo(object):
	def __init__(self):
		self.order = -1
		self.parameters = None

	def execute_task(**kwargs):
		self.order = ++TaskExecutionOrder
		self.parameters = kwargs
