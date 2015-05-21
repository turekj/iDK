import core.task
import os
import plistlib
import pytest
import shutil
import tasks.plist_replace_task


class TestPropertyListReplaceTask(object):
	task = tasks.plist_replace_task.PropertyListReplaceTask()

	def test_execute_task_raises_on_non_dict_content(self):
		task_parameters = {'path': 'test/res/sample_cp.plist', 'contents': 'test_contents'}

		with pytest.raises(core.task.TaskParameterException):
			self.task.execute_task(task_parameters)

	def test_execute_task(self):
		shutil.copy('test/res/sample.plist', 'test/res/sample_cp.plist')
		replace_contents = {"UIMainStoryboardFile": "UNITTEST", "UISupportedInterfaceOrientations": ["UIInterfaceOrientationLandscapeLeft", "UIInterfaceOrientationLandscapeRight"]}
		task_parameters = {'path': 'test/res/sample_cp.plist', 'contents': replace_contents}
		self.task.execute_task(task_parameters)

		property_list = plistlib.readPlist('test/res/sample_cp.plist')
		main_storyboard_file = property_list["UIMainStoryboardFile"]
		orientations = property_list["UISupportedInterfaceOrientations"]

		os.remove('test/res/sample_cp.plist')

		assert main_storyboard_file == "UNITTEST"
		assert len(orientations) == 2
		assert orientations[0] == "UIInterfaceOrientationLandscapeLeft"
		assert orientations[1] == "UIInterfaceOrientationLandscapeRight"
