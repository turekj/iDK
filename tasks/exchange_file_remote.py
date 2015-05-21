import core.task


class ExchangeFileWithRemoteTask(core.task.Task):
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['path', 'remote_path'], parameters)
		pass
