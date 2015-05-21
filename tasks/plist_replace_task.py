import core.task
import plistlib


class PropertyListReplaceTask(core.task.Task):
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['path', 'contents'], parameters)
		path = parameters['path']
		contents = parameters['contents']

		if isinstance(contents, dict):
			property_list = self.replace_contents(plistlib.readPlist(path), contents)
			plistlib.writePlist(property_list, path)
		else:
			raise core.task.TaskParameterException('contents', 'contents must be of dictionary type')

	def replace_contents(self, property_list, contents_to_replace):
		for key in property_list:
			if key in contents_to_replace:
				if isinstance(property_list[key], dict):
					property_list[key] = self.replace_contents(property_list[key], contents_to_replace[key])
				else:
					property_list[key] = contents_to_replace[key]

		return property_list
