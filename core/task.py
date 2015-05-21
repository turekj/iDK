import core.discovery


class TaskMetaClass(type):
	def __new__(cls, clsname, bases, attrs):
		new_cls = super(TaskMetaClass, cls).__new__(cls, clsname, bases, attrs)
		core.discovery.TaskRegistry.register_task(new_cls)	
		return new_cls


class Task(object):
	__metaclass__ = TaskMetaClass

	def execute_task(self, parameters=None):
		pass


class TaskGenericException(Exception):
	def __init__(self, description):
		self.description = description


class TaskParameterException(TaskGenericException):
	def __init__(self, parameter_name, description):
		self.parameter_name = parameter_name
		self.description = description
