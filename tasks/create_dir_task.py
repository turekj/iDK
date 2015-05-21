import core.task
import os


class CreateDirectoryTask(core.task.Task):
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['path'], parameters)
		path = parameters['path']
			
		if os.path.exists(path):
			raise core.task.TaskGenericException('path %s already exists' % path)
		else:
			os.mkdir(path)		
