import core.task


class CloneTask(core.task.Task):
	def execute_task(self, parameters=None):
		if isinstance(parameters, dict) and parameters['repository_type'] is not None:
			repository_type = parameters['repository_type']

			if repository_type == 'svn':
				pass
			else:
				raise core.task.TaskParameterException('repository_type', 'unsupported repository type %s' % repository_type)	
		else:
			raise core.task.TaskParameterException('repository_type', 'repository type was not specified')
