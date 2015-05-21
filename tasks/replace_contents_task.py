import core.task
import re


class ReplaceContentsTask(core.task.Task):
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['path', 'to_replace', 'replace_with'], parameters)
		path = parameters['path']
		to_replace = parameters['to_replace']
		replace_with = parameters['replace_with']

		file_contents = None

		with open(path, 'r') as file_handle:
			file_contents = file_handle.read()

		file_contents = re.subn(to_replace, replace_with, file_contents)[0]

		with open(path, 'w') as file_handle:
			file_handle.write(file_contents)
