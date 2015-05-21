import core.task
import os


class CreateDirectoryTask(core.task.Task):
	def execute_task(self, parameters=None):
		if isinstance(parameters, dict) and 'path' in parameters:
			path = parameters['path']
			
			if os.path.exists(path):
				raise core.task.TaskGenericException('path %s already exists!' % path)
			else:
				os.mkdir(path)
		else:
			raise core.task.TaskParameterException('path', 'parameter is mandatory!')
		
