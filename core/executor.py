import core.task


class TaskExecutor(object):
	def __init__(self, discovered_tasks):
		self.discovered_tasks = discovered_tasks

	def execute_tasks(self, tasks):
		for task_configuration in tasks:
			try:
				print "Executing task %s..." % task_configuration.name

				task = self.discovered_tasks[task_configuration.name]
				task.execute_task(task_configuration.parameters)

				print "Task %s executed successfully!" % task_configuration.name
			except core.task.TaskParameterException as e:
				print "Incorrect parameter %s for task %s: %s!" % (e.parameter_name, task_configuration.name, e.description)
				break
			except core.task.TaskGenericException as e:
				print "Exception during %s task execution: %s!" % (task_configuration.name, e.description)
				break
			except Exception as e:
				print "Unknown exception during %s task execution: %s!" % (task_configuration.name, str(e))
				break
