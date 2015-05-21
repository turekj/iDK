import core.task
import pytest
import tasks.create_dir_task

class TestCreateDirectoryTask(object):
	task = tasks.create_dir_task.CreateDirectoryTask()

	def test_execute_raises_on_no_path_given(self):
		with pytest.raises(core.task.TaskParameterException):
			self.task.execute_task()

	def test_execute_raises_on_directory_exists(self):
		with pytest.raises(core.task.TaskGenericException):
			self.task.execute_task({'path': 'test/res'})
