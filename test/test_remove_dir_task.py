import core.task
import os
import pytest
import tasks.remove_dir_task

class TestRemoveDirectoryTask(object):
	task = tasks.remove_dir_task.RemoveDirectoryTask()

	def test_execute_raises_on_no_path_given(self):
		with pytest.raises(core.task.TaskParameterException):
			self.task.execute_task()

	def test_execute_raises_on_directory_not_exists(self):
		with pytest.raises(core.task.TaskGenericException):
			self.task.execute_task({'path': 'test/non_existing_directory'})

	def test_execute_removes_directory(self):
		os.mkdir('test/non_existing_directory')

		self.task.execute_task({'path': 'test/non_existing_directory'})
		exists = os.path.exists('test/non_existing_directory')

		if os.path.exists('test/non_existing_directory'):
			os.rmdir('test/non_existing_directory')

		assert exists is False
