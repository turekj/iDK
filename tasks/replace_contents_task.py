import core.task


class ReplaceContentsTask(core.task.Task):
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['path', 'to_replace', 'replace_with'], parameters)
