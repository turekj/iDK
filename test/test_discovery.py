import core.discovery
import pytest
import test.res.dummy_task
import test.res.dummy_object
import test.res.dummy_object_task

class TestTaskDiscoverer(object):
	discoverer = core.discovery.TaskDiscoverer()

	def test_discover_tasks(self):
		tasks = self.discoverer.discover_tasks()
		
		assert len(tasks) == 1
		assert 'dummy' in tasks
		assert tasks['dummy'].__class__ is test.res.dummy_task.DummyTask

	def test_topmost_module(self):
		module = 'some.dummy.module_name'
		topmost_module = self.discoverer._topmost_module(module)

		assert topmost_module == 'module_name'
