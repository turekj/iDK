class TaskExecutor(object):
	def __init__(self, discovered_tasks):
		self.discovered_tasks = discovered_tasks

	def execute_tasks(self, tasks):
		for task_configuration in tasks:
			task = self.discovered_tasks[task_configuration.name]
			task.execute_task(task_configuration.parameters)
