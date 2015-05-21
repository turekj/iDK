import core.discovery


class TaskMetaClass(type):
	def __new__(cls, clsname, bases, attrs):
		new_cls = super(TaskMetaClass, cls).__new__(cls, clsname, bases, attrs)
		core.discovery.TaskRegistry.register_task(new_cls)	
		return new_cls


class TaskGenericException(Exception):
	def __init__(self, description):
		self.description = description


class TaskParameterException(TaskGenericException):
	def __init__(self, parameter_name, description):
		self.parameter_name = parameter_name
		self.description = description


class Task(object):
	__metaclass__ = TaskMetaClass

	def execute_task(self, parameters=None):
		pass

	def _check_mandatory_parameters(self, mandatory_parameter_names, supplied_parameters=None):
		if not isinstance(supplied_parameters, dict):
			if len(mandatory_parameter_names) > 0:
				raise TaskParameterException(mandatory_parameter_names[0], 'parameter is mandatory')
			else:
				return

		for parameter_name in mandatory_parameter_names:
			if parameter_name not in supplied_parameters:
				raise TaskParameterException(parameter_name, 'parameter is mandatory')
