import os
import shutil
import tasks.exchange_file_remote


class TestExchangeFileWithRemoteTask(object):
	task = tasks.exchange_file_remote.ExchangeFileWithRemoteTask()

	def test_execute_task(self):
		shutil.copy('test/res/to_be_rid.txt', 'test/res/to_be_rid_cp.txt')
		task_parameters = {'path': 'test/res/to_be_rid_cp.txt', 'remote_path': 'http://textfiles.com/stories/rid.txt'}
		self.task.execute_task(task_parameters)

		result_text = ''

		with open('test/res/to_be_rid_cp.txt', 'r') as result_text_file:
			result_text = result_text_file.read()

		os.remove('test/res/to_be_rid_cp.txt')

		expected = None

		with open('test/res/rid.txt', 'r') as expected_content_file:
			expected = expected_content_file.read()

		assert result_text == expected
