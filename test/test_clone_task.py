import core.task
import pytest
import tasks.clone_task


class TestCloneTask(object):
	task = tasks.clone_task.CloneTask()

	def test_execute_raises_on_no_repository_type(self):
		with pytest.raises(core.task.TaskParameterException):
			self.task.execute_task()

	def test_execute_raises_on_unsupported_repository_type(self):
		with pytest.raises(core.task.TaskParameterException):
			self.task.execute_task({'repository_type': 'git'})
