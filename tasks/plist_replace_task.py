import core.task
import plistlib


class PropertyListReplaceTask(core.task.Task):
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['path', 'contents'], parameters)
		path = parameters['path']
		contents = parameters['contents']

		if isinstance(contents, dict):
			property_list = plistlib.readPlist(path)
		else:
			pass
