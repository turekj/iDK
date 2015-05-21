import pkgutil
import sys


class TaskRegistry(object):
	Tasks = {}

	@classmethod
	def register_task(cls, task_cls):
		cls.Tasks[task_cls.__name__] = task_cls


class TaskDiscoverer(object):
	def discover_tasks(self):
		tasks = {}

		for cls_name, cls in TaskRegistry.Tasks.iteritems():
			if cls.__module__.endswith('_task'):
				task_name = self._topmost_module(cls.__module__)[:-5]
				tasks[task_name] = cls()

		return tasks

	def _topmost_module(self, module_name):
		if module_name is not None:
			module_parts = module_name.split('.')

			if len(module_parts) > 0:
				return module_parts[-1]

		return None
