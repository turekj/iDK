import core.discovery


class TaskMetaClass(type):
	def __new__(cls, clsname, bases, attrs):
		new_cls = super(TaskMetaClass, cls).__new__(cls, clsname, bases, attrs)
		core.discovery.TaskRegistry.register_task(new_cls)	
		return new_cls


class Task(object):
	__metaclass__ = TaskMetaClass

	def execute_task(**kwargs):
		pass

