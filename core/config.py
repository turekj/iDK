class TaskConfiguration(object):
	def __init__(self, name, parameters):
		self.name = name
		self.parameters = parameters


class TaskConfigurationLoader(object):
	def load_configuration(self, path):
		return []
