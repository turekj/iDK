import collections
import yaml


class TaskConfiguration(object):
	def __init__(self, name, parameters):
		self.name = name

		if parameters is not None:
			self.parameters = parameters
		else:
			self.parameters = []


class TaskConfigurationLoaderException(Exception):
	pass


class TaskConfigurationLoader(object):
	def load_configuration(self, path):
		stream = file(path, 'r')
		configuration = yaml.load(stream)
		stream.close()

		if configuration is not None and 'tasks' in configuration:
			return [TaskConfiguration(name, parameters) for name, parameters in configuration['tasks'].iteritems()]
		else:
			raise TaskConfigurationLoaderException


_mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG

def dict_representer(dumper, data):
    return dumper.represent_dict(data.iteritems())

def dict_constructor(loader, node):
    return collections.OrderedDict(loader.construct_pairs(node))

yaml.add_representer(collections.OrderedDict, dict_representer)
yaml.add_constructor(_mapping_tag, dict_constructor)
