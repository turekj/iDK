import core.task
import traceback
import sys


class TaskExecutor(object):
	def __init__(self, discovered_tasks):
		self.discovered_tasks = discovered_tasks

	def execute_tasks(self, tasks):
		for task_configuration in tasks:
			try:
				print "Executing task %s..." % task_configuration.name

				if task_configuration.name in self.discovered_tasks:
					task = self.discovered_tasks[task_configuration.name]
					task.execute_task(task_configuration.parameters)
				else:
					print "Unknown task %s!" % task_configuration.name
					break 

				print "Task %s executed successfully!" % task_configuration.name
			except core.task.TaskParameterException as e:
				print "Incorrect parameter %s for task %s: %s!" % (e.parameter_name, task_configuration.name, e.description)
				break
			except core.task.TaskGenericException as e:
				print "Exception during %s task execution: %s!" % (task_configuration.name, e.description)
				break
			except Exception as e:
				print "Unknown exception during %s task execution!" % (task_configuration.name)
				traceback.print_exc()
				break
