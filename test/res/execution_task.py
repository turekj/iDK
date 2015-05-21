class TaskStub(object):
	TaskOrder = 0

	def __init__(self):
		self.order = -1
		self.parameters = None

	def execute_task(self, parameters):
		TaskStub.TaskOrder += 1
		self.order = TaskStub.TaskOrder
		self.parameters = parameters


class TaskOne(TaskStub):
	pass


class TaskTwo(TaskStub):
	pass
