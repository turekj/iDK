import core.task
import os


class RemoveDirectoryTask(core.task.Task):
	def execute_task(self, parameters=None):
		if isinstance(parameters, dict) and 'path' in parameters:
			path = parameters['path']
			
			if not os.path.exists(path):
				raise core.task.TaskGenericException('path %s does not exist' % path)
			else:
				os.rmdir(path)
		else:
			raise core.task.TaskParameterException('path', 'parameter is mandatory')
