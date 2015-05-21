import core.task
import os
import pytest
import shutil
import tasks.clone_task


class TestCloneTask(object):
	task = tasks.clone_task.CloneTask()

	def test_execute_raises_on_unsupported_repository_type(self):
		with pytest.raises(core.task.TaskParameterException):
			self.task.execute_task({'repository_type': 'git', 'repository_path': 'git@github.com:turekj/iDK.git', 'clone_path': 'test/project_clone'})

	def test_execute_clones_svn_repository(self):
		os.mkdir('test/project_clone')
		
		task_parameters = {'repository_type': 'svn', 'repository_path': 'http://gcs-admin-toolkit.googlecode.com/svn/trunk/', 'clone_path': 'test/project_clone'}
		self.task.execute_task(task_parameters)
		cloned = os.path.exists('test/project_clone/src/python/csvtocontentapi.py')

		shutil.rmtree('test/project_clone')

		assert cloned
