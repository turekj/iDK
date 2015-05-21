import core.task
import os
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

	def test_execute_creates_directory(self):
		self.task.execute_task({'path': 'test/new_dir'})
		exists = os.path.exists('test/new_dir')

		if os.path.exists('test/new_dir'):
			os.remove('test/new_dir')

		assert exists is True
